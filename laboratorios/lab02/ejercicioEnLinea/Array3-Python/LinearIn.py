# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:40:00 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def LinearIn(outer, inner):
    N= 0
    for i in range(0,len(inner)):
        for j in range(0,len(outer)):
            if(inner[i]== outer[j]):
                N=N+1
                break
    if(N==len(inner)):
        return True
    return False