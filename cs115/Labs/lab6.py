'''
Created on _______________________
@author:   ALexander Lu
Pledge:    I pledge my Honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
#The right most bit for an odd number is 1 and for even it is 0
#The original number 
def isOdd(n):
    '''Returns whether or not the integer argument is odd. The base 2 version of 42 is 101010'''
    if n%2==0:
        return False
    return True

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    return numToBinary(n//2) + str(n%2)
    

def binaryToNum(s):
    def helper(s,n):
        '''Precondition: s is a string of 0s and 1s.
        Returns the integer corresponding to the binary representation in s.
        Note: the empty string represents 0.'''
        if s=='':
            return 0
        return helper(s[:-1],n+1) + int(s[-1])*(2**n)
    return helper(s,0)

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s=='11111111':
        return 8*'0'
    a=binaryToNum(s)
    b = 8-len(numToBinary(a+1))
    c = b*'0'
    return c + numToBinary(a+1)


def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n==-1:
        return ''
    print(s)
    return count(increment(s),n-1)


def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    return numToTernary(n//3) + str(n%3)

print(numToTernary(42))

def ternaryToNum(s):
    def helper(s,n):
        '''Precondition: s is a string of 0s, 1s, and 2s.
        Returns the integer corresponding to the ternary representation in s.
        Note: the empty string represents 0.'''
        if s=='':
            return 0
        return helper(s[:-1],n+1) + int(s[-1])*(3**n)
    return helper(s,0)

print(ternaryToNum('1120'))
