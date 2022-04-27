# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:25:46 2022

@author: Emi Giannoni
"""
import random


def simulation(fullbucket):

    draws = []
    bucket = fullbucket[:]

    for i in range(3):
        ball = random.choice(bucket)
        bucket.remove(ball)
        draws.append(ball)

    return draws


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    fullbucket = []
    coincidences = 0

    for i in range(3):
        fullbucket.append('green')
        fullbucket.append('red')

    for i in range(numTrials):

        draws = simulation(fullbucket)

        if draws[0] == draws[1] and draws[1] == draws[2]:

            coincidences += 1

    return (float(coincidences) / numTrials)


print(noReplacementSimulation(1000000))