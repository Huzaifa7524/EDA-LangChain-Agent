# EDA LangChain Agent: Prompt Engineering Documentation

## Table of Contents
- [EDA LangChain Agent: Prompt Engineering Documentation](#eda-langchain-agent-prompt-engineering-documentation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prompt Structure](#prompt-structure)
  - [Prompt Flow](#prompt-flow)
  - [Techniques Used](#techniques-used)
  - [Prompt Components](#prompt-components)
    - [System Message](#system-message)
    - [Human Message Template](#human-message-template)
    - [AI Message for SQL Context](#ai-message-for-sql-context)
    - [Agent Scratchpad](#agent-scratchpad)
  - [Customization and Improvement](#customization-and-improvement)

## Introduction

This document details the prompt engineering techniques used in the EDA LangChain Agent. Prompt engineering is crucial for guiding the AI to perform comprehensive Exploratory Data Analysis (EDA) tasks effectively.

## Prompt Structure

The EDA LangChain Agent uses a multi-part prompt structure to guide the AI's behavior:

1. System Message: Defines the AI's role and provides detailed guidelines
2. Human Message Template: Structures user queries and sets expectations
3. AI Message: Provides context for SQL functions
4. Agent Scratchpad: Allows for the AI's thought process to be included

## Prompt Flow

![prompt-flow](/images/prompt_flow.png)

## Techniques Used

1. **Role-Playing**: The AI is assigned a specific role as an EDA specialist.
2. **Detailed Instruction Sets**: Comprehensive guidelines for various aspects of EDA.
3. **Task Decomposition**: Breaking down the EDA process into specific steps.
4. **Few-Shot Learning**: Providing examples of expected output format.
5. **Context Injection**: Supplying relevant context about SQL functions and dataframe naming.
6. **Error Prevention**: Including notes on potential pitfalls and how to avoid them.
7. **Output Structuring**: Guiding the AI to provide structured, actionable insights.

## Prompt Components

### System Message

The system message defines the AI's role and provides detailed guidelines for the EDA process. It covers:

- Data overview
- Descriptive statistics
- Distribution analysis
- Correlation analysis
- Advanced statistical analysis
- Data visualization
- Feature engineering suggestions
- Missing data analysis
- Outlier detection
- Machine learning model recommendations

### Human Message Template

The human message template structures user queries and sets expectations for the AI's response. It includes:

- A placeholder for the user's specific query
- Instructions to provide SQL queries, statistical analyses, and visualization code
- A reminder to use consistent naming conventions

### AI Message for SQL Context

This component provides context about available SQL functions, enhancing the AI's ability to generate appropriate SQL queries for data analysis.

### Agent Scratchpad

The agent scratchpad allows for the inclusion of the AI's thought process, making the analysis more transparent and debuggable.

## Customization and Improvement

The prompt can be customized to focus on specific types of analysis or adapted for particular domains. Potential improvements include:

- Adding domain-specific terminology and analysis techniques
- Incorporating more advanced statistical methods
- Expanding machine learning model suggestions
- Enhancing visualization recommendations based on data characteristics

By continually refining the prompt based on user feedback and results, the EDA LangChain Agent can be made more effective and versatile.

