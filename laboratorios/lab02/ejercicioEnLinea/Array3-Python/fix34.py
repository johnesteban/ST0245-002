# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 21:50:52 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def fix34(nums):
    for i in range(len(nums)): #C1*n
        for j in range(len(nums)): #C2*n*n
            if nums[i]==4 and nums[j]==3: #C3*n*n
                temporal=nums[j+1] #C4*n*n
                nums[j+1]=nums[i] #C5*n*n
                nums[i]=temporal #C6*n*n
    return nums #C7
"""
CÁLCULO DE COMPLEJIDAD
T(n)=C1*n+C2*n^2+C3*n^2+C4*n^2+C5*n^2+C6*n^2+C7
T(n)=C2*n+n^2(C2+C3+C4+C5+C6)+C--->Factor común y regla de la suma
T(n)=C2*n+C*n^2--->Regla de la suma
T(n)=n+n^2--->Regla del producto
T(n)=n^2--->(Se toma el valor máximo entre los dos, en este caso n^2 es mayor que n)
T(n) es O(n^2)--->Notación O
Donde n es la longitud del arreglo
"""