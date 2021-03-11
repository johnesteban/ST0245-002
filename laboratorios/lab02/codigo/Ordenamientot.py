from time import time
import matplotlib.pyplot as plt

def ordenar(arr):
   for i in range(1,len(arr)): #C1*n
       j=i#n*C2
       while (j > 0 and (arr[j-1]>arr[j])):#C3*n(n+1)/2
           temp=arr[j]#C4*n(n+1)/2
           arr[j]=arr[j-1]#C5*n(n+1)/2
           arr[j-1]=temp#C6*n(n+1)/2
           j=j-1#C7*n(n+1)/2
   return arr
"""
T(n)=C1*n+n*C2+C3*n(n+1)/2+C4*n(n+1)/2+C5*n(n+1)/2+C6*n(n+1)/2+C7*n(n+1)/2
T(n)=(n(n+1)/2*)(C3+C4+C5+C6)+C'-->Regla de las sumas y producto
T(n)=(n^2+n)*1/2*C'---->Se quita la suma interna
T(n)=n^2+n---->Se quitan los productos y la suma interna
T(n)=O(n^2)
"""
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
        arreglo[i]=n-i #Me da el arreglo de mayor a menor, por ende debe organizarlos todos
    return arreglo
    
for i in range(1000,12401,600):
    arreglo=generarArreglo(i)
    ini=time()
    ordenar(arreglo)
    fin=time()
    total=fin-ini
    print(total)
    times.append(total)
     
 
plot(times,12401,"InsertionSort")

