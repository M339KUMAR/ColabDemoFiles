#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:46:28 2025

@author: manavmishra
"""

name = "Alice"     # A string
age = 30           # An integer
weight = 68.5312      # A float (weight in kilograms)
is_student = True  # A boolean (True or False)

print("Name:", name, "(Type:", type(name), ")")
print("Age:", age, "(Type:", type(age), ")")
print("Weight:", weight, "(Type:", type(weight), ")")
print("Is a student:", is_student, "(Type:", type(is_student), ")")

# String Manipulation
# Strings can be combined and modified.

greeting = "Hello"
message = greeting + ", " + name + "!"  # Concatenation
print(message)

# String formatting with f-strings
formatted_message = f"{name} is {age} years old and weighs {round(weight, 2)} kg."
print(formatted_message)
