# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 20:27:38 2022

@author: Emi
"""
import random

def yieldAllCombos(items):

    N = len(items)

    # enumerate the 2**N possible combinations

    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)

        

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
    + str(self.weight) + '>'
                     
def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]        

def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]


items = buildItems()
combos = yieldAllCombos(items)

powerset = []


for i in range(2**len(items)):

    powerset.append(combos.__next__())
     
    print ('POWERSET AT ITERATION' + str(i) + str(powerset))