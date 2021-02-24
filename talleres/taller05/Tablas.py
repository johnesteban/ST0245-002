import time
import matplotlib.pyplot as plt
def tablas(n):
    for i in range(1,n+1): #C1*n
        print("-------TABLA DEL "+str(i)+"-------")
        for j in range(1,11):#C2*n*n
            ans=i*j #C3*n*n
            print(str(i)+"*"+str(j)+"="+str(ans)) #C4*n*n
            
tablas(9)
"""
T(n)=C1*n+C2*n^2+C3*n^2+C4*n^2
T(n)=n^2*(C1+C3+C4)+C'-->Regla de las sumas y producto
T(n)=n^2*C'---->Se quitan los productos y se simplifica la suma
T(n)=O(n^2)
"""

times=[]
def plot(times,n,lab):
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.title('Tiempos de complejidad para el algoritmo tablas de multiplicar con 20 tamaños del problema diferentes')
    plt.plot(range(1000000,n),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()
    
for i in range(1000000,1000020):
    ini=time.time()
    tablas(i)
    fin=time.time()
    print(fin-ini)
    times.append(fin-ini)


plot(times,1000020,"Tablas de multiplicar")
