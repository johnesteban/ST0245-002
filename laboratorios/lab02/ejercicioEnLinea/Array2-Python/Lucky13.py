# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:36:06 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def Lucky13(nums):
    for i in range(0,len(nums)):
        if(nums[i]== 1 or nums[i]==3):
            return False
    return True