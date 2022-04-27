# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:42:55 2022

@author: Emi Giannoni, based on MIT 6.002x Lecture 8 - Monte Carlo Simulations

Code that simulates the Buffon - Laplace method to estimate the value of pi,
by randomly throwing needles to a circle into a square of size 2 x 2
(so the radio of the circle must be 1) and measuring the ratio of needles that
falls into the circle vs the squeare.
"""
import random
import numpy


def throwNeedles(numNeedles):
    '''
    Parameters
    ----------
    numNeedles : int - number of needles to be trow in each simulation

    Returns
    -------
    TYPE : float - estimation of pi based on a simulation of Buffon - Lapplace
    method

    '''
    inCircle = 0
    for needles in range(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        # x, y pair of cartesian coordinates that represent the position
        # where the needle falls
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
            # This calculate the distance from (x,y) to the origin using
            # Pitagora's theorem. If the distance is greater than 1,
            # the point must be outside the radio of the circle.
    return 4 * (inCircle/float(numNeedles))
    # Acording to Buffon - Laplace, the estimation of pi must be 4 times
    # the ratio of the needles in the circle (inCircle) vs the needles in
    # the square (since all needles falls into the square, this is equivalent
    # to the total number of needles)


def getEst(numNeedles, numTrials):
    '''
    Parameters
    ----------
    numNeedles : int - number of needles to be trow in each simulation
    numTrials : int - number of trials of Buffon - Lapplace simulation to be
    performed, using numNeedles needles in each simulation.

    Returns
    -------
    TYPE : tupple - containing the average estimation and the standard
    deviation of our samples after runing numTrials simulation using numNeedles
    needles.
    '''
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = numpy.std(estimates)
    # numpy.std calculates the standard deviation of a sample
    curEst = sum(estimates) / len(estimates)
    print('Est. = ' + str(curEst) + ', Std Dev = ' + str(round(sDev, 6))
          + ' , Needles = ' + str(numNeedles))
    return(curEst, sDev)


def estPi(precision, numTrials):
    '''
    Parameters
    ----------
    precision : float - deviation to evaluate the accuracy of our estimation.
    numTrials : int - number of trials of Buffon - Lapplace simulation to be
    performed in each call to getEst.

    Returns
    -------
    curEst : float - estimation of pi value.
    '''
    numNeedles = 1000
    sDev = precision
    while sDev >= precision / 1.96:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst


estPi(0.005, 100)

# Expected ouput:
# Est. = 3.1397200000000014, Std Dev = 0.053529 , Needles = 1000
# Est. = 3.1362200000000002, Std Dev = 0.037491 , Needles = 2000
# Est. = 3.1384199999999987, Std Dev = 0.021528 , Needles = 4000
# Est. = 3.1418850000000007, Std Dev = 0.018146 , Needles = 8000
# Est. = 3.1440399999999986, Std Dev = 0.013821 , Needles = 16000
# Est. = 3.1417825000000006, Std Dev = 0.010108 , Needles = 32000
# Est. = 3.1419050000000004, Std Dev = 0.006723 , Needles = 64000
# Est. = 3.1422684375000007, Std Dev = 0.005312 , Needles = 128000
# Est. = 3.141994843750002, Std Dev = 0.003549 , Needles = 256000
