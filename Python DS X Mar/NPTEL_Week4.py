# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 08:48:55 2023

@author: Nilakshi
"""

# To work with dataframes
import pandas as pd 

# To perform numerical operations
import numpy as np

# To visualize data
import seaborn as sns

# To partition the data
from sklearn.model_selection import train_test_split

# Importing library for logistic regression
from sklearn.linear_model import LogisticRegression

# importing the library of KNN
from sklearn.neighbors import KNeighborsClassifier  

# Importing performance metrics - accuracy score & confusion matrix
from sklearn.metrics import accuracy_score,confusion_matrix

###############################################################################
# =============================================================================
# Importing data
# =============================================================================
data = pd.read_csv('ServiceTest.csv',na_values=[" ?"]) 

# =============================================================================
# Data pre-processing
# =============================================================================

data.isnull().sum()

missing = data[data.isnull().any(axis=1)]
# axis=1 => to consider at least one column value is missing in a row

data2 = data.dropna(axis=0)


# Reindexing the salary status names to 0,1 
# Encode categorical variable, Service - Yes as 1 and No as 0 for both the train and test datasets
data2['Service']=data2['Service'].map({' No':0,' Yes':1})
print(data2['Service'])

new_data=pd.get_dummies(data2, drop_first=True)

# Storing the column names 
columns_list=list(new_data.columns)
print(columns_list)

# Separating the input names from data
features=list(set(columns_list)-set(['Service']))
print(features)

# Storing the output values in y
y=new_data['Service'].values
print(y)

# Storing the values from input features
x = new_data[features].values
print(x)

# Splitting the data into train and test
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3, random_state=0)

# Make an instance of the Model
logistic = LogisticRegression()
'''
# Fitting the values for x and y
logistic.fit(train_x,train_y)
logistic.coef_
logistic.intercept_

# Prediction from test data
prediction = logistic.predict(test_x)
print(prediction)

# Confusion matrix
confusion_matrix = confusion_matrix(test_y, prediction)
print(confusion_matrix)

# Calculating the accuracy
accuracy_score=accuracy_score(test_y, prediction)
print(accuracy_score)
'''