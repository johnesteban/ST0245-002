import numpy as np
from collections import deque
class GraphAm:

    def __init__(self, size):
        self.size = size
        self.matriz = np.zeros((size, size))
        
    def __str__(self):
        return f'{self.matriz}'

    def getWeight(self, source, destination):
        return self.matriz[source][destination] #O(1)

    def addArc(self,source,destination):
        self.matriz[source][destination]=1 
        self.matriz[destination][source]=1 #O(1)

    def getSuccessors(self, vertex):
        succs = [] #C
        for k, v in enumerate(self.matriz[vertex]): #C*V
            if v != 0: #C
                succs.append(k) #O(V)
        return succs #C ---->O(V^2)
     
    def isBicoloreable(self,origen):
        #-1 sin colorear, #1 se colorea con el primer color, #0 se colorea con el segundo color
        colorArr=[-1]*self.size   #C
        colorArr[origen]=1    #C
        queue=deque()           #C
        queue.append(origen) #C
        while queue:  #C*n
            u=queue.pop() #C
            if self.matriz[u][u] == 1: #C
                return "NOT BICOLOREABLE" #C
            for v in range(self.size): #C*m
                if self.matriz[u][v] == 1 and colorArr[v] == -1: #C
                    colorArr[v] = 1 - colorArr[u] #C
                    queue.append(v) #C
                elif self.matriz[u][v] == 1 and colorArr[v] == colorArr[u]: #C
                    return "NOT BICOLOREABLE" #C
        return "BICOLOREABLE" #C
    
    #Función basada de= https://www.geeksforgeeks.org/bipartite-graph/
    
"""
CÁLCULO DE COMPLEJIDAD
T(n,m)=C1+C2*m*n
T(n,m) es O(C1+C2*m*n)--->(Notación O)
O(C1+C2*m*n)=O(C2*m*n)--->(Regla de la suma)
O(C2*m*n)=O(m*n)--->Regla del producto
T(n,m) es O(m*n)
En donde m es el número de vértices en el grafo y n el número de aristas
"""
ga=GraphAm(3)
ga.addArc(0,1)
ga.addArc(1,2)
ga.addArc(2,0)
print(ga.isBicoloreable(2))
"""ga=GraphAm(3)
ga.addArc(0,1)
ga.addArc(1,2)
print(ga.isBicoloreable(0))
ga=GraphAm(9)
ga.addArc(0,1)
ga.addArc(0,2)
ga.addArc(0,3)
ga.addArc(0,4)
ga.addArc(0,5)
ga.addArc(0,6)
ga.addArc(0,7)
ga.addArc(0,8)
print(ga.isBicoloreable(0))"""

class __main__():
    entrada=input()
    cadena=""
    while entrada!="0":
        nodos=int(entrada)
        ga=GraphAm(nodos)
        entrada=int(input())
        for i in range(entrada):
            entrada=input()
            numero1,numero2=entrada.split()
            ga.addArc(int(numero1),int(numero2))
        cadena+=ga.isBicoloreable(0)+"\n"
        entrada=input()
    print("\n")
    print(cadena)

        
