#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:36:20 2025

@author: manavmishra
"""

import os
import pandas as pd

os.chdir("/Users/manavmishra/Documents/Python for Data Science/Week-3")

cars_data = pd.read_csv("Toyota.csv", index_col=0, na_values=["??", "????"])

# Frequency table
df2 = pd.crosstab(index=cars_data["FuelType"], columns='count', dropna=True)
df3 = pd.crosstab(columns=cars_data["FuelType"], index='count', dropna=True)


# Two-way table
df2 = pd.crosstab(columns=cars_data["FuelType"], 
                  index=cars_data["Automatic"], 
                  dropna=True)
print(df2)

# Joint-probability
df1 = pd.crosstab(columns=cars_data["FuelType"], 
                  index=cars_data["Automatic"], 
                  dropna=True)
print(df1)
print("")

# Marginal-probability
df2 = pd.crosstab(columns=cars_data["FuelType"], 
                  index=cars_data["Automatic"], 
                  dropna=True,
                  normalize=True)
print(df2)
print("")

# Conditional-probability
df3 = pd.crosstab(columns=cars_data["FuelType"], 
                  index=cars_data["Automatic"], 
                  dropna=True,
                  normalize='columns',
                  margins=True)
print(df3)
print("")

# Conditional-probability
df4 = pd.crosstab(columns=cars_data["FuelType"], 
                  index=cars_data["Automatic"], 
                  dropna=True,
                  normalize='index',
                  margins=True)
print(df4)
print("")
