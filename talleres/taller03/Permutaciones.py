# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:11:49 2021

@author: LENOVO
"""

def permutations(base, cadena):
    if len(cadena) == 0:
        print (base)
    else:
        i = 0
        while i < len(cadena):
            permutations(base + cadena[i], cadena[0:i] + cadena[i+1:])
            i = i + 1

permutations("","abc")