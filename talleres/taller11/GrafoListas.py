class GraphAl:
    
    def __init__(self, size):
        self.size = size
        self.lista = [[] for i in range(size)]

    def __repr__(self):
        return '{}'.format(self.lista)

    def getWeight(self, source, destination):
        for d in self.lista[source]: #O(v)
            if d[source] == destination: #C
                return d[source] #C
            #Complejidad= O(v)

    def addArc(self, source, destination, weight):
        self.lista[source].append((destination, weight)) #O(V)

    def getSuccessors(self, vertice):
        succs = []
        for d in self.lista[vertice]: #C
            succs.append(d)  #O(V)
        return succs #C
    #Complejidad= O(V)

    


ga = GraphAl(3)
ga.addArc(0, 3, 10)
print(ga)
print(ga.getWeight(0, 3))
ga.addArc(0, 4, 7)
print(ga)
print(ga.getSuccessors(0))

