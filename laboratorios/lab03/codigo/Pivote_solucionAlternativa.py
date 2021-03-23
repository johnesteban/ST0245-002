def SumArray(arreglo):
    total=0
    for i in range(len(arreglo)):
        total+=arreglo[i]
    return total 

def Pivote(arreglo):
    ladoDerecho=0 #C
    ladoIzquierdo=0 #C
    minimo=SumArray(arreglo) #C*n
    for i in range(len(arreglo)):#n
        ladoIzquierdo=SumArray(arreglo[:i])#n*n
        ladoDerecho=SumArray(arreglo[i+1:])#n*n
        diferencia=abs(ladoIzquierdo-ladoDerecho)#c*n*n
        if(diferencia<minimo): #c*n*n
            minimo=diferencia #c*n*n
            posicionPivote=i #c*n*n
    return posicionPivote

"""
COMPLEJIDAD
    T(n)=(C*n)*(C*n)
    T(n) es O(C*n*C*n)
    O(C*n*C*n)=O(C(n*n))
    O(C(n*n))=O(n*n)
    O(n*n)=O(n^2)
"""
arreglo=[10,20,5,3,20,10]
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo)))
arreglo1= [10,2,4,8] 
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo1)))
arreglo2=[10,2,5,2,11]
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo2)))
arreglo3=[2,1,5,6,20,30,40,3,20,4,5]
print("La posición de pivote del arreglo es: "+str(Pivote(arreglo3)))