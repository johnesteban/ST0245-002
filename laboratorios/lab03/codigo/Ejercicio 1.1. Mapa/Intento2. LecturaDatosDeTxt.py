import csv
from collections import deque
aListVertices=deque()
aListArcos=deque()
archivo='medellin_colombia-grande.txt'
i=0
print("---ESTRUCTURA DE DATOS DE LOS VERTICES---")
with open(archivo, 'r') as f: #C1
    reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE) #C2
    for row in reader:  #C3*n
        aListVertices.append(row) #C4*n
        if(len(row)==0):#C5*n
            break #C6*n
    aListVertices.popleft() #C7
    aListVertices.pop() #C8
    print(aListVertices) #C9
    i=len(aListVertices)+2 #C10
    
print('\n')
print("---ESTRUCTURA DE DATOS DE LOS ARCOS---")
with open(archivo, 'r') as f:  #C11
    reader = csv.reader(f, delimiter=' ', quoting=csv.QUOTE_NONE) #C12
    for row in reader: #C13*m
        aListArcos.append(row)  #C14*m
    for i in range(i+1): #C15*n
        aListArcos.popleft() #C16*n
    print(aListArcos) #C17
    
#Para una parte del codigo nos basamos en lo siguiente: https://stackoverflow.com/questions/14885908/strip-white-spaces-from-csv-file

"""
CALCULO COMPLEJIDAD
T(n,m)=C1+C2+C3*n+C4*n+C5*n+C6*n+C7+C8+C9+C10+C11+C12+C13*m+C14*m+C15*n+C16*n+C17
T(n,m) es O(C1+C2+C3*n+C4*n+C5*n+C6*n+C7+C8+C9+C10+C11+C12+C13*m+C14*m+C15*n+C16*n+C17)--->(Notación O)
O(C1+C2+C3*n+C4*n+C5*n+C6*n+C7+C8+C9+C10+C11+C12+C13*m+C14*m+C15*n+C16*n+C17)=O((n*(C3+C4+C5+C6+C15+C16))+(m*(C13+C14))+C')--->(Regla de la suma y factor común)
O((n*(C3+C4+C5+C6+C15+C16))+(m*(C13+C14))+C')=O((n*C)+(m*C))--->(Regla de la suma)     
O((n*C)+(m*C))=O(n+m)---->(Regla del producto)
T(n,m) es O(n+m)
Donde n es la longitud de los vertices y m es la longitud de los arcos 
"""                                                                      
