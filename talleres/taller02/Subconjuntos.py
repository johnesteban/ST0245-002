# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 06:52:55 2021

@author: LENOVO
"""

def subconjuntos(s):
    subconjuntosBase("", s)

def subconjuntosBase(base, t):
    if len(t) == 0:
        print(base)
    else:
       x = t[1:]
       z= t[:1]
       subconjuntosBase(base+z,x)
       subconjuntosBase(base,x)

print(subconjuntos("Santi"))


