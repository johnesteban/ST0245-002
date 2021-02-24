import time
import random
import matplotlib.pyplot as plt
#Con ciclos
def ArraySum(arr):
    result=0;#C1
    for i in range(0,len(arr)):#C2*n
        result=arr[i]+result#C3*n
    print(result)#C4


    
"""
T(n)=C1+C2*n+C3*n+C4
T(n)=n*(C2+C3)+C'-->Regla de las sumas
T(n)=n*C'---->Se quitan los productos
T(n)=O(n)
"""
times=[]
def plot(times,n,lab):
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.plot(range(1000000,n,100000),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()
    
def getTime(meth,a,b):
     ini = ((time.time()))
     meth(a)
     fin = ((time.time()))
     print(str(fin-ini))
     times.append(fin-ini)
     
n=1000000
while n<=3000001:
 arr=[0]*n
 for x in range(n):
    arr[x]=random.randint(1,10000000)
 getTime(ArraySum,arr,n)
 n=n+100000
 
plot(times,3000001,"ArraySum")


