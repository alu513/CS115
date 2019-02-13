'''
Created on Sep 29, 2016

@author: Alex Lu
'''
'I pledge my honor that I have abided by the Stevens Honor System'


def knapsack(capacity, items):
    'returns the maximum value as well as the list of items that you stole'
    if items == []:
        return [0,[]]
    if capacity == 0:
        return [0,[]]
    if items[0][0] > capacity:
        return knapsack(capacity, items[1:])
    useIt = knapsack(capacity - items[0][0], items[1:]) 
    loseIt = knapsack(capacity, items[1:])
    value = useIt[0] + items[0][1]
    itemList = [items[0]] + useIt[1]
    used = [value,itemList]
    if (used[0]>loseIt[0]):
        return used
    else:
        return loseIt
    
    
    

