#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 18:53:33 2025

@author: manavmishra
"""

l1 = [1,2,3,4,5]
f1 = list(map(lambda x: x**2, l1))
print(f1)


f2 = lambda x: x**3

l2 = [f2(k) for k in l1]
print(l2)

f3 = lambda x: [x*1 if i%2==0 else -1 for i in l1]


li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i)



# If-else

x = 10
y = 5

# # Method-1 (2 if blocks)
# if (x > y):
#     print("x is greater than y")
    
# if (x < y):
#     print("y is greater than x")
    
# if (x == y):
#     print("x is equal to y")
     
    
# # Method-2 (1 if-else block)
# if (x > y):
#     print("x is greater than y")
# elif (x < y):
#     print("y is greater than x")
# else:
#     print("x is equal to y")
  














