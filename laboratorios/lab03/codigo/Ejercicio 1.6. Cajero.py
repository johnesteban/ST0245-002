from collections import deque
    
class Banco():
    def Simulacion(fila1, fila2, fila3, fila4): 
        filaFinal=deque() #C1
        while(len(fila1)>0 or len(fila2)>0 or len(fila3)>0 or len(fila4)>0): #C2*n donde n es la fila con mayor numero de personas
            if len(fila1)>0: #C3*n
                filaFinal.append(fila1.popleft()) #C4*n
            if len(fila2)>0: #C5*n
                filaFinal.append(fila2.popleft()) #C6*n
            if len(fila3)>0: #C7*n
                filaFinal.append(fila3.popleft())#C8*n
            if len(fila4)>0: #C9*n
                filaFinal.append(fila4.popleft()) #C10*n
        cajero1="Cajero 1" #C11
        cajero2="Cajero 2" #C12
        StringFinal="" #C13
        while len(filaFinal)>1: #C14*(m-1) donde m es el total de personas en el banco
            StringFinal+=cajero1+" atendiendo a "+filaFinal.popleft()+"\n" #C15*(m-1)
            StringFinal+=cajero2+" atendiendo a "+filaFinal.popleft()+"\n" #C16*(m-1)
        if len(filaFinal)>0: #C17
            StringFinal+=cajero1+" atendiendo a "+filaFinal.popleft() #C18 
        return StringFinal #C19
            
class __main__():
    fila1=deque()
    fila2=deque()
    fila3=deque()
    fila4=deque()
    fila1.append("Esteban")
    fila1.append("Angela")
    fila1.append("Laura")
    fila1.append("John")
    fila1.append("Diego")
    fila2.append("Nicolas")
    fila2.append("Santiago")
    fila2.append("Gladys")
    fila3.append("Diana")
    fila4.append("Camilo")
    fila4.append("Alejandra")
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