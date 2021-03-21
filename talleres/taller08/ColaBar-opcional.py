class Cola():
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)
    
class __main__():
    lista=Cola()
    lista.agregar("Juan")
    lista.agregar("María")
    lista.agregar("Pedro")
    
    i=0
    while i<lista.tamano():
        print("Atendiendo a "+lista.avanzar())
    

