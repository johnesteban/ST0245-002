# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 22:08:27 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def maxSpan(nums):
    temporal=0 #C1
    maximo=0 #C2
    for i in range(len(nums)): #C3*n
        for j in range(len(nums)): #C4*n*n
            if nums[i]==nums[j]: #C5*n*n
                temporal=j-i+1 #C6*n*n
                maximo=max(temporal,maximo) #C7*n*n
    return maximo #C8
"""
CÁLCULO DE COMPLEJIDAD
T(n)=C1+C2+C3*n+C4*n^2+C5*n^2+C6*n^2+C7*n^2+C8
T(n)=C3*n+n^2(C4+C5+C6+C7)+C--->Factor común y regla de la suma
T(n)=C3*n+C*n^2--->Regla de la suma
T(n)=n+n^2--->Regla del producto
T(n)=n^2--->(Se toma el valor máximo entre los dos, en este caso n^2 es mayor que n)
T(n) es O(n^2)--->Notación O
Donde n es la longitud del arreglo
"""