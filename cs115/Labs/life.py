#
# life.py - Game of Life lab
#
# Name: Alexander Lu
# Pledge: I pledge my Honor that I have abided by the Stevens Honor System
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width,height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
        
def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    """returns a 2d array of all live cells - with the value of 1 - 
    except for a one-cell-wide border of empty cells (with the value of 0) around the edge of the 2d array."""
    A = createBoard(w,h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = 1
    return A
    
def randomCells(w,h):
    """returns an array of randomly-assigned 1's and 0's except that the outer edge of the array is still completely empty (all 0's)"""
    A = createBoard(w,h)
    for row in range(1,h-1):
        for col in range(1,w-1):
            A[row][col] = random.choice( [0,1] )
    return A

def copy(A):
    """returns a deep copy of array A"""
    B = createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            B[row][col] = A[row][col]
    return B

def innerReverse(A):
    """returns a copy of array A except with an outer edge of 0's and with the 1's and 0's reversed"""
    B = copy(A)
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if(A[row][col]) == 1:
                B[row][col]=0
            if(A[row][col]) == 0:
                B[row][col]=1
    return B

def countNeighbors(row,col,A):
    """returns the number of live neighbors for a cell in the board A at a particular row and col"""
    num = 0
    if row!=0 and row!=len(A)-1 and col!=0 and col!=len(A[0])-1:
        if A[row][col+1] == 1:
            num+=1
        if A[row][col-1] == 1:
            num+=1
        if A[row+1][col] == 1:
            num+=1
        if A[row-1][col] == 1:
            num+=1
        if A[row+1][col+1] ==1:
            num+=1
        if A[row-1][col+1] ==1:
            num+=1
        if A[row-1][col-1] ==1:
            num+=1
        if A[row+1][col-1] ==1:
            num+=1
    return num

def next_life_generation(A):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0."""
    B = copy(A)
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if countNeighbors(row, col, A)<2:
                B[row][col]=0
            elif countNeighbors(row, col, A)>3:
                B[row][col]=0
            elif countNeighbors(row, col, A)==3 and A[row][col]==0:
                B[row][col]=1
            else:
                B[row][col]=A[row][col]
    return B
















