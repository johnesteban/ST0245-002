import matplotlib.pyplot as plt
from time import time
import string
import random

def adn(chain1, chain2):
    if(len(chain1) == 0 or len(chain2)== 0):
        return 0  #C1=7
    if(chain1[len(chain1)-1] == chain2[len(chain2)-1]):
        return adn(chain1[:-1], chain2[:-1]) + 1 #C2=10 T(n)=T(n-1)+C2
    return max(adn(chain1[:-1], chain2), adn(chain1, chain2[:-1])) #C3=4  T(n)=T(n-1)+T(n-1)+C3

"""
CÁLCULO COMPLEJIDAD
T(n)=T(n-1)+T(n-1)+C3
T(n)=C3(2^(n)-1)+C1(2^(n-1))
T(n) es O(C3(2^(n)-1)+C1(2^(n-1)))
O(C3(2^(n)-1)+C1(2^(n-1)))=O((2^(n)-1)+(2^(n-1)))
O((2^(n)-1)+(2^(n-1))=O(2^n+2^n)
O(2^n+2^n)=O(2(2^n))
O(2(2^n))=O(2^n)
  
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
for i in range(1,20):
    cadena1=""
    cadena2=""
    for j in range(1,final):
        cadena1+=random.choice(string.ascii_letters)
        cadena2+=random.choice(string.ascii_letters)
    print(cadena1) #Esto solo es para probar, luego lo debo de borrar
    print(cadena2)
    inicio=time()
    adn(cadena1,cadena2)
    fin=time()
    total=fin-inicio
    print(total) #Igual este
    times.append(total)
    final=final+1
plot(times,20,"Subsecuencia Común")

#%%
##tiempo que demora con dos cadenas de 300000 caracteres
string.ascii_letters='cgta'
cadenax=""
cadenay=""
for j in range(1,20):
    cadenax+=random.choice(string.ascii_letters)
    cadenay+=random.choice(string.ascii_letters)
print(cadenax)
print(cadenay)
inicio=time()
adn(cadenax,cadenay)
fin=time()
total=fin-inicio
print(total)




        