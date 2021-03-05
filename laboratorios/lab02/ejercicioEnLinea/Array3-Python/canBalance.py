# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:40:01 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def canBalance(nums):
    SI= False
    sum1=0
    for i in range(0,len(nums)):
        sum1= sum1+nums[i]
        sum2= 0
        for j in range(i+1,len(nums)):
            sum2=sum2+nums[j]
        if(sum1== sum2):
            SI= True
            break
        else:
            SI= False
    return SI