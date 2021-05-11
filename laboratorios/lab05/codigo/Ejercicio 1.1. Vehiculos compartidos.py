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

    def addArc(self, source, destination, weight):
        self.matriz[source][destination] = weight #O(1)

    def getSuccessors(self, vertex):
        succs = [] #C
        for k, v in enumerate(self.matriz[vertex]): #C*V
            if v != 0: #C
                succs.append(k) #O(V)
        return succs #C ---->O(V^2)a 


class vehiculosCompartidos():
    def leerArchivo(self,numeroPuntos,p):
        nombreDelArchivo="dataset-ejemplo-U="+str(numeroPuntos)+"-p="+str(p)+".txt"
        g=GraphAm(numeroPuntos)
        archivo=open(nombreDelArchivo,'r',encoding="utf-8")
        textoString=archivo.read()
        archivo.close()
        Lineas=textoString.split("\n")
        #for i in range(209):
            
        for linea in Lineas:
            columnas=linea.split()
            #Descartar lineas fuera del dataset
            if len(columnas)<3:
                continue
            if columnas[0]=="Vertices.":
                continue
            if columnas[0]=="Costo":
                continue
            if int(float(columnas[1]))==-75:
                continue
            else:
                g.addArc(int(columnas[0])-1,int(columnas[1])-1,int(columnas[2])-1)
                #print(columnas[0]+columnas[1]+columnas[2])
        return g
                
            
    def asignarVehiculos(self,grafo,p):
        permutacionParaCadaSubconjunto=deque()
        dueno=2 #Empieza en 2 porque 1 es la empresa
        contador=1
        permutacion=deque()
        while dueno<=grafo.size:
            if contador==1:
                permutacion=deque()
                permutacion.append(dueno)
                dueno+=1
                contador+=1
            else:
                permutacion.append(dueno)
                dueno+=1
                contador+=1
                if(contador==6 or dueno==grafo.size):
                    contador=1
                    permutacionParaCadaSubconjunto.append(permutacion)      
        return permutacionParaCadaSubconjunto
    
    def guardarArchivo(self,permutacionParaCadaSubconjunto,numeroDePuntos,p):
        nombreArchivo="respuesta-ejemplo-U="+str(numeroDePuntos)+"-p="+str(p)+".txt"
        f=open(nombreArchivo,'w')
        for lista in permutacionParaCadaSubconjunto:
            for duenoVehiculo in lista:   
                f.write(str(duenoVehiculo)+" ")
            f.write("\n")
        f.close()
        

class __main__():
    v=vehiculosCompartidos()
    grafo=v.leerArchivo(205,1.3)
    permutacionParaCadaSubconjunto=v.asignarVehiculos(grafo,1.3)
    v.guardarArchivo(permutacionParaCadaSubconjunto,205,1.3)     

#Código basado del spoiler que se encuentra en Github: https://github.com/mauriciotoro/ST0245-Eafit/tree/master/laboratorios/lab05/spoiler/ejercicio-1.1/java