import matplotlib.pyplot as plt
from time import time
import string
import random

def adn(chain1, chain2):
    if(len(chain1) == 0 or len(chain2)== 0):
        return 0  #C1=7    T(p)=C1
    if(chain1[len(chain1)-1] == chain2[len(chain2)-1]):
        return adn(chain1[:-1], chain2[:-1]) + 1 #C2=10 T(p)=T(p-2)+C2
    return max(adn(chain1[:-1], chain2), adn(chain1, chain2[:-1])) #C3=4  T(p)=T(p-1)+T(p-1)+C3
#p=n+m  
"""
CÁLCULO COMPLEJIDAD
T(p)=T(p-1)+T(p-1)+C3   donde p=n+m
T(p)=C3(2^(p)-1)+C1(2^(p-1))--->(Al resolverla en WolframAlpha)
T(p)   es O(C3(2^(p)-1)+C1(2^(p-1)))----->(Notación O)
O(C3(2^(p)-1)+C1(2^(p-1)))= O((2^(p)-1)+(2^(p-1)))---->Regla del producto
O((2^(p)-1)+(2^(p-1)))=O(2^p+2^p)---->(Regla de la suma)
O(2^p+2^p)=O(2(2^p))---->(Factor común)
O(2(2^p))=O(2^p)
Entonces T(p)=O(2^p)
donde p es la suma de la longitud de las cadenas

"""
times=[]
def plot(times,n,lab):
    
    plt.xlabel('Dimension del problema')
    plt.ylabel('Tiempo de complejidad')
    plt.plot(range(1,n),times,label=lab)
    plt.grid()
    plt.legend()
    plt.show()

string.ascii_letters='abcdefghijklmnopqrstuvwxyz'
final=1
for i in range(0,20):
    cadena1=""
    cadena2=""
    for j in range(1,final):
        cadena1+=random.choice(string.ascii_letters)
        cadena2+=random.choice(string.ascii_letters)
    print(cadena1) 
    print(cadena2)
    inicio=time()
    adn(cadena1,cadena2)
    fin=time()
    total=fin-inicio
    print(total)
    times.append(total)
    final=final+1
plot(times,20,"Subsecuencia Común")






        