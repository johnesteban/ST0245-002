# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 08:06:05 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def Invertir_arreglo(array):
    n = len(array) #C1
    for i in range(0,int(n/2)): #T(n)= T(n/2)*C2
        temp = array[i]         #C3*T(n/2)
        array[i] = array[n-i]   #C4*T(n/2)
        array[n-i] = temp       #C5*T(n/2)
    return array
a=[]
n=int(input("Ingrese un número entero "))
while n!=-1:
    a.append(n)
    n=int(input("Ingrese un número entero "))

print(a)
print(Invertir_arreglo(a))

#Complejidad:
    #T(n)= C1 + (C2+C3+C4+C5)*T(n/2)
    #T(n)=T(n/2)+ C ... Regla de la suma
    #T(n)= C*log(n)/Log(2) + C1 ... Solución de Wolfram Alpha
    #T(n)= C*log2(n) + C1 ... Cambio de base
    #T(n) es O(C*log2(n) + C1) ... Notación O
    #O(C*log2(n) + C1)= O(C*log2(n)) ... Regla de la suma
    #O(C*log2(n)) = O(log2(n)) ... Regla del producto
    #O(log2(n)) = O(log(n))