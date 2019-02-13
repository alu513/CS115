'''
Created on Sep 15, 2016

@author: Alex Lu
'''
'''I pledge my honor that I have abided by the Stevens Honor System'''
'''Alexander Lu'''

from cs115 import reduce, map, range



def dot(L,K):
    '''Outputs the dot product of lists L and K'''
    if L == []:
        return 0.0
    elif K == []:
        return 0.0
    return L[0]*K[0] + dot(L[1:], K[1:])


def explode(S):
    '''take a string S as input and should return a list of the characters in that string'''
    if S == '':
        return []
    return [S[0]] + explode(S[1:])

def ind(e,L):
    '''returns the index of the element in the list/string. If the element is not in the list/string then it returns the length of the list/string instead'''
    if L == []:
        return 0
    if L == '':
        return 0
    if e == L[0]:
        return 0
    return 1 + ind(e, L[1:])


def removeAll(e,L):
    '''removes all the elements e in the list/string'''
    if L == []:
        return []
    if L == '':
        return ''
    if e == L[0]:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])
    
    
def myFilter(f,L):
    '''removes all the elements in the list that return false from the function given'''
    if L == []:
        return []
    if f(L[0]) == False:
        return  myFilter(f, L[1:])
    return [L[0]] + myFilter(f, L[1:])    

def deepReverse(L):
    '''reverses all the elements in the list including if the element itself is a list'''
    if L == []:
        return []
    if isinstance(L[-1], list):
        return [deepReverse(L[-1])] + deepReverse(L[:-1])
    return [L[-1]] + deepReverse(L[:-1])
   
