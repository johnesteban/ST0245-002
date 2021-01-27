# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:33:33 2021

@author: Carlos Vélez Manco, Esteban Castro Ramirez
"""
import math 
class Punto2D():
    """Representacion de punto en 2 dimenciones"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def radio_polar(self):
        return math.sqrt(self.x**2+self.y**2)
        
    def angulo_polar(self):
        return math.atan(self.y/self.x)

    def dist_euclidiana(self, other):
        return math.sqrt(((other.x-self.x)**2)+((other.y-self.y)**2))
    
