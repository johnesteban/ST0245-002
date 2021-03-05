# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:16:02 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def bigDiff(nums):
    Diff= 0 #C1
    for i in range (0,len(nums)): #C2*n
        for j in range(0,len(nums)): #C3*n*n
            if(nums[i]<nums[j]): #C4*n*n
                N= nums[j]-nums[i] #C5*n*n
                if(N>Diff): #C6*n*n
                    Diff= N #C7*n*n
            else: #C8*n*n
                N= nums[i]-nums[j] #C9*n*n
                if(N>Diff): #C10*n*n
                    Diff= N #C11*n*n
    return Diff #C12
"""
CÁLCULO DE COMPLEJIDAD
T(n)=C1+C2*n+C3*n^2+C4*n^2+C5*n^2+C6*n^2+C7*n^2+C8*n^2+C9*n^2+C10*n^2+C11*n^2+C12
T(n)=C2*n+n^2(C3+C4+C5+C6+C7+C8+C9+C10+C11)+C--->Factor común y regla de la suma
T(n)=C2*n+C*n^2--->Regla de la suma
T(n)=n+n^2--->Regla del producto
T(n)=n^2--->(Se toma el valor máximo entre los dos, en este caso n^2 es mayor que n)
T(n) es O(n^2)--->Notación O
Donde n es la longitud del arreglo
"""