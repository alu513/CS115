'''
Created on _______________________
@author:   _______________________
Pledge:    I pledge my honor that I have abided by the Stevens Honor System. Alexander Lu

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    'returns the minimum number of coins as well as the coins themselves in a list'
    def helper(amount, coins, a, L):
        if amount == 0:
            return [a] + [L]
        if coins == []:
            return [float("inf")] + [L]
        if coins[0] > amount:
            return helper(amount, coins[1:], a, L)       
        return min(helper(amount - coins[0], coins, a + 1, L + [coins[0]]), helper(amount, coins[1:], a, L))

    return helper(amount, coins, 0,[])


print(giveChange(48, [1, 5, 10, 25, 50]))

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(scrabbleScores, Dictionary) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    def letterScore(letter, scorelist):
        'returns the score of one letter'
        if letter == scorelist[0][0]:
            return scorelist[0][1]
        return letterScore(letter, scorelist[1:])

    def wordScore(S, scorelist):
        'returns the score of a word'
        if S == '':
            return 0
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)
    
    def score(dct,lst,i):
        'returns the wordscore for all the words in the dictionary in a list'
        if i == len(dct):
            return []
        return lst + [[dct[i]] + [wordScore(dct[i], scrabbleScores)]] + score(dct, lst, i+1)
    return score(Dictionary, [], 0)
print(wordsWithScore(Dictionary, scrabbleScores))
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if L == []:
        return []
    if n==0:
        return []
    return [L[0]] + take(n-1,L[1:])

print(take(2,[5,4,3,2,1]))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0:
        return L
    return drop(n-1,L[1:])

print(drop(2,[5,4,3,2,1]))
