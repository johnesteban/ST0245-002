# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:42:51 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def tripleUp(nums):
    for i in range(len(nums)-2): #C1*(n-2)
        if nums[i]==nums[i] and nums[i+1]==nums[i]+1 and nums[i+2]==nums[i]+2:#C2*(n-2)
            return True #C3*(n-2)
    return False #C4
"""
CÁLCULO DE COMPLEJIDAD
T(n)=C1*(n-2)+C2*(n-2)+C3*(n-2)+C4
T(n)=(n-2)*(C1+C2+C3)+C--->Factor común y regla de la suma
T(n)=(n-2)*C--->Regla de la suma
T(n)=n-2--->Regla del producto
T(n)=n--->Regla de la suma
T(n) es O(n)--->Notación O
Donde n es la longitud del arreglo
"""