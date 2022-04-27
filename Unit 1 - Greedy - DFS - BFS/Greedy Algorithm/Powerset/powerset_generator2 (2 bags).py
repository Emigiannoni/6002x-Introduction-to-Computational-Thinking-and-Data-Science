# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 20:13:19 2022

@author: Emi
"""

# generate all combinations of N items

def powerSet(items):

    N = len(items)

    # enumerate the 2**N possible combinations

    for i in range(3**N):

        print('i = ' + str(i))
        
        combo1 = []
        combo2 = []

        for j in range(N):

            # test bit jth of integer i

            print('j = ' + str(j))

            if (i >> j) % 2 == 1:

                print('Item = ' + str(items[j]))               

                combo1.append(items[j])
        
        for k in range(N):

            # test bit jth of integer i

            print('k = ' + str(k))

            if (i >> k) % 2 != 1:

                print('Item = ' + str(items[k]))               

                combo2.append(items[k])

        yield (combo1, combo2)


list = [1,2,3]

x = powerSet(list)

powerset = []


for i in range(2**len(list)):

    powerset.append(x.__next__())
    
    print ('POWERSET AT ITERATION' + str(i) + str(powerset))
    