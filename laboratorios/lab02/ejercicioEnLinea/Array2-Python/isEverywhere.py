# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:39:58 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def isEverywhere(nums, val):
    SI= True
    for i in range(0,len(nums)-1):
        if(nums[i]== val or nums[i+1]== val):
            SI= True
        else:
            SI= False
            break;
    return SI