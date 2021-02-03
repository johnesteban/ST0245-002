# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:30:49 2021

@author: LENOVO
"""
def Suma_grupo(start, nums, target):
    if start>=len(nums):
        if target ==0:
            return True
        else:
            return False
    return Suma_grupo(start+1, nums, target) or Suma_grupo(start+1, nums, target-nums[start])

print(Suma_grupo(0,[2, 4, 8],10))