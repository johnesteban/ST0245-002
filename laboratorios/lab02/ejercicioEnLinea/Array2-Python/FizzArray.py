# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:41:11 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def fizzArray(n):
    nums=[0]*n #C1
    for i in range(len(nums)): #C2*n
        nums[i]=i #C3*n
    return nums #C4
"""
CÁLCULO DE COMPLEJIDAD
T(n)=C1+C2*n+C3*n+C4
T(n)=n*(C2+C3)+C--->Factor común y regla de la suma
T(n)=n*C--->Regla de la suma
T(n)=n--->Regla del producto
T(n) es O(n)--->Notación O
Donde n es la longitud del arreglo
"""