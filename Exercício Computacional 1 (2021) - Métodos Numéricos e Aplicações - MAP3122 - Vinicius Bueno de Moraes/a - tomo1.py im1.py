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
print("Exercício 1 - tomo1.py - im1")

#Importação dos Arrays e Imagens Disponibilizados
#Estes devem estar na mesma pasta em que o programa se encontra

p = np.load("p11.npy")
img = Image.open("im1.png")
data = asarray(img)

#Deduzindo valor de n do par (f*, p)

n = int((len(p))/2)
y = n*n
print()
print("O valor de n, deduzido do par (f*, p) é igual a: %s" % n)

#Composição da Matriz A

a = np.zeros(((2*n), (n*n)))
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

#Cálculo e Geração dos Comparáveis 

b = a.transpose()
deltas = [0.001, 0.01, 0.1]
identidade = np.eye(n*n)
e = np.dot(b, a)
o = 0

p_certo = np.dot(b, p)

for m in deltas:
    f = deltas[o]*identidade
    matriz = e + f

    #Algoritimo para Eliminação Gaussiana - Resolução do Sistema

    i = 0
    j = 0
    k = 0
    for k in range (0, y-1):
        for i in range (k+1, y):
            ratio = matriz[i, k]/matriz[k, k] 
            for j in range (k, y-1):
                matriz[i, j] -= ratio * matriz[k, j]
            p_certo[i] -= ratio * p_certo[k]

    x_gauss = np.zeros(y)

    x_gauss[y-1] = p_certo[y-1]/matriz[y-1, y-1]
    for i in range (y-2, -1, -1):
        soma_colunas = 0
        for j in range (i+1, y):
            soma_colunas += matriz[i, j] * x_gauss[j]
        x_gauss[i] = (p_certo[i] - soma_colunas)/matriz[i, i]
    
    #Ajustar Vetor em uma Matriz  
    
    gauss_final = np.zeros((n, n))
    z = math.sqrt(len(x_gauss))
    i = 0
    j = 0
    k = 0
    for t in x_gauss:
        gauss_final[i][j] = x_gauss[k]
        i = i + 1
        k = k + 1
        if i % z == 0 and z != 0:
            i = 0
            j = j + 1

    #Print de resultado

    print()
    print("A matriz referente a im1 original (f) se encontra abaixo: ")
    print()
    print(data)
    print()
    print("A matriz solução para delta = %s e n = %s se encontra abaixo:" % (deltas[o], n))
    print()
    print(gauss_final)
    
    plt.suptitle("Análise ref. ao Exercício 1 - tomo1.py - im1 | n = %s e Delta = %s " % (n, deltas[o]))
    plt.subplot(1, 2, 1)
    plt.imshow(gauss_final, cmap='gray')
    plt.title("f - Reconstrução")
    plt.subplot(1, 2, 2)
    plt.imshow(data, cmap='gray')
    plt.title("f* - Imagem Original")
    plt.show()
    o = o + 1 
print()
print("O programa foi executado com sucesso e as imagens exibidas")
print()