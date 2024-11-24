# Water Quality Prediction

# Summary
1. Problem Description
2. Dependency and environment management
3. EDA
4. Data preparation
5. Model training and tuning
6. Comparing models' performance and training the best
7. Creating python scripts from notebook
8. Local model deployment with Flask
9. Local model deployment with Docker
10. Cloud model deployment with AWS Elastic Beanstalk


## 1. Problem Description
Drinking water or potable water is water that is safe for ingestion, either when drunk directly in liquid form or consumed indirectly through food preparation. It is often (but not always) supplied through taps, in which case it is also called tap water.

For the ML Zoomcamp mid-term project, several machine learning models were evaluated, and the best-performing one was deployed as a public web application on AWS using Elastic Beanstalk.

The dataset used is the one found on Kaggle: https://www.kaggle.com/datasets/adityakadiwal/water-potability


## 2. Dependency and environment management
Pipenv was used to create the virtual environment and install the dependencies. In order to follow the development of the project you must clone the [repository](https://github.com/jdanussi/ml-zoomcamp-2024-midterm-project.git), create the virtual environment installing the required dependencies and activate it as demonstrated below.


```bash

# Clone the project repository
git clone https://github.com/jdanussi/ml-zoomcamp-2024-midterm-project.git

# Change dir to the project folder
cd ml-zoomcamp-2024-midterm-project

# Create a new virtual environment and install the project dependencies
pipenv install

# Activate the new environment
pipenv shell

# Check the python path in the new environment
which python

```


## 3. EDA
In statistics, exploratory data analysis (EDA) is an approach of analyzing data sets to summarize their main characteristics, often using statistical graphics and other data visualization methods.

In the EDA section of the notebook, summary statistics of the dataset were examined, missing values were imputed using mean values, and the correlations between variables were analyzed. Most variables were found to be largely independent, except for a notable correlation between solids and sulfate, and a weaker correlation between solids and ph.


## 4. Data preparation

