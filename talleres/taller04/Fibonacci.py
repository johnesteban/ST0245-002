import matplotlib.pyplot as plt
from time import time


def Fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


for i in range(15,35):
    inicio=time()
    print(Fibonacci(i))
    fin=time()
    total=fin-inicio
    print(total)
 
 ##La gráfica en Excel de su complejidad es de tipo exponencial, igualmente
 ##a la anterior, consume muy poco tiempo para n pequeños, pero a medida
 ##que n se hace más grande, el algoritmo consume más tiempo.