# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:15:58 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""
def countEvens(nums):
    num= 0
    for i in range(0,len(nums)):
        if(nums[i]% 2== 0):
            num= num+1
        else:
            num= num
    return num