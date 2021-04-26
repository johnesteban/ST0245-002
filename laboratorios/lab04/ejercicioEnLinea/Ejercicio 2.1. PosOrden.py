
class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.izquierda=None
        self.derecha=None
        
    def __repr__(self):
        return f'{self.dato}'   

class Arbol:
    def __init__(self):
        self.raiz = None
        
    def insert(self,dato):
        if self.raiz is None:
            self.raiz=Nodo(dato)
        else:
            self.insertarAux(dato,self.raiz)
            
        #Complejidad de insert=O(n)
            
    def insertarAux(self,dato,actual):
        if actual.dato==dato:
            return 
        if dato>actual.dato:
            if actual.derecha is None:
                actual.derecha=Nodo(dato) 
            else:
                self.insertarAux(dato,actual.derecha)
        else:
            if actual.izquierda is None:
                actual.izquierda=Nodo(dato)
            else:
                self.insertarAux(dato,actual.izquierda)
        
    def imprimirPos(self):
        self.__imprimir_Posaux(self.raiz)
        
    def __imprimir_Posaux(self, actual):
        if actual is not None:
            self.__imprimir_Posaux(actual.izquierda)
            self.__imprimir_Posaux(actual.derecha)
            print(actual.dato)
    
    #Complejidad de imprimirPos=O(n)
            

class __main__():

    cantidadNodos=int(input("Ingrese la cantidad de nodos de su árbol binario de búsqueda: ")) #C1
    a=Arbol() #C2
    for i in range(cantidadNodos):#C3*n
        numero=int(input())   #C4*n
        a.insert(numero)    #C5*n*n
        
    print("\n")  #C6
    print("---RECORRIDO EN POS-ORDEN---") #C7 
    a.imprimirPos()  #C8*n
    
"""
CÁLCULO DE COMPLEJIDAD
T(n)=C1+C2+C3*n+C4*n+C5*n^2+C6+C7+C8*n---->Ecuación de recurrencia
T(n) es O(C1+C2+C3*n+C4*n+C5*n^2+C6+C7+C8*n)--->(Notación O)
O(C1+C2+C3*n+C4*n+C5*n^2+C6+C7+C8*n)=O((n*(C3+C4+C8))+(n^2(C8))+C')--->(Factor común y regla de la suma)
O((n*(C3+C4+C8))+(n^2(C8))+C')=O(n*C+n^2*C)---->(Regla de la suma)
O(n*C+n^2*C)=O(n+n^2)--->(Regla del producto)
O(n+n^2)=O(n^2)--->(Regla de la suma)
T(n) es O(n^2)
En donde n es la cantidad de nodos del árbol
"""
    
    