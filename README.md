# EDA LangChain Agent

## Author: Huzaifa Tahir
- **Email:** huzaifatahir7524@gmail.com
- **LinkedIn:** [linkedin.com/in/huzaifatahir7524](https://linkedin.com/in/huzaifatahir7524)
- **GitHub:** [github.com/Huzaifa7524](https://github.com/Huzaifa7524)

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Documentation](#documentation)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

The EDA LangChain Agent is an advanced tool for performing Exploratory Data Analysis (EDA) using natural language queries. It leverages the power of large language models and the LangChain framework to provide comprehensive insights into datasets, generate visualizations, and offer statistical analyses.

This tool is designed to streamline the EDA process, making it more accessible to data scientists, analysts, and researchers of all skill levels. By using natural language processing, it allows users to explore their data through intuitive queries, receiving in-depth analyses and visualizations in response.

## Features

- **Natural Language Queries**: Ask questions about your data in plain English.
- **Comprehensive EDA**: Covers data overview, descriptive statistics, distribution analysis, correlation analysis, and more.
- **Automatic Visualization**: Generates relevant plots and charts based on the data and query.
- **Statistical Analysis**: Performs various statistical tests and provides interpretations.
- **Machine Learning Insights**: Offers suggestions for potential machine learning models and preprocessing steps.
- **SQL Integration**: Utilizes SQL for efficient data querying and manipulation.
- **Interactive Web Interface**: Built with Streamlit for easy use and deployment.

## Requirements

- Python 3.10+
- OpenAI API  + GROQ key 
- Required Python libraries (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Huzaifa7524/eda-langchain-agent.git
   cd eda-langchain-agent
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API and Groq key as an environment variable:
   ```
   OPENAI_API_KEY = "sk-proj-"
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    os.environ["GROQ_API_KEY"] = "gsk_"
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run eda_langchain_agent.py
   ```

2. Open the provided URL in your web browser.

3. Upload your CSV file using the file uploader.

4. Enter your EDA query in the text input field. You can ask specific questions about your data or type "Perform comprehensive EDA" for a full analysis.

5. Click the "Analyze" button to process your query.

6. Review the analysis results, including text insights and visualizations.

## Configuration

You can modify the `comprehensive_eda_prompt` in the script to customize the behavior of the AI assistant. This allows you to tailor the analysis to your specific needs or domain.

## Documentation

For a detailed explanation of the prompt engineering techniques used in this project, please refer to the [Prompt Engineering Documentation](docs/prompt_engineering.md).

For a line-by-line explanation of the code, see the [Code Documentation](docs/code_explanation.md).

## Contributing

Contributions to the EDA LangChain Agent are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

Please ensure that your code adheres to the existing style and that you have tested your changes thoroughly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

