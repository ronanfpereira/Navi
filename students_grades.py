# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:47:10 2020

@author: Ronan Pereira

This program reads the names and grades of a number of students
and prints the highest grade and the respective students name
"""
# Declaring the number of students to be read and declaring the dictionary
N = 5
dc = {}

# Reading the students names and grades
for i in range(0,N,1):
    nome = input('Entre com o nome completo do aluno: ')
    nota = float(input('Entre com a nota do aluno: '))
    dc[nome] = nota

# Identifying the highest grade and the student name
MAIOR_NOTA = max(dc.values())
ALUNO_MAIOR_NOTA = max(dc,key=dc.get)

print(f' O aluno {ALUNO_MAIOR_NOTA} recebeu a maior nota de valor {MAIOR_NOTA}.')
