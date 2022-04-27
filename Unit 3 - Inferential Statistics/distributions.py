# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:28:43 2022

@author: Emi Giannoni

Based on MIT 6.002x Lecture 7 - Inferencial Statistics on EDx

El objetivo de este codigo es verificar que la REGLA EMPIRICA para 1, 1.96 y 3
desvios estandar se cumple en distribucion normal.

Primero graficamos mediante sampleo aleatorio una curva de distribucion normal.
Luego definimos la funcion gaussian, que representa la ecuacion de distribucion
normal a integrar.
Por ultimo, integramos sobre curvas con medias y desvios aleatorios
para obtener una demostracion numerica numerica de la regla empirica.
"""
import random
import pylab
import scipy.integrate

''' *** NORMAL DITRIBUTION *** '''

dist = []
for i in range(100000):
    dist.append(random.gauss(0, 30))
pylab.hist(dist, 30)


def gaussian(x, mu, sigma):
    factor1 = (1.0 / (sigma * ((2 * pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x - mu)**2) / (2 * sigma**2))
    return factor1 * factor2


def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu =', mu, 'and sigma =', sigma)
        for numStd in (1, 1.96, 3):
            area = scipy.integrate.quad(gaussian, mu-numStd*sigma,
                                        mu+numStd*sigma, (mu, sigma))[0]
            print('Fraction within', numStd, 'std =', round(area, 4))
        print('\n')


checkEmpirical(10)
