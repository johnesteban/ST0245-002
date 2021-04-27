class Arbol:
    def __init__(self,dato):
        self.dato=dato
        self.izquierda=None
        self.derecha=None
                
    def buscarAbuela(self,nombre):
        try:
            return nombre.izquierda.izquierda
        except:
            return "No se pudo encontrar la abuela materna de "+nombre.dato

class __main__():
    raiz=Arbol("Wilkenson") 
    raiz.izquierda=Arbol("Joaquina")
    raiz.derecha=Arbol("Sufranio")
    raiz.izquierda.izquierda=Arbol("Eustaquia")
    raiz.izquierda.derecha=Arbol("Eustaquio")
    raiz.derecha.izquierda=Arbol("Piolina")
    raiz.derecha.derecha=Arbol("Piolin")
    raiz.izquierda.izquierda.izquierda=Arbol("Florinda")
    raiz.izquierda.derecha.derecha=Arbol("Jovin")
    raiz.derecha.derecha.derecha=Arbol("Usnavy")
    raiz.derecha.izquierda.izquierda=Arbol("Wilberta")
    try:
        print("La abuela materna de "+raiz.dato+" es: "+raiz.buscarAbuela(raiz).dato)
    except:
        print(raiz.buscarAbuela(raiz))
    try:
        print("La abuela materna de "+raiz.derecha.dato+" es: "+raiz.buscarAbuela(raiz.derecha).dato)
    except:
        print(raiz.buscarAbuela(raiz.derecha))
    try:
        print("La abuela materna de "+ raiz.derecha.izquierda.izquierda+" es: "+raiz.buscarAbuela(raiz.derecha.izquierda.izquierda).dato)
    except:
        print(raiz.buscarAbuela(raiz.derecha.izquierda.izquierda))
    try:
        print("La abuela materna de "+raiz.izquierda.izquierda.izquierda+" es: "+raiz.buscarAbuela(raiz.izquierda.izquierda.izquierda).dato)
    except:
        print(raiz.buscarAbuela(raiz.izquierda.izquierda.izquierda))


#Codigo basado para la construcción del arbol de: https://unipython.com/arboles-en-python/#:~:text=En%20Ciencias%20de%20la%20computaci%C3%B3n,sub%2D%C3%A1rboles%20con%20nodos%20superiores.&text=Un%20%C3%A1rbol%20es%20un%20tipo,tiene%20soporte%20para%20%C3%A1rboles%20incorporado.