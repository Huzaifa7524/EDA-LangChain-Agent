import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, select, insert
from langchain.prompts.chat import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent import AgentExecutor
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.prompt import SQL_FUNCTIONS_SUFFIX
from langchain_core.messages import AIMessage, SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.agents import create_openai_tools_agent
from langchain_groq import ChatGroq

OPENAI_API_KEY = ""
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

os.environ["GROQ_API_KEY"] = ""

def create_sqlite_database(df, db_name='eda_data.db'):
    engine = create_engine(f'sqlite:///{db_name}')
    df.to_sql('dataset', engine, if_exists='replace', index=False)
    return engine

def extract_python_code(text):
    code_blocks = []
    lines = text.split('\n')
    in_code_block = False
    current_block = []

    for line in lines:
        if line.strip().startswith('```python'):
            in_code_block = True
        elif line.strip() == '```' and in_code_block:
            in_code_block = False
            code_blocks.append('\n'.join(current_block))
            current_block = []
        elif in_code_block:
            current_block.append(line)

    return code_blocks

def main():
    st.title("EDA LangChain Agent with Visualization")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        file_name = uploaded_file.name
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.write(df.head())

        engine = create_sqlite_database(df)
        
        llm=ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")
        
        db = SQLDatabase.from_uri(f"sqlite:///eda_data.db")
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)

        context = toolkit.get_context()
        
        messages = [
            SystemMessage(content="""
                You are an advanced AI assistant specializing in Exploratory Data Analysis (EDA), statistics, data visualization, and machine learning. Your task is to provide comprehensive insights into the uploaded dataset. Follow these guidelines:

                1. Data Overview:
                - Summarize the dataset's structure (rows, columns, data types).
                - Identify the target variable if applicable.
                - Detect any immediate data quality issues (missing values, outliers).

                2. Descriptive Statistics:
                - Provide summary statistics for numerical columns (mean, median, std, min, max, quartiles).
                - For categorical columns, show frequency distributions and unique value counts.
                - Identify skewness and kurtosis in numerical data.

                3. Data Distribution Analysis:
                - Analyze the distribution of each numerical variable (normal, skewed, multimodal).

                4. Correlation Analysis:
                - Compute and interpret correlation matrices for numerical variables.
                - For categorical variables, consider chi-square tests or cramer's V for association.

                5. Data Visualization:
                - Generate appropriate visualizations for different data types and analyses:
                    * Histograms and KDE plots for distributions
                    * Box plots and violin plots for numerical summaries and outlier detection
                    * Scatter plots and pair plots for relationships between variables
                    * Bar plots and pie charts for categorical data
                    * Heatmaps for correlation matrices
                    * Time series plots if temporal data is present
                - Always provide complete Python code for each visualization, including necessary imports.
                - Use 'df' as the name of the dataframe in your visualization code.

                6. Missing Data Analysis:
                - Quantify and visualize missing data patterns.
                - Suggest appropriate imputation techniques based on the data's nature.

                7. Outlier Detection and Treatment:
                - Identify outliers using statistical methods (Z-score, IQR) and visualizations.
                - Propose strategies for handling outliers based on their nature and impact.

                8. Machine Learning Model Recommendations:
                    - Based on the data characteristics and potential target variable, suggest suitable ML models.
                    - Explain why these models are appropriate for the given data.
                    - Highlight potential challenges in modeling (class imbalance, high dimensionality).
                    - Suggest evaluation metrics appropriate for the problem and data type.

                Always provide clear explanations of your findings, their implications, and the reasoning behind your suggestions. Use SQL queries for data extraction and analysis where appropriate, and provide complete Python code for all visualizations and statistical tests. Remember to use 'df' as the name of the dataframe in all your code examples.
            """),
            HumanMessagePromptTemplate.from_template("""
            Perform the following EDA task:{file_name}
                                                     table_name: dataset
            {input}

            Provide a detailed analysis covering the aspects mentioned in the guidelines, including relevant SQL queries, 
            statistical analyses, and Python code for visualizations.
            """),
            AIMessage(content=SQL_FUNCTIONS_SUFFIX),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]

        prompt = ChatPromptTemplate.from_messages(messages)
        prompt = prompt.partial(**context, file_name=file_name,tabel_name='dataset')

        agent = create_openai_tools_agent(llm, toolkit.get_tools(), prompt)

        agent_executor = AgentExecutor(
            agent=agent,
            tools=toolkit.get_tools(),
            verbose=True,
        )

        st.subheader("Ask Questions About Your Data")
        query = st.text_input("Enter your EDA query:")

        if st.button("Analyze"):
            if query:
                try:
                    with st.spinner("Analyzing..."):
                        response = agent_executor.invoke({"input": query})
                        st.markdown("### Analysis Results")
                        st.markdown(response["output"])

                        # Extract and execute Python code for visualization
                        code_blocks = extract_python_code(response["output"])
                        for code in code_blocks:
                            try:
                                exec(code)
                                st.pyplot(plt)
                                plt.close()
                            except Exception as e:
                                st.error(f"Error executing visualization code: {e}")

                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("Please enter a query before analyzing.")

if __name__ == "__main__":
    main()