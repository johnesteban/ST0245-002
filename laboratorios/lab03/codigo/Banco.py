
class Cola():
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.append(item)

    def avanzar(self):
        return self.items.pop(0)

    def tamano(self):
        return len(self.items)
    
class Banco():
    def Simulacion(fila):
        cajero1="Cajero 1"
        cajero2="Cajero 2"
        StringFinal=""
        while fila.tamano()>1:
            StringFinal+=cajero1+" atendiendo a "+fila.avanzar()+"\n"
            StringFinal+=cajero2+" atendiendo a "+fila.avanzar()+"\n"
        if fila.tamano()>0:
            StringFinal+=cajero1+" atendiendo a "+fila.avanzar()    
        return StringFinal
            
class __main__():
    fila1=Cola()
    fila2=Cola()
    fila3=Cola()
    fila4=Cola()
    fila1.agregar("Esteban")
    fila1.agregar("Angela")
    fila1.agregar("Laura")
    fila1.agregar("John")
    fila1.agregar("Diego")
    fila2.agregar("Nicolas")
    fila2.agregar("Santiago")
    fila2.agregar("Gladys")
    fila3.agregar("Diana")
    fila4.agregar("Camilo")
    fila4.agregar("Alejandra")
    filaFinal=Cola() 
    while(fila1.tamano()>0 or fila2.tamano()>0 or fila3.tamano()>0 or fila4.tamano()>0):
        if fila1.tamano()>0:
            filaFinal.agregar(fila1.avanzar())
        if fila2.tamano()>0:
            filaFinal.agregar(fila2.avanzar())
        if fila3.tamano()>0:
            filaFinal.agregar(fila3.avanzar())
        if fila4.tamano()>0:
            filaFinal.agregar(fila4.avanzar())
    print("---SIMULACIÓN BANCO---")
    print(Banco.Simulacion(filaFinal))
    print("Simulación terminada")
    
    
