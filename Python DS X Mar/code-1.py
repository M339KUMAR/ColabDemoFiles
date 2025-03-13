#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 18:09:49 2025

@author: manavmishra
"""

import numpy as np
import pandas as pd

data = pd.read_csv('/Users/manavmishra/Documents/Python for Data Science/Week-3/Iris_data_sample.csv')

df2 = data.iloc[:, 1:]
print(df2.info())

df3 = data.select_dtypes(exclude=[object, int])
print(df3.head())
print(data.head())

print(df3.columns)
print(data.columns)

n1 = np.array([1,2,3,4,5,6,7,8,9])
n2 = n1[:-1] + n1[1:]
print(n2)
