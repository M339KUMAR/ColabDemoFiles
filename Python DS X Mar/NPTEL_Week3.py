# -*- coding: utf-8 -*-
"""
Created on Sat Feb 08 07:44:17 2025

@author: Nilakshi
"""

import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

cars_data = pd.read_csv('Toyota.csv')

cars_data = pd.read_csv('Toyota.csv',index_col=0) #first column becomes index column

#creating copy of original data
cars_data1 = cars_data.copy(deep = True)


#To get index of the dataframe
index = cars_data1.index
print(index)

#To get the headings of the columns
headings = cars_data1.columns
print(headings)

#size
sz = cars_data1.size
print(sz)

#shape
sh = cars_data1.shape
print(sh)

#memory usage of each column in bytes
memo = cars_data1.memory_usage()
print(memo)

#array dimension
dim = cars_data1.ndim
print(dim)

#The function head returns the first n rows from the dataframe
nrow = cars_data1.head(6) #6 means upto 5 rows
print(nrow)

#The function tail returns the last n rows for the object based on position
pos = cars_data1.tail(5)
print(pos)


#at provides label-based scalar lookups
sc_at = cars_data1.at[4,'FuelType']
print(sc_at)

#iat provides integer-based lookups
sc_iat = cars_data1.iat[4,5]
print(sc_iat)

#To access a group of rows and columns by label(s) .loc[ ] can be used
grp = cars_data1.loc[:,'FuelType']
print(grp)


#object type
tp = cars_data1.dtypes
print(tp)

#returns a subset of the columns from dataframe based on the column dtypes
col_tp = cars_data1.select_dtypes(exclude=[object])
print(col_tp)

#information of columns
info = cars_data1.info()
print(info)

#unique data in a column using numpy
#print(np.unique(cars_data1['KM']))


#Two-way table - Joint probablity
xx = pd.crosstab(index = cars_data1['Automatic'],columns = cars_data1['FuelType'],normalize= True, dropna=True)
print(xx)

#Plot and Visualization of data
#plt.figure()
plt.scatter(cars_data1['Age'],cars_data1['Price'],color='blue')
#plt.scatter(cars_data1['Weight'],cars_data1['Price'],color='green')
plt.title('Scatter plot of Age vs Price')
plt.xlabel('Age')
plt.ylabel('Price')
plt.show()
