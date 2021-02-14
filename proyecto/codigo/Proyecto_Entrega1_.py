
import pandas as pd
import os

ganadoEnfermo="./ganado enfermo CSVs" 
ganadoSano="./ganado sano CSVs"
print(ganadoEnfermo)
print(ganadoSano)
listaEnfermos=os.listdir(ganadoEnfermo)
listaSanos=os.listdir(ganadoSano)#Me da los nombres de los archivos que se encuentran en la carpeta en una lista


for i in range(len(listaEnfermos)):
  direccion=ganadoEnfermo+"/"+listaEnfermos[i]
  data=pd.read_csv(direccion,header=None)
  print(data)

for i in range(len(listaSanos)):
   direccion2=ganadoSano+"/"+listaSanos[i]
   data2=pd.read_csv(direccion2,header=None)
   print(data2)

