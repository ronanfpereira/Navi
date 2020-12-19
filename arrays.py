# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:27:15 2020

@author: Ronan Pereira

This program generates an array with a given range, print the position of the max value
and calculates the average value of the entire array
"""
import math

# Declaring the range and the vector
RANGE = 10
V = []

# Building the vector with respectives rules
for i in range (0,RANGE,1):
    if i%2 == 0:
        V.append(3**i+7*(math.factorial(i)))
    else:
        V.append(2**i+4*(math.log(i)))

# Finding and printing the position of the max value
A = max(V)
MEDIA = 0
for i in range (0,RANGE,1):
    if V[i] == A:
        print(f'A posicao do maior valor do vetor eh {i}')
        break

# Finding and printing the average value
for i in range (0,RANGE,1):
    MEDIA += V[i]

MEDIA /= len(V)

print(f'Media dos valores do vetor com arredondamento para duas casas decimais eh {round(MEDIA,2)}')
