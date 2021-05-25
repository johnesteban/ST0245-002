import numpy as np 
import math

def vecinoCompresion(archivo,tamano):
    copia=np.copy(archivo) 
    filas,columnas=copia.shape 
    
    
    filaSalida=int(filas*tamano)  
    columnaSalida=int(columnas*tamano) 
 
    salida=np.zeros((filaSalida,columnaSalida)) 
    
    filaElegida=0
    columnaElegida=0
    suma=(tamano)**-1  
    for i in range(filaSalida): 
        for j in range(columnaSalida): 
            if columnaElegida>=columnas:  
                break  
            salida[i,j]=copia[filaElegida,columnaElegida] 
            columnaElegida+=int(suma) 
        filaElegida+=int(suma) 
        columnaElegida=0 
        if filaElegida>=filas:  
            break 
    return salida  

def vecinoDescompresion(archivo,tamano):  
    copia=np.copy(archivo) 
    filas,columnas=copia.shape 
    
    
    filaSalida=int(filas*tamano)  
    columnaSalida=int(columnas*tamano) 
 
    salida=np.zeros((filaSalida,columnaSalida)) 
    
    if tamano==1:  
        salida=copia
    else:   
        contadorFilas=0  
        for i in range(filaSalida): 
            contadorColumnas=0 
            for j in range(columnaSalida): 
                salida[i,j]=copia[int(math.floor(contadorFilas/tamano)),int(math.floor(contadorColumnas/tamano))]  
                contadorColumnas+=1 
                if j+1>=columnaSalida: 
                    break   
            contadorFilas+=1  
            if i+1>=filaSalida: 
                break  
    return salida  


