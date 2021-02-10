# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 03:10:09 2021

@author: Carlos Gustavo Vélez Manco
"""

def hanoi(topN, a = "Tower1", b = "Tower2", c = "Tower3"):
    if(topN == 1):
        print("move "+ str(topN)+ " to "+ c)
    else:
        hanoi(topN-1,a,c,b)
        print("move "+ str(topN)+ " to "+ c)
        hanoi(topN-1,b,a,c)
hanoi(3)

##Por qué con a,c,b y a,b,c NO se mueven en la torre 1?
## Con a,c,b y b,a,c FUNCIONA HPTA!!!