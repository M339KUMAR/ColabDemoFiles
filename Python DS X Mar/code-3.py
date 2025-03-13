#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:19:40 2025

@author: manavmishra
"""

import os
import pandas as pd
import numpy as np

os.chdir("/Users/manavmishra/Documents/Python for Data Science/Week-3")

cars_data = pd.read_csv("Toyota.csv", na_values=["??", "????"])
print(cars_data.head())

cars_data2 = cars_data.apply(lambda x: x.fillna(x.mean())\
                            if (x.dtype=='float') else\
                            x.fillna(x.value_counts().index[0]))
    
print(cars_data2.isnull().sum())
print("break")
print(cars_data2.dropna().sum())



if condition:
    print("")
    print("")
    #code-block
else:
    print("")

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1 if k%2==0 else -1 for k in list1]
print(list2)




