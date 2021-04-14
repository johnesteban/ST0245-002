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
        
    def buscarBST(self, e):
        return self.buscarBSTAux(self.raiz, e)
    
    def buscarBSTAux(self, n, e):
        if n == None:
          return False
        if n.dato == e:
          return True
        if e < n.dato:
          return self.buscarBSTAux(n.izquierda,e)
        return self.buscarBSTAux(n.derecha,e)
    
    def insert(self,dato):
        if self.raiz is None:
            self.raiz=Nodo(dato)
        else:
            self.insertarAux(dato,self.raiz)
            
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
                
    
    def imprimir(self):
        self.__imprimir_aux(self.raiz)
        
    def __imprimir_aux(self, actual):
        if actual is not None:
            self.__imprimir_aux(actual.izquierda)
            print(actual.dato)
            self.__imprimir_aux(actual.derecha)
     
    def dibujar(self):
        return  f'digraph G {"{"} \n {self.dibujar_aux(self.raiz)} \n{"}"}'
    
    def dibujar_aux(self, actual):
        if actual is None:
            return 
        else:
            if actual.izquierda is not None and actual.derecha is not None:
                return f'{actual} -> {actual.izquierda} \n {actual} -> {actual.derecha}'
            if actual.left is not None:
                return f'{actual} -> {actual.izquierda}'
            if actual.right is not None:
                return f'{actual} -> {actual.derecha}'
            
    def borrar(self, data):
        self.__borrar_aux(data, self.raiz)

    def __borrar_aux(self, data, actual):
        if actual is None:
            return
        if data>actual.dato:
            actual.derecha=self.__borrar_aux(data,actual.derecha)
        elif data<actual.dato:
            actual.izquierda=self.__borrar_aux(data,actual.izquierda)
        else:
            if actual.izquierda is None:
                temp=actual.derecha
                return temp
            elif actual.derecha is None:
                temp=actual.izquierda
                return temp
            else:
                temp = self.__minValueNode(actual)
                actual.dato=temp.dato
                actual.derecha = self.__borrar_aux(temp.dato,data)
        return actual

    def __minValueNode(self, actual):
        temp=actual
        while(temp.izquierda is not None):
            temp=temp.izquierda 
        return temp
        
class archivo():
    archivo=open("personas-en-situacion-de-vulnerabilidad.csv",'r') 
    texto_en_string=archivo.read()
    archivo.close()
    separado_por_lineas=texto_en_string.split("\n") 
    arbolDatos=Arbol()
    print("----Arbol con los datos del csv---")
    for linea in separado_por_lineas:
        columnas = linea.split(",")
        apellido = columnas[0]
        nombre = columnas[1]
        telefono = columnas[3]
        if columnas[3]=="PhoneNumber":
            continue
        arbolDatos.insert(telefono)
    arbolDatos.imprimir()
    print("\n")
   
class __main__():
    print("---Arbol de prueba---")
    a=Arbol()
    a.insert(2)
    a.insert(3)
    a.insert(6)
    a.insert(1)
    a.insert(0)
    print(a.buscarBST(7))
    print(a.buscarBST(6))
    print(a.dibujar())
    a.borrar(6)
    a.borrar(0)
    a.imprimir()
        
            

