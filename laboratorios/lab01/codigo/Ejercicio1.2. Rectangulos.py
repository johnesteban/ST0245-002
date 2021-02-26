import matplotlib.pyplot as plt
from time import time


def formas(n):
    if n<=2:
        return n
    return formas(n-1)+formas(n-2)
    
##print(formas(3))

times=[]

def plot(times,n,lab):
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.plot(range(16,n),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()

for i in range(16,35):
    inicio=time()
    formas(i)
    fin=time()
    total=fin-inicio
    times.append(total)
plot(times,35,"Rectangulos")