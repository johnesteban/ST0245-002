# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:16:09 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def Sum28(nums):
    num= 0
    for i in range (0,len(nums)):
        if(nums[i]== 2):
            num= num+1
    if(num==4):
        return True
    return False