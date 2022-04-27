# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 19:52:50 2022

@author: Emi Giannoni
"""

# generate all combinations of N items

def powerSet(items):

    N = len(items)

    # enumerate the 2**N possible combinations

    for i in range(3**N):

        combo = []

        for j in range(N):

            # test bit jth of integer i

            if (i >> j) % 2 == 1:

                combo.append(items[j])

        yield combo

list = [1,2,3]

x = powerSet(list)

powerset = []


for i in range(2**len(list)):

    powerset.append(x.__next__())
    
    print (i, powerset)
    
