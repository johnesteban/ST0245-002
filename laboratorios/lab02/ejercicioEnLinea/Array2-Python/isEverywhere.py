# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:39:58 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def isEverywhere(nums, val):
    for i in range(0,len(nums)-1): #C1*(n-1)
        if(nums[i]== val or nums[i+1]== val): #C2*(n-1)
            return True #C3*(n-1)
    return False
"""
CÁLCULO DE COMPLEJIDAD
T(n)=C1*(n-1)+C2*(n-1)+C3*(n-1)+C4
T(n)=(n-1)*(C1+C2+C3)+C--->Factor común y regla de la suma
T(n)=(n-1)*C--->Regla de la suma
T(n)=n-1--->Regla del producto
T(n)=n--->Regla de la suma
T(n) es O(n)--->Notación O
Donde n es la longitud del arreglo
"""