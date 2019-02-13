'''
Created on Oct 25, 2016

@author: Alex Lu
'''
'I pledge my Honor that I have abided by the Stevens Honor System'

FullAdder = { ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }


def numToBaseB(N, B):
    'returns the string representing the number N in base B'
    if N == 0:
        return ''
    return numToBaseB(N//B, B) + str(N%B)



def baseBToNum(S, B):
    def helper(S,B,x):
        'returns the number S in the base B'
        if S=='':
            return 0
        return helper(S[:-1],B,x+1) + int(S[-1])*(B**x)
    return helper(S,B,0)


 
def baseToBase(B1,B2,SinB1):
    'converts a number (SinB1) in one base (B1) to a number in a different base (B2)'
    a = baseBToNum(SinB1, B1)
    b = numToBaseB(a, B2)
    return b

def add(S,T):
    'adds two binary numbers together by converting bases'
    a = baseBToNum(S, 2)
    b = baseBToNum(T, 2)
    c = a+b
    d = numToBaseB(c, 2)
    return d


def pad(S,T):
    'adds zeroes to the front of the binary number with less numbers'
    a=max(len(S), len(T))
    if len(S)>len(T):
        b = a-len(T)
        c = b*'0'
        return c+T
    if len(T)>len(S):
        b = a-len(S)
        c = b*'0'
        return c+S
    

def addB(S,T):
    def helper(S,T,C):
        'adds two binary numbers together without converting bases'
        if len(S)>len(T):
            T = pad(S,T)
        if len(T)>len(S):
            S = pad(S,T)
        if int(C)>0 and S=='':
            return '1'
        if S=='':
            return ''  
        sumBit, carryOut = FullAdder[(S[-1],T[-1],C)]
        return helper(S[:-1], T[:-1], carryOut) + sumBit
    return helper(S, T, '0')

print(addB("1011", "101"))



    


        