def SumArray(arreglo):
    total=0
    for i in range(len(arreglo)):
        total+=arreglo[i]
    return total 

def Pivote(arreglo):
    ladoDerecho=0 #C
    ladoIzquierdo=0 #C
    arregloNuevo=[0]*len(arreglo) #C
    suma=0 #C
    for i in range(len(arreglo)): #n
        arregloNuevo[i]=arreglo[i]+suma #n
        suma+=arreglo[i] #n
    minimo=SumArray(arreglo) #C*n
    for i in range(1,len(arreglo)):#n-1
        ladoIzquierdo=arregloNuevo[i-1]-arregloNuevo[0]#c*n
        ladoDerecho=arregloNuevo[len(arregloNuevo)-1]-arregloNuevo[i]#c*n
        diferencia=abs(ladoIzquierdo-ladoDerecho)#c*n
        if(diferencia<minimo): #c*n
            minimo=diferencia #c
            posicionPivote=i-1 #c
    return posicionPivote #c
    
"""
COMPLEJIDAD
    T(n)=C*n+C*n+C*n+C
    T(n) es O(C*n+C*n+C*n+C)
    O(C*n+C*n+C*n+C)=O(C*n+C*n+C*n)
    O(C*n+C*n+C*n)=O(c(n+n+n))
    O(c(n+n+n))=O(n+n+n)
    O(n+n+n)=O(3n)
    O(3n)=O(n)
"""
arreglo=[10,20,5,3,20,10]
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo)))
arreglo1= [10,2,4,8] 
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo1)))
arreglo2=[10,2,5,2,11]
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo2)))