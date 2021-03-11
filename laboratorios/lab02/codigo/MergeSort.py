from time import time
import matplotlib.pyplot as plt

def mergeSort(arr):
    if  len(arr)<2:  #C1
        return arr   #C2
    else:   #C3
        mitad=int(len(arr)/2)  #C4
        mitadDerecha=mergeSort(arr[:mitad]) #C5+T(n/2)
        mitadIzquierda=mergeSort(arr[mitad:]) #C6+T(n/2)
        return merge(mitadDerecha,mitadIzquierda)  #cn
    
    
def merge(arreglo1,arreglo2):
    arregloResultante=[] #C8
    i=0 #C9
    j=0  #C10
    while i<len(arreglo1) and j<len(arreglo2):  #T(n-1)+C "El peor caso para el while es que recorra todo el arreglo 1 y solo le quede faltando una posición del arreglo 2 o viceversa"
                                                 #"Y como n es la longitud del arreglo original, entonces i+j=n/2+(n/2-1)=n-1
            if(arreglo1[i]<arreglo2[j]):  #C+T(n-1)
                arregloResultante.append(arreglo1[i]) #C+T(n-1)*T(n) "Complejidad del metodo agregar"
                i=i+1 #C*T(n-1)
            else: #C
                arregloResultante.append(arreglo2[j]) 
                j=j+1
    arregloResultante+=arreglo1[i:] #C
    arregloResultante+=arreglo2[j:] #C
    return arregloResultante  #C

print(mergeSort([6,5,12,10,9,1]))
        

times=[]
def plot(times,n,lab):
    plt.xlabel('Dimension del problema (Longitud del arreglo)')
    plt.ylabel('Tiempo de complejidad (ms)')
    plt.title('Medicion de los tiempos de complejidad para 20 tamaños del problema diferentes')
    plt.plot(range(1000,n,600),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()

def generarArreglo(n):
    arreglo=[0]*n
    for i in range(n):
        arreglo[i]=n-i#Me da el arreglo de mayor a menor, por ende debe organizarlos todos
    return arreglo
    

for i in range(1000,12401,600):
    arreglo=generarArreglo(i)
    ini=time()
    mergeSort(arreglo)
    fin=time()
    total=fin-ini
    print(total)
    times.append(total)
     
 
plot(times,12401,"MergeSort")