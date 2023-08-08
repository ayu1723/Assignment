# -*- coding: utf-8 -*-
"""Assignment 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fQsVSivcEPOf5A4ybjDWmkc55FMeGQmq
"""

'''
Q1. Create a python program to sort the given list of tuples based on integer value using a
lambda function.
[('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using
lambda and map functions.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and
lambda functions
Given String: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected output:('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.

Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
filter function.
[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
function.
['python', 'php', 'aba', 'radar', 'level']
'''

l = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

sorted_data = sorted(l,key=lambda x: x[1])

for player, runs in sorted_data:
    print(f'{player}: {runs}')

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x=lambda y:(y**2)
print(list(map(x,l)))

l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x=lambda y:str(y)
print(list(map(x,l)))

from functools import reduce

l=list(range(1,26))

def product(y,z):
  return y*z
t=reduce(product,l)
t

l=[2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
l1=[]
def divi(i):
  for i in l:
    if (i%2==0 and i%3==0):
      return i
    else:
      pass

t=list(filter(divi,l))
print(t)
#can you tell whats the problem in this?

l = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
l1 = []

def divi(i):
    return i % 2 == 0 and i % 3 == 0

t = list(filter(divi, l))
print(t)

s=['python', 'php', 'aba', 'radar', 'level']
ip=lambda x:x==x[::-1]
t=list(filter(ip,s))
t



