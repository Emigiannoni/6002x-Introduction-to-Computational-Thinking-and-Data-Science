# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:01:41 2022

@author: Emi
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    
    X = []
    
    if len(L) > 0:
    
        for element in L:
        
            X.append(len(element))
            
        mean = sum(X)/float(len(X))
        tot = 0.0
        for x in X:
            tot += (x - mean)**2
            std = (tot/len(X))**0.5
        
        return std

    else:
            
        return False

    
    

L = ['apples', 'oranges', 'kiwis', 'pineapples']

print(stdDevOfLengths(L))