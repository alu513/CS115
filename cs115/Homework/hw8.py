'''
Created on Oct 28, 2016

@author: Alex Lu
'''
'I pledge my Honor that I have abided by the Stevens Honor System'


def binaryToNum(s):
    'Returns the integer corresponding to the binary representation in s'
    def helper(s,n):
        if s=='':
            return 0
        return helper(s[:-1],n+1) + int(s[-1])*(2**n)
    return helper(s,0)

def numToBinary(n):
    'Returns the string with the binary representation of non-negative integer n.'
    if n==0:
        return ''
    return numToBinary(n//2) + str(n%2)


def TC(s,newS):
    'returns twos complement of a binary number'
    if s== '':
        a = binaryToNum(newS)
        b = (a+1)
        c = numToBinary(b)
        return c
    if s[0] == '1':
        newS += '0'
        return TC(s[1:],newS)
    if s[0] == '0':
        newS += '1'
        return TC(s[1:],newS)


def TcToNum(s):
    'given a binary number returns the twos complement number'
    if s[0] == '0':
        return binaryToNum(s)
    def helper(s,newS):
        if s == '':
            a = binaryToNum(newS)
            b = (-1)*(a+1)
            return b
        if s[0] == '1':
            newS += '0'
            return helper(s[1:],newS)
        if s[0] == '0':
            newS += '1'
            return helper(s[1:],newS)
    return helper(s, '')    



def NumToTc(n):
    'given a number returns the twos complement in binary'
    if n==0:
        return '00000000'
    if n>127 or n<-128:
        return 'Error'
    if n>0:
        a = numToBinary(n)
        b = 8-len(numToBinary(n))
        c = '0'*b
        return c + a
    if n<0:
        a = (-1)*n
        b = numToBinary(a)
        c = 8-len(numToBinary(a))
        d = '0'*c
        e = d+b
        f = TC(e,'')
        return f

        


        