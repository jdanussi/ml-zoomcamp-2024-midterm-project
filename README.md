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
Pipenv was used to create the virtual environment and install the dependencies. In order to follow the development of the project you must clone the repository, create the virtual environment installing the required dependencies and activate the environment as shown below


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

# Deploy a local service for water potability prediction using Flash
python predict.py

# Test the flask web service from other terminal of the same instance
python predic-test.py

# Deploy a local service for water potability prediction using a docke container
docker run -it --rm -p 9696:9696 potability-predict:latest

# Test the containerized service from other terminal of the same instance
python predic-test.py

# Test the same service deployed in AWS Elasticbealstalk
python predic-test-eb.py 

```