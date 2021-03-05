# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:16:09 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def Sum28(nums):
    num= 0 #C1
    for i in range (0,len(nums)): #C2*n
        if(nums[i]== 2): #C3*n
            num= num+1 #C4*n
    if(num==4): #C5
        return True #C6
    return False
"""
CÁLCULO DE COMPLEJIDAD
T(n)=C1+C2*n+C3*n+C4*n+C5+C6+C7
T(n)=n*(C2+C3+C4)+C--->Factor común y regla de la suma
T(n)=n*C--->Regla de la suma
T(n)=n--->Regla del producto
T(n) es O(n)--->Notación O
Donde n es la longitud del arreglo
"""