# -*- coding: utf-8 -*-
"""
Created on Sat Jan 01 15:16:04 2025

@author: Nilakshi
"""

import pandas as pd
import numpy as np

# Load data from CSV file into a DataFrame
df = pd.read_csv('example.csv')

# Calculate the average grade for each subject
average_grades = df.groupby('Subject')['Grade'].mean()

# Find the student with the highest average grade
#best_student = df.loc[df['Grade'].idxmax(), 'Name']

# Determine the number of students who failed in each subject
#failed_students = df[df['Grade'] < 60].groupby('Subject')['Name'].count()

# Concatenate student's name and subject to form a new column
#df['Student_Subject'] = df['Name'] + ' - ' + df['Subject']

# Convert DataFrame to NumPy array and perform element-wise arithmetic operations
grades_array = df['Grade'].to_numpy()
scaled_grades = (grades_array + 10) * 2

# Use string operations to extract the first name and last name of the student
#df['First Name'] = df['Name'].apply(lambda name: name.split()[0])
#df['Last Name'] = df['Name'].apply(lambda name: name.split()[-1])

print("Average Grades:")
print(average_grades)
#print("\nBest Student:", best_student)
print("\nNumber of Failed Students:")
#print(failed_students)
print("\nData with Student_Subject:")
print(df)
print("\nScaled Grades (NumPy Array):")
print(scaled_grades)
