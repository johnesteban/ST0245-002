# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:36:06 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def Lucky13(nums):
    for i in range(0,len(nums)): #C1*n
        if(nums[i]== 1 or nums[i]==3): #C2*n
            return False #C3*n
    return True #C4
"""
CÁLCULO DE COMPLEJIDAD
T(n)=C1*n+C2*n+C3*n+C4
T(n)=n*(C1+C2+C3)+C--->Factor común y regla de la suma
T(n)=n*C--->Regla de la suma
T(n)=n--->Regla del producto
T(n) es O(n)--->Notación O
Donde n es la longitud del arreglo
"""