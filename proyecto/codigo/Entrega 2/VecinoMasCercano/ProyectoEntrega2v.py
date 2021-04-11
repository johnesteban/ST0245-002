import numpy as np
import os
from collections import deque
import pandas as pd
import VecinoMasCercano as vc

#Tengo una lista (linkedlist) de diccionaros, cada uno tiene dentro un nombre y un numpy (matriz multidimensional) con el csv
class estructura():
    def estructuraDatos(self,ganado):
        archivo=os.listdir(ganado) #Me da los nombres de los archivos que se encuentran en la carpeta en una lista
        arregloGanado=deque()   #Creo una lista
        for i in range(len(archivo)):
            diccionario={}
            diccionario["nombre"]=archivo[i]  #Le estoy diciendo que el nombre del diccionario va a ser igual al nombre del archivo
            direccion=ganado+"/"+archivo[i]
            data=pd.read_csv(direccion,header=None) #Lectura del archivo
            arreglo=np.asarray(data)  #Creo un numpy con todos los datos que se leen de la linea anterior
            diccionario["arreglo"]=arreglo #Ese arreglo lo guardo en "arreglo" del diccionario
            arregloGanado.append(diccionario)  #Agrego ese diccionario a la lista de arriba
        return arregloGanado #Retorno el arreglo de diccionarios
    
    def compresion(self,carpeta,arreglo):
        for i in range(len(arreglo)):  
            ImgCom=vc.vecino(arreglo[i]["arreglo"],0.5).astype(np.uint8) #Hago la interpolacion bilinear de cada archivo
            df=pd.DataFrame(np.array(ImgCom))
            df.to_csv(carpeta+"/"+arreglo[i]["nombre"],header=None) #Guardo la imagen en formato csv comprimida en la carpeta de imagenes comprimidas
            
    def descompresion(self,carpetaOrigen,carpetaDestino):
        for i in os.listdir(carpetaOrigen):
            im=pd.read_csv(carpetaOrigen+"/"+i)  #Abro la imagen 
            arreglo=vc.vecino(np.array(im),2).astype(np.uint8) #Se hace la interpolacion ampliando la imagen al tamaño original
            df=pd.DataFrame(np.array(arreglo))
            df.to_csv(carpetaDestino+"/"+i,header=None) #Lo guardo nuevamente en formato csv
            
class __main__():
    ganadoEnfermo="./archivosCSV/ganado enfermo CSVs" 
    ganadoSano="./archivosCSV/ganado sano CSVs"
    carpetaGanadoSanoCom="./archivosCSV/ImagenesSComprimidas"
    carpetaGanadoEnfermoCom="./archivosCSV/ImagenesEComprimidas"
    carpetaGanadoEnfermoDes="./archivosCSV/ImagenesEDescomprimidas"
    carpetaGanadoSanoDes="./archivosCSV/ImagenesSDescomprimidas"
    archivo=estructura()
    print("---MATRIZ GANADO ENFERMO---")
    arregloGanadoEnfermo=archivo.estructuraDatos(ganadoEnfermo)
    print(arregloGanadoEnfermo)
    print("\n")
    print("---MATRIZ GANADO SANO---")
    arregloGanadoSano=archivo.estructuraDatos(ganadoSano)
    print(arregloGanadoSano)
    print("---COMPRIMIENDO---")
    archivo.compresion(carpetaGanadoEnfermoCom,arregloGanadoEnfermo)
    archivo.compresion(carpetaGanadoSanoCom,arregloGanadoSano)
    print("Compresion terminada, revisa tus carpetas")
    print("---DESCOMPRIMIENDO---")
    archivo.descompresion(carpetaGanadoEnfermoCom,carpetaGanadoEnfermoDes)
    archivo.descompresion(carpetaGanadoSanoCom,carpetaGanadoSanoDes)
    print("Descompresion terminada, revisa tus carpetas")
    
        
    
        
    
   
    
   



