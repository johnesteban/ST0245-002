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
                succs.append(v) #O(V)
        return succs #C ---->O(V^2)
    
    


ga = GraphAm(3)
ga.addArc(0, 1 , 15)
ga.addArc(0, 2 , 30)
ga.addArc(1, 1 , 7)
print(ga)
print(ga.getSuccessors(0))
print(ga.getSuccessors(1))
print(ga.getSuccessors(2))
print(ga.getWeight(1, 1))
print(ga.getWeight(0,0))

