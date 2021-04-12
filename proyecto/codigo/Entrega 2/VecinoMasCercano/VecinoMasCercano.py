import numpy as np 

def vecinoCompresion(archivo,tamano):  #imput_signal= arreglo del csv #zoom_multiples= como la quiero comprimir
    copia=np.copy(archivo) #Copia de la imagen de entrada
    filas,columnas=copia.shape #Como el numpy es una matriz retorna el número de filas y columnas
    
    
    filaSalida=int(filas*tamano)  #Si tenía 100 filas y puse 0.5, darán ya 50 filas
    columnaSalida=int(columnas*tamano) #Si tenía 200 columnas y puse 0.5 como parametro, darán ya 100 filas
 
    salida=np.zeros((filaSalida,columnaSalida)) #Imagen de salida, inicialmente llena de ceros

    filaElegida=0
    columnaElegida=0
    for i in range(filaSalida):
        for j in range(columnaSalida):
            if columnaElegida>=columnas:
                break
            salida[i,j]=copia[filaElegida,columnaElegida]
            columnaElegida+=2
        filaElegida+=2
        columnaElegida=0
        if filaElegida>=filas:
            break
    return salida 

def vecinoDescompresion(archivo,tamano):  #imput_signal= arreglo del csv #zoom_multiples= como la quiero comprimir
    copia=np.copy(archivo) #Copia de la imagen de entrada
    filas,columnas=copia.shape #Como el numpy es una matriz retorna el número de filas y columnas
    
    
    filaSalida=int(filas*tamano)  #Si tenía 100 filas y puse 0.5, darán ya 50 filas
    columnaSalida=int(columnas*tamano) #Si tenía 200 columnas y puse 0.5 como parametro, darán ya 100 filas
 
    salida=np.zeros((filaSalida,columnaSalida)) #Imagen de salida, inicialmente llena de ceros

    filaElegida=0
    columnaElegida=0
    i=0
    j=0
    while i<=filaSalida:
        while j<=columnaSalida:
            salida[i,j]=copia[filaElegida,columnaElegida]
            salida[i,j+1]=copia[filaElegida,columnaElegida]
            salida[i+1,j]=copia[filaElegida,columnaElegida]
            salida[i+1,j+1]=copia[filaElegida,columnaElegida]
            columnaElegida+=1
            j+=2
            if j+1>=columnaSalida:
                break
        filaElegida+=1
        columnaElegida=0
        j=0
        i+=2
        if i+1>=filaSalida:
            break
    return salida 
    
"""
Complejidad O(n*m), en donde n es la cantidad de filas de la matriz de salida y m la cantidad de columnas
"""
    