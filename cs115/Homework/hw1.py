'''
Created on Sep 14, 2016

@author: Alex Lu
'''

from cs115 import reduce, map, range

"""returns the factorial of the positive number n"""
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(3))

"""adds together x and y"""
def add(x,y):
    return x+y

"""returns the average of a list of numbers"""
def mean(L):
    return (reduce(add,L))/len(L)

print(mean([1,2,3,4]))


"""returns the sum of a list of numbers"""
def sum(L):
    return reduce(add,L)

"""returns true if n divided by k has no remainder, returns false if there is a remainder"""
def divides(n):
    def div(k):
        return n%k==0
    return div



"""returns false if the number n is either less than 2 or if the number is not prime. returns true if the number is prime"""
def prime(n):
    if n<2:  return False
    if sum(map(divides(n),range(2,n**(1/2)))) > 0 : return False
    else: return True 

print(prime(24))


"""I pledge my honor that I have abided by the Stevens Honor System"""
"""Alexander Lu"""



 
    



    
