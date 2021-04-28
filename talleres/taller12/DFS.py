import numpy as np

class GraphAm:

    def __init__(self, size):
        self.size = size
        self.matriz = np.zeros((size, size))
        
    def __str__(self):
        return f'{self.matriz}'

    def getWeight(self, source, destination):
        return self.matriz[source][destination] #O(1)

    def addArc(self, source, destination, weight):
        self.matriz[source][destination] = weight #O(1)

    def getSuccessors(self, vertex):
        succs = [] #C
        for k, v in enumerate(self.matriz[vertex]): #C*V
            if v != 0: #C
                succs.append(k) #O(V)
        return succs #C ---->O(V^2)a 
    
    def hayCaminoDFS(self,origen,destino):
        visitados=[False]*self.size
        return self.hayCaminoDFSAux(origen,destino,visitados)
    
    def hayCaminoDFSAux(self,origen,destino,visitados):
        visitados[origen]=True
        if origen==destino:
            return True
        for vertice in self.getSuccessors(origen):
          if (visitados[vertice]==False):
            if self.hayCaminoDFSAux(vertice,destino,visitados):
              return True
        return False


ga = GraphAm(8)
ga.addArc(2,4,15)
ga.addArc(1,5,30)
ga.addArc(3,1,7)
ga.addArc(3,7,5)
ga.addArc(7,5,20)
ga.addArc(5,6,100)
ga.addArc(6,5,40)
print(ga)
print(ga.getSuccessors(0))
print(ga.getSuccessors(1))
print(ga.getSuccessors(2))
print(ga.getSuccessors(3))
print(ga.getSuccessors(4))
print(ga.getSuccessors(5))
print(ga.getSuccessors(6))
print(ga.getSuccessors(7))
print(ga.getWeight(1,2))
print(ga.getWeight(0,0))
print(ga.hayCaminoDFS(0,2))
print(ga.hayCaminoDFS(3,5))
print(ga.hayCaminoDFS(1,6))
print(ga.hayCaminoDFS(1,7))
