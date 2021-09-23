#Importação de Bibliotecas

import math as math
import numpy as np
from numpy import load
from numpy import linalg as la
from numpy import asarray
import matplotlib.pyplot as plt
from PIL import Image   

#Localizar local em que o arquivo esta salvo/rodando

print()
print ("PROGRAMA SENDO EXECUTADO/ARMAZENADO EM:")
print()
import os
print(os.path.abspath("."))

#Cabeçalho

print()
print("Escola Politécnica da USP - MAP-3122 - Métodos Numéricos e Aplicações")
print("Nome: Vinicius Bueno de Moraes | NUSP: 10256432")
print()
print("Exercício 2 - Cálculo dos 12 Determinantes")

ns = [5, 10, 30]
o = 0
for t in ns:
    print()
    print("Para n = %s, se tem:" % ns[o])
    print()

    n = ns[o]

    #Composição da Matriz A

    a = np.zeros((((6*n)-2), (n*n)))
    i = 0
    j = 0
    d = 0
    while j < (n*n) and i < (n):
        if ((j-d) % n == 0):
            a[i][j] = 1 
        if ((j-d) % n != 0):
            a[i][j] = 0
        j = j + 1
        if j == n*n:
            i = i + 1
            d = d + 1
            j = 0
    t = 1 
    while j < (n*n) and i >= n and i < (n*2):
        if j < (n*t) and j >= (n*(t-1)):
            a[i][j] = 1 
        else:
            a[i][j] = 0
        j = j + 1
        if j == n*n:
            i = i + 1
            t = t + 1
            j = 0
    q = 1
    while j < (n*n) and i >= (2*n) and i < (4*n-1):
        if ((n*q) - (j+1)) % (n+1) == 0 and ((n*q) - (j+1)) >= 0 and ((n*q) - (j+1)) <= (n*n):
            a[i][j] = 1
        else:
            a[i][j] = 0
        j = j + 1
        if j == n*n:
            i = i + 1
            q = q + 1
            j = 0
    r = 1
    while j < (n*n) and i >= (4*n-1) and i < (6*n-2):
        if ((n*r) - (j+1)) % (n-1) == 0 and ((n*r) - (j+1)) > 0 and ((n*r) - (j+1)) < (n*n-1):
            a[i][j] = 1
        else:
            a[i][j] = 0
        j = j + 1
        if j == n*n:
            i = i + 1
            r = r + 1
            j = 0    

    #Cálculo dos 12 Determinantes

    b = a.transpose()
    deltas = [0, 0.001, 0.01, 0.1]
    identidade = np.eye(n*n)
    e = np.dot(b, a)
    u = 0

    for m in deltas:
        f = deltas[u]*identidade
        matriz = e + f
        det = np.linalg.det(matriz)

        print("O determinante para n = %s e Delta = %s é: %s" % (n, deltas[u], det))
        u = u + 1
        
    o = o + 1

print()
print("O programa foi executado com sucesso e os 12 Determinantes pertinentes ao exercício 2 calculados")
print()