'''
Created on Sep 22, 2016

@author: Alex Lu
'''
'I pledge my honor that I have abided by the Stevens Honor System'
'Alexander Lu'



def change(amount,coins):
    'Returns the minimum number of coins required to make the amount'
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    if coins[0] == amount:
        return 1
    if coins[0] > amount:
        return change(amount, coins[1:])
    use_it = 1+ change(amount - coins[0], coins)
    lose_it = change(amount, coins[1:])
    
    return min(use_it, lose_it)

def change2(amount,coins):
    'Returns the minimum number of coins required to make the amount, another version'
    if amount == 0:
        return 0
    if coins == []:
        return float("inf")
    if(coins[0]>amount):
        return change(amount, coins[1:])
    return min(change(amount - coins[0], coins) + 1, change(amount, coins[1:]))




print(change(12, [2, 3, 4, 7]))