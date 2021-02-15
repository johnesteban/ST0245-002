
import pandas as pd
import os
import numpy as np

ganadoEnfermo="./archivosCSV/ganado enfermo CSVs" 
ganadoSano="./archivosCSV/ganado sano CSVs"
listaEnfermos=os.listdir(ganadoEnfermo)
listaSanos=os.listdir(ganadoSano)#Me da los nombres de los archivos que se encuentran en la carpeta en una lista


for i in range(len(listaEnfermos)):
  direccion=ganadoEnfermo+"/"+listaEnfermos[i]
  data=pd.read_csv(direccion,header=None)
  arregloEnfermos=np.asarray(data)
  print(arregloEnfermos)

for i in range(len(listaSanos)):
   direccion2=ganadoSano+"/"+listaSanos[i]
   data2=pd.read_csv(direccion2,header=None)
   arregloSanos=np.asarray(data2)
   print(arregloSanos)

