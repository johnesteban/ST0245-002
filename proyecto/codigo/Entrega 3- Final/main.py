import numpy as np
import os
from collections import deque
import pandas as pd
import LZ77 as lz
import VecinoMasCercano_ as vc
import matplotlib.pyplot as plt
from time import time


class estructura():
    def estructuraDatos(self,ganado):
        archivo=os.listdir(ganado) 
        arregloGanado=deque()   
        for i in range(len(archivo)):
            diccionario={}
            direccion=ganado+"/"+archivo[i]
            data=pd.read_csv(direccion,header=None)
            arreglo=np.asarray(data,dtype=int)  
            diccionario["arreglo"]=arreglo 
            filas,columnas=np.shape(arreglo)
            diccionario["nombre"]=archivo[i]+"."+str(filas)+"."+str(columnas)
            arregloGanado.append(diccionario) 
            plt.imshow(arreglo)  
            plt.show()
        return arregloGanado 
    
    
    def compresion(self,carpeta,arreglo):
        for i in range(len(arreglo)): 
            filas,columnas=arreglo[i]["arreglo"].shape 
            compressor=lz.LZ77(30)
            ImgCom=vc.vecinoCompresion(arreglo[i]["arreglo"],0.25).astype(np.uint8)
            Concatenacion=np.concatenate(ImgCom)
            origin=list(Concatenacion)
            ImgCom2=compressor.compress(origin) 
            df=pd.DataFrame(np.array(ImgCom2))
            df.to_csv(carpeta+"/"+arreglo[i]["nombre"],index=False) 
            plt.imshow(ImgCom2)
            plt.show()
                    
    def descompresion(self,carpetaOrigen,carpetaDestino):
        for i in os.listdir(carpetaOrigen):
            im=pd.read_csv(carpetaOrigen+"/"+i)   
            decompressor=lz.LZ77(30) 
            arreglo=decompressor.decompress(im.values) 
            columnas=i.split(".")
            filasf=int(columnas[2])
            filasff=int(filasf/4)
            columnasf=int(columnas[3])
            columnasff=int(columnasf/4)
            descompresion=np.array(arreglo).reshape(filasff,columnasff)
            arreglov=vc.vecinoDescompresion(np.asarray(descompresion),4).astype(np.uint8) 
            df=pd.DataFrame(np.array(arreglov))
            df.to_csv(carpetaDestino+"/"+i,header=None,index=False) 
            plt.imshow(arreglov)
            plt.show()
            
            
class __main__():
    ganadoEnfermo="./archivosCSV/ImagenesEE" 
    carpetaGanadoEnfermoCom="./archivosCSV/ImagenesEComprimidas"
    carpetaGanadoEnfermoDes="./archivosCSV/ImagenesEDescomprimidas"
    archivo=estructura()
    print("---MATRIZ GANADO ENFERMO---")
    arregloGanadoEnfermo=archivo.estructuraDatos(ganadoEnfermo)
    print(arregloGanadoEnfermo)
    print("---COMPRIMIENDO---")
    inicio=time()
    archivo.compresion(carpetaGanadoEnfermoCom,arregloGanadoEnfermo)
    fin=time()
    print(fin-inicio)
    print("Compresion terminada, revisa tus carpetas")
    print("---DESCOMPRIMIENDO---")
    inicio1=time()
    archivo.descompresion(carpetaGanadoEnfermoCom,carpetaGanadoEnfermoDes)
    fin1=time()
    print(fin1-inicio1)
    print("Descompresión terminada, revisa tus carpetas")

    
        
    
        
    
   
    
   









