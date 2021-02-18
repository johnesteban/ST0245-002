# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:05:48 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""
from time import time
import random
import matplotlib.pyplot as plt
import numpy as np
#Genera un arreglo de longitud n con números aleatorios y devuelve el máximo entre ellos
def maximo_arreglo_aleatorio(len):
    array = [0] * len
    M = 0
    for i in range(len):
        array[i] = random.randrange(0,100) 
        if array[i] > M: 
            M = array[i]
        else:
            M = M
    print(array)
    return M
print(maximo_arreglo_aleatorio(3))
#%%
## Grafica de los tiempos (en segundos) que tarda en realizar 20 operaciones.
## No se tienen en cuneta los valores de 0 segundos.

x=np.array(range(20))*1
y=np.array(range(20))*1.0
F = 0
for i in range(1000):
    inicio = time()
    maximo_arreglo_aleatorio(3)
    fin = time()
    tiempo_i = fin-inicio
    print(fin - inicio)
    y[i-F] = tiempo_i
    if(tiempo_i != 0):
        y[i-F] = tiempo_i ## ¿Cómo hacer que repita?
    else:
        F = F+1
        if(i-F >=20):
            break
    plt.plot(x,y)
    plt.show()