# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:03:13 2021

@author: LENOVO
"""
class Mcd():
    def  gcd_euclid ( p , q ):
        if(p%q==0):
            return q
        else:
            return Mcd.gcd_euclid(q,p%q)

class Principal():
    print (Mcd.gcd_euclid ( 60 , 48 ))
    print (Mcd.gcd_euclid ( 20,16 ))
    print (Mcd.gcd_euclid(1000,10))