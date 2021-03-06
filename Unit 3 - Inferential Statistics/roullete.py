# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 12:09:35 2022

@author: Emi Giannoni

Based on MIT 6.002x Lecture 7 - Inferencial Statistics on EDx
"""

# En una "Ruleta Justa" hay un 50% de probabilidades de que salga rojo y
# 50% de que salga negro, no contemplando la posibilidad de 0 ni 00.
# Mas abajo encontramos las clases para ruleta europea (incluye 0) y
# ruleta americana (incluye 0 y 00), cambiando las probabilidades

import random


class FairRoulette(object):

    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0
        self.pocketOdds = len(self.pockets) - 1.0
        # Apostar al pocket devuelve mayor redituo

    def spin(self):
        self.ball = random.choice(self.pockets)

    def isBlack(self):
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10) or
                (self.ball > 18 and self.ball <= 28)):
            return self.ball % 2 == 0
        else:
            return self.ball % 2 == 1

    def isRed(self):
        return type(self.ball) == int and not self.isBlack()

    def betBlack(self, amt):
        if self.isBlack():
            return amt * self.blackOdds
        else:
            return -amt

    def betRed(self, amt):
        if self.isRed():
            return amt * self.redOdds
        else:
            return -amt

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt * self.pocketOdds
        else:
            return -amt

    def __str__(self):
        return 'Fair Roulette'


def playRoulette(game, numSpins, toPrint=True):
    luckyNumber = '2'
    bet = 1  # amt en la clase FairRoulette
    totRed, totBlack, totPocket = 0.0, 0.0, 0.0
    for i in range(numSpins):
        game.spin()
        totRed += game.betRed(bet)
        totBlack += game.betBlack(bet)
        totPocket += game.betPocket(luckyNumber, bet)
        # acumula las ganancias de apostar rojo, negro o al 'luckyNumber' 2.
        # como bet = amt = 1, podemos asumir que contar ganancia es lo mismo
        # que contar aciertos / frecuencia.
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting Red = ', str(100*totRed/numSpins) + '%')
        print('Expected return betting Black = ', str(100*totBlack/numSpins) + '%')
        print('Expected return betting ', luckyNumber, ' = ', str(100*totPocket/numSpins) + '%')
    return (totRed/numSpins, totBlack/numSpins, totPocket/numSpins)

# numSpins = 1000000
# game = FairRoulette()
# playRoulette(game, numSpins)


# 1000000 spins of Fair Roulette
# Expected return betting Red =  0.033%
# Expected return betting Black =  -0.033%
# Expected return betting  2  =  -0.6976%
# Los resultados deben tender a 0, debido a que es una ruleta justa
# y explicado por la ley de los numeros grandes (Bernoulli)


class EuRoulette(FairRoulette):

    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')

    def __str__(self):
        return 'European Roulette'


class AmRoulette(EuRoulette):

    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')

    def __str__(self):
        return 'American Roulette'


def findPocketReturn(game, numTrials, trialSize, toPrint):
    pocketReturns = []
    for t in range(numTrials):
        trialVals = playRoulette(game, trialSize, toPrint)
        pocketReturns.append(trialVals[2])
    return pocketReturns


''' *** EXPERIMENT RUNING *** '''

# random.seed(0)
# numTrials = 20
# resultDict = {}
# games = (FairRoulette, EuRoulette, AmRoulette)
# for numSpins in (100, 1000, 10000, 100000):
#     print('\nSimulate betting a pocket for ', numTrials, ' trials of ', numSpins, ' spins each.')
#     for G in games:
#         pocketreturns = findPocketReturn(G(), numTrials, numSpins, False)
#         print('Expected return for ', G(), '=', str(100 * sum(pocketreturns)/float(len(pocketreturns))) + '%')       


def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return (mean, std)


numTrials = 20
resultDict = {}
games = (FairRoulette, EuRoulette, AmRoulette)
for G in games:
    resultDict[G().__str__()] = []
for numSpins in (100, 1000, 10000, 100000):
    print('\nSimulate betting a pocket for ', numTrials, ' trials of ',
          numSpins, ' spins each.')
    for G in games:
        pocketreturns = findPocketReturn(G(), numTrials, numSpins, False)
        mean, std = getMeanAndStd(pocketreturns)
        resultDict[G().__str__()].append((numSpins, 100*mean, 100*std))
        print('Expected return for ', G(), '=',
              str(100 * sum(pocketreturns)/float(len(pocketreturns))) + '%',
              '+/-' + str(round(100*1.96 * std, 3)) + '% with 95% confidence')
