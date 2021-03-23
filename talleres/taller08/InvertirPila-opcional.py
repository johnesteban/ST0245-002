class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.insert(0,item)

     def extraer(self):
         return self.items.pop(0)

     def tamano(self):
         return len(self.items)
     
     def extraerFinal(self):
         return self.items.pop()
     
             

class __main__():
    lista=Pila()
    lista.incluir(3)
    lista.incluir(2)
    lista.incluir(1)
    i=0
    print("---LISTA NORMAL---")
    while(i<lista.tamano()):
        print(lista.extraer())
    
    lista.incluir(3)
    lista.incluir(2)
    lista.incluir(1)
    i=0
    print("---LISTA INVERTIDA---")
    while(i<lista.tamano()):
        print(lista.extraerFinal())
        
    