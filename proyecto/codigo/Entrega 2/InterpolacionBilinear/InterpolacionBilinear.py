import numpy as np 

def interpolacion(archivo,tamano):  #archivo=arreglo del csv #tamaño=como la quiero comprimir
    copia=np.copy(archivo) #Copia de la imagen de entrada
    filas,columnas=copia.shape #Como el numpy es una matriz retorna el número de filas y columnas
    
    filaSalida=int(filas*tamano)  #Si tenía 100 filas y puse 0.5, darán ya 50 filas
    columnaSalida=int(columnas*tamano) #Si tenía 200 columnas y puse 0.5 como parametro, darán ya 100 filas
 
    salida=np.zeros((filaSalida,columnaSalida)) #Imagen de salida, inicialmente llena de ceros
 
    for i in range(filaSalida): #O(n) donde n es el tamaño de la fila de la imagen de salida
        for j in range(columnaSalida): #O(m*n) donde m es el tamaño de la columna de la imagen de salida
            #Las coordenadas (i, j) en la imagen de salida corresponden al promedio de los cuatro puntos más cercanos (x1, y1) (x2, y2), (x3, y3), (x4, y4) en la imagen de entrada
            Xtemp=i/filaSalida*filas #Supongamos que estoy en (1,1) entonces xtemp=1/(50*100)
            Ytemp=j/columnaSalida*columnas #Supongamos que estoy en (1,1) entonces ytemp=1/(200*100)
 
            x1=int(Xtemp)
            y1=int(Ytemp)
 
            x2=x1
            y2=y1+1
 
            x3=x1+1
            y3=y1
 
            x4=x1+1
            y4=y1+1
 
            u=Xtemp-x1
            v=Ytemp-y1
 
            # Evitar el cruce
            if x4>=filas:
                x4=filas-1
                x2=x4
                x1=x4-1
                x3=x4-1
            if y4>=columnas:
                y4=columnas-1
                y3=y4
                y1=y4-1
                y2=y4-1
 
            # Interpolación
            salida[i,j]=(1-u)*(1-v)*int(copia[x1,y1])+(1-u)*v*int(copia[x2, y2])+u*(1-v)*int(copia[x3, y3])+u*v*int(copia[x4, y4])
    return salida


"""
COMPLEJIDAD DE INTERPOLACION BILINEAR
T(n,m)=C+C1*n+C2*(n*m)--->Ecuación de recurrencia
T(n,m) es O(C+C1*n+C2*(n*m))--->(Notación O)
O(C+C1*n+C2*(n*m))=O(C1*n+C2*(n*m))--->(Regla de la suma)
O(C1*n+C2*(n*m))=O(n+(n*m))--->(Regla del producto)
O(n+(n*m))=O(n*m)
T(n,m) es O(n*m)
En donde n es el número de filas y m el numero de columnas de la matriz de salida, es decir luego de la compresion o descompresion
"""

#Código tomado de: https://programmerclick.com/article/9212974781/