import pandas as pd
import csv
from io import open
archivo=open('C:/Users/LENOVO/Desktop/medellin_colombia-grande.txt','r') #r porque quiero leer el archivo
contenido=archivo.readlines() #almacena lo que tiene en cada linea en una lista
archivo.close()


dataVertices = pd.read_csv('Vertices.csv', sep=",", keep_default_na=True) #C1
print(dataVertices.head()) #Devuelve las primeras 5 filas                 #C2

dataArcos = pd.read_csv('Arcos.csv', sep=",", keep_default_na=True)      #C3        
print(dataArcos.head()) #Devuelve las primeras 5 filas                   #C4

diccArcos={}  #C5
for i in range(len(dataArcos)):  #C6*n
    diccArcos[(dataArcos.iloc[i]['ID'],dataArcos.iloc[i]['ID1'])] = dataArcos.iloc[i]['ID'],dataArcos.iloc[i]['ID1'] #C7*n
    #El iloc me devuelve los valores especificados que le mando por filas y columnas
    #iloc[filas,columnas]
    #En este caso le estoy diciendo que me devuelva la primera fila con la columna ID
    #Y la primera fila con la columna ID1 que es precisamente lo que necesitamos de arcos ya 
    #que podemos omitir los nombres

print("El diccionario de los arcos es:") #C8
print(diccArcos)  #C9

diccVert={}  #C10
for i in range(len(dataVertices)): #C11*m
    diccVert[(dataVertices.iloc[i]['ID'])]= dataVertices.iloc[i]['ID']  #C12*m

print("El diccionario de los vertices es:")  #C13
print(diccVert) #C14

"""
CÁLCULO DE COMPLEJIDAD
T(n,m)=C1+C2+C3+C4+C5+C6*n+C7*n+C8+C9+C10+C11*m+C12*m+C13+C14
T(n,m) es O(C1+C2+C3+C4+C5+C6*n+C7*n+C8+C9+C10+C11*m+C12*m+C13+C14)---->(Notación O)
O(C1+C2+C3+C4+C5+C6*n+C7*n+C8+C9+C10+C11*m+C12*m+C13+C14)=O((n*(C6+C7))+(m*(C11+C12))+C')--->(Factor común y regla de la suma)
O((n*(C6+C7))+(m*(C11+C12))+C')=O((n*C)+(m*C))--->(Regla de la suma)
O((n*C)+(m*C))=O(n+m)--->(Regla del producto)
T(n,m) es O(n+m)
en donde n es la cantidad de arcos
y m es la cantidad de vertices
"""                                


