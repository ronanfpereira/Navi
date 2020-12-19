# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:20:31 2020

@author: Ronan Pereira

This program calculate the number of Multiples of three numbers in a range
"""

# The three multiples of interest
A = 37
B = 49
C = 2

# Range that will be used
RANGE = 5000000

# Counting the multiples
K = 1
while A * B * C * K <= RANGE:
    K = K + 1

print (K-1)
