# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 09:32:35 2021

@author: LENOVO
"""

class Fecha():

    
    def __init__(self,dia,mes, anyo):
         self.dia=dia
         self.mes=mes
         self.anyo=anyo
    
    def dia(self):
        return self.dia
    
    def mes(self):
        return self.mes
    
    def anyo(self):
        return self.anyo
    
    def transformar(self):
        fecha=str(self.anyo)+str(self.mes)+str(self.dia)
        numero=int(fecha)
        return numero
    
    def comparar(self,otra):
        if(self.transformar()<otra.transformar()):
            return -1
        
        elif(self.transformar()>otra.transformar()):
            return 1
        
        else:
            return 0
        
        
    def toString(self):
        return "La fecha es: "+str(self.dia)+"/"+str(self.mes)+"/"+str(self.anyo)
 
class main():
    Fecha1 = Fecha(1,3,2017)
    Fecha2 = Fecha(1,3,2015)
    if Fecha1.comparar(Fecha2)==-1:
        print("La fecha es menor a la ingresada")
    elif Fecha1.comparar(Fecha2)==1:
        print("La fecha es mayor a la ingresada")
    else:
        print("Las fecha son iguales ")
        
    print(Fecha1.toString())
    print(Fecha2.toString())