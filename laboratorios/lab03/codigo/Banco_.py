
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
    def Simulacion(fila1, fila2, fila3, fila4): 
        filaFinal=Cola() #C1
        while(fila1.tamano()>0 or fila2.tamano()>0 or fila3.tamano()>0 or fila4.tamano()>0): #C2*n donde n es la fila con mayor numero de personas
            if fila1.tamano()>0: #C3*n
                filaFinal.agregar(fila1.avanzar()) #C4*n
            if fila2.tamano()>0: #C5*n
                filaFinal.agregar(fila2.avanzar()) #C6*n
            if fila3.tamano()>0: #C7*n
                filaFinal.agregar(fila3.avanzar())#C8*n
            if fila4.tamano()>0: #C9*n
                filaFinal.agregar(fila4.avanzar()) #C10*n
        cajero1="Cajero 1" #C11
        cajero2="Cajero 2" #C12
        StringFinal="" #C13
        while filaFinal.tamano()>1: #C14*(m-1) donde m es el total de personas en el banco
            StringFinal+=cajero1+" atendiendo a "+filaFinal.avanzar()+"\n" #C15*(m-1)
            StringFinal+=cajero2+" atendiendo a "+filaFinal.avanzar()+"\n" #C16*(m-1)
        if filaFinal.tamano()>0: #C17
            StringFinal+=cajero1+" atendiendo a "+filaFinal.avanzar() #C18 
        return StringFinal #C19
            
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
    print("---SIMULACIÓN BANCO---")
    print(Banco.Simulacion(fila1,fila2,fila3,fila4))
    print("Simulación terminada")

"""
CALCULO DE COMPLEJIDAD
T(n,m)=C1+C2*n+C3*n+C4*n+C5*n+C6*n+C7*n+C8*n+C9*n+C10*n+C11+C12+C13+C14*(m-1)+C15*(m-1)+C16*(m-1)+C17+C18+C19
T(n,m) es O(C1+C2*n+C3*n+C4*n+C5*n+C6*n+C7*n+C8*n+C9*n+C10*n+C11+C12+C13+C14*(m-1)+C15*(m-1)+C16*(m-1)+C17+C18+C19)--->(Notacion O)
O(C1+C2*n+C3*n+C4*n+C5*n+C6*n+C7*n+C8*n+C9*n+C10*n+C11+C12+C13+C14*(m-1)+C15*(m-1)+C16*(m-1)+C17+C18+C19)=O((n*(C2+C3+C4+C5+C6+C7+C8+C9+C10))+((m-1)*(C14+C15+C16))+C')---->(Regla de la suma y factor comun)
O((n*(C2+C3+C4+C5+C6+C7+C8+C9+C10))+((m-1)*(C14+C15+C16))+C')=O((n*C')+(m-1*C))--->(Regla de la suma)
O((n*C')+(m-1*C))=O(n+(m-1))--->(Regla del producto)
O(n+(m-1))=O(n+m)--->(Regla de la suma)
O(n+m)=O(m)--->(Regla de la suma, sabemos que m siempre es mayor o igual a n, ya que m es el numero de personas en el banco y n la fila entre las 4 existentes con mayor numero de personas )
T(n,m) es O(m)
donde m es el número de personas en el banco
"""