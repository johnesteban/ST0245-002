
import pandas as pd
import os

ganadoEnfermo=os.getcwd()+"\ganado enfermo CSVs" #Multicomputador sin tener que cambiar la ruta (?)
ganadoSano=os.getcwd()+"\ganado sano CSVs"
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


### No sabemos si funciona bien la ruta (ganadoEnfermos y ganadoSano) en multicomputador
### Al menos a mi me ejecuta, si tienen problemas cambia la ruta por la de tu pc por favor
    

