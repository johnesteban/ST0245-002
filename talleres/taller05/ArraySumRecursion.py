import time
import random
import matplotlib.pyplot as plt
#Con recursion
def ArraySum(arr):
    if len(arr)==1: 
        return arr[0]  #C1=5
    else:
        return (ArraySum(arr[1:])+arr[0]) #T(n)=C2+T(n-1)  donde C2=4

print(ArraySum([2,4,5,10,15,0]))
    
"""
T(n)=C2+T(n-1)
"""
#%%
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




