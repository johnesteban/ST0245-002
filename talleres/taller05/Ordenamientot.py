import time
import random
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
print(ordenar([10,9,8,7,6,2,3,1,0,5,4]))
#%%
"""
T(n)=C1*n+n*C2+C3*n(n+1)/2+C4*n(n+1)/2+C5*n(n+1)/2+C6*n(n+1)/2+C7*n(n+1)/2
T(n)=(n(n+1)/2*)(C3+C4+C5+C6)+C'-->Regla de las sumas y producto
T(n)=(n^2+n)*1/2*C'---->Se quita la suma interna
T(n)=n^2+n---->Se quitan los productos y la suma interna
T(n)=O(n^2)
"""
times=[]
def plot(times,n,lab):
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.plot(range(2000,n,100),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()
    
def getTime(meth,a,b):
     ini = ((time.time()))
     meth(a)
     fin = ((time.time()))
     print(str(fin-ini))
     times.append(fin-ini)
     
n=2000
while n<=4001:
 arr=[0]*n
 for x in range(n):
    arr[x]=random.randint(1,10000000)
 getTime(ordenar,arr,n)
 n=n+100
 
plot(times,4001,"Ordenar")

