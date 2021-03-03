# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 07:54:47 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""
def Generar_arreglo(n):
    a=[] 
    for i in range (0,n):    
        for j in range(0,i): 
            a.append(j+1)    
    print(a)                 

    