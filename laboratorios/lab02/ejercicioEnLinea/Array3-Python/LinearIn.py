# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:40:00 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def LinearIn(outer, inner):
    N= 0 #C1
    for i in range(0,len(inner)): #C2*n
        for j in range(0,len(outer)): #C3*m*n
            if(inner[i]== outer[j]): #C4*m*n
                N=N+1 #C5*m*n
                break #C6*m*n
    if(N==len(inner)): #C7
        return True #C8
    return False #C9
"""
CÁLCULO DE COMPLEJIDAD
T(n,m)=C1+C2*n+C3*n*m+C4*m*n+C5*m*n+C7+C8+C9
T(n,m)=n*C2+(n*m)*(C3+C4+C5)+C--->Factor común y regla de la suma
T(n,m)=n*C2+(n*m)*C--->Regla de la suma
T(n,m)=n+(n*m)--->Regla del producto
T(n,m)=n*m--->(Se toma el valor mayor, en este caso es n*m, ya que ambos valores son positivos)
T(n,m)=m--->(Se puede omitir el valor de n, ya que m es mayor)
T(n,m) es O(m)--->Notación O
Donde n es la longitud del arreglo inner
Y donde m es la longitud del arreglo outer
"""
