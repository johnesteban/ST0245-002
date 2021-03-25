def SumArray(arreglo):
    total=0 #C1
    for i in range(len(arreglo)): #C2*n
        total+=arreglo[i] #C3*n
    return total  #C4
#Complejidad del metodo sumArray=C1+C2*n+C3*n+C4=n*(C2+C3)+C'=n*C=n-->O(n)


def Pivote(arreglo):
    ladoDerecho=0 #C1
    ladoIzquierdo=0 #C2
    arregloNuevo=[0]*len(arreglo) #C3
    suma=0 #C4
    for i in range(len(arreglo)): #C5*n donde n es la longitud del arreglo
        arregloNuevo[i]=arreglo[i]+suma #C6*n
        suma+=arreglo[i] #C7*n
    minimo=SumArray(arreglo) #C8*n, la complejidad del metodo sumArray es O(n)
    for i in range(1,len(arreglo)):#C9*(n-1)
        ladoIzquierdo=arregloNuevo[i-1]#C10*(n-1)
        ladoDerecho=arregloNuevo[len(arregloNuevo)-1]-arregloNuevo[i]#C11*(n-1)
        diferencia=abs(ladoIzquierdo-ladoDerecho)#C12*(n-1)
        if(diferencia<minimo): #C13*(n-1)
            minimo=diferencia #C14*(n-1)
            posicionPivote=i #C15*(n-1)
    return posicionPivote #C16
    
"""
COMPLEJIDAD
    T(n)=C1+C2+C3+C4+C5*n+C6*n+C7*n+C8*n+C9*(n-1)+C10*(n-1)+C11*(n-1)+C12*(n-1)+C13*(n-1)+C14*(n-1)+C15*(n-1)+C16
    T(n) es O(C1+C2+C3+C4+C5*n+C6*n+C7*n+C8*n+C9*(n-1)+C10*(n-1)+C11*(n-1)+C12*(n-1)+C13*(n-1)+C14*(n-1)+C15*(n-1)+C16)--->(Notacion O)
    O(C1+C2+C3+C4+C5*n+C6*n+C7*n+C8*n+C9*(n-1)+C10*(n-1)+C11*(n-1)+C12*(n-1)+C13*(n-1)+C14*(n-1)+C15*(n-1)+C16)=O((n*(C5+C6+C7+C8))+((n-1)*(C9+C10+C11+C12+C13+C14+C15))+C')--->(Regla de la suma y factor común)
    O((n*(C5+C6+C7+C8))+((n-1)*(C9+C10+C11+C12+C13+C14+C15))+C')=O((n*C)+((n-1)*C))-->(Regla de la suma)  
    O((n*C)+((n-1)*C))=O(n+(n-1))--->(Regla del producto)                                                                                                         
    O(n+(n-1))=O(n)--->(Regla de la suma)
    T(n) es O(n)
    donde n es la longitud del vector dinámico
"""
arreglo=[10,20,5,3,20,10]
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo)))
arreglo1= [10,2,4,8] 
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo1)))
arreglo2=[10,2,5,2,11]
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo2)))
arreglo3=[2,1,5,6,20,30,40,3,20,4,5]
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo3)))
