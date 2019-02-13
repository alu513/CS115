'''
Created on Sep 8, 2016

@author: Alex Lu
'''
from cs115 import map,reduce,range
import math

"""returns the inverse of x"""
def inverse(x):
    return 1/x 
print(inverse(3))


"""returns the sum of the inverse factorials of n terms and adds 1, represents the approximation of the value e"""
def add(x,y):
    return x+y
def e(n):
    return reduce(add,map(inverse,map(math.factorial,range(1,n+1)))) + 1
print (e(10))

"""returns the absolute value of the difference between the actual value of e and the approximation"""
def error(n):
    return abs(math.e - e(n))
print(error(3))


"""I pledge my honor that I have abided by the Stevens Honor System"""
"""Alexander Lu"""