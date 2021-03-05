# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:16:02 2021

@author: Carlos Gustavo Vélez Manco, John Esteban Castro Ramírez
"""

def bigDiff(nums):
    Diff= 0
    for i in range (0,len(nums)):
        for j in range(0,len(nums)):
            if(nums[i]<nums[j]):
                N= nums[j]-nums[i]
                if(N>Diff):
                    Diff= N
            else:
                N= nums[i]-nums[j]
                if(N>Diff):
                    Diff= N
    return Diff
