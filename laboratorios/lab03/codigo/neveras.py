from collections import deque        
class Nevera():
    def __init__(self,codigo, descripcion):
        self.codigo=codigo
        self.descripcion=descripcion
        
    def concatenar(self):
        return '('+str(self.codigo)+','+self.descripcion+')'
    
class Solicitudes():
    def __init__(self, nombreT, cantidad):
        self.nombreT=nombreT
        self.cantidad=cantidad
    
    def asignarSolicitudes(neveras,solicitudes):
        if len(neveras)==0 or len(solicitudes)==0: #C1
            return "No hay nada solicitado o para asignar"  #C2
        StringFinal=""  #C3
        StringAcumulativa="" #C4
        totalsolicitudes=len(solicitudes) #C5
        for i in range(totalsolicitudes): #C6*n, donde n es el total de solicitudes
            solicitud=solicitudes.popleft() #C7*n
            i=0 #C8*n
            while len(neveras)>0 and i<solicitud.cantidad: #C9*n*m donde m es el numero de neveras
                nevera=neveras.pop() #C10*n*m
                StringAcumulativa+=nevera.concatenar()+',' #C11*n*m
                i+=1 #C12*n*m
            StringFinal+=solicitud.nombreT+'-->'+'['+StringAcumulativa[:len(StringAcumulativa)-1]+']'+'\n' #C13*n
            StringAcumulativa="" #C14*n
        return StringFinal#C15
"""
CALCULO DE COMPLEJIDAD
T(n,m)=C1+C2+C3+C4+C5+C6*n+C7*n+C8*n+C9*n*m+C10*n*m+C11*n*m+C12*n*m+C13*n+C14*n+C15
T(n,m) es O(C1+C2+C3+C4+C5+C6*n+C7*n+C8*n+C9*n*m+C10*n*m+C11*n*m+C12*n*m+C13*n+C14*n+C15)--->(Notación O)
O(C1+C2+C3+C4+C5+C6*n+C7*n+C8*n+C9*n*m+C10*n*m+C11*n*m+C12*n*m+C13*n+C14*n+C15)=O(n*(C6+C7+C8+C9+C13+C14)+n*m(C9+C10+C11+C12)+C')--->Regla de la suma y factor comun
O(n*(C6+C7+C8+C9+C13+C14)+n*m(C9+C10+C11+C12)+C')=O((n*C)+((n*m)*C^))--->Regla de la suma
O((n*C)+((n*m)*C^))=O(n+(n*m))---->Regla del producto
O(n+(n*m))=O(n*m)--->(Regla de la suma, tomo el maximo)
T(n,m) es O(n*m)
Donde n es el total de solicitudes o cantidad de tiendas que están solicitando las neveras
y m es el total de neveras disponibles en el almacén
"""    
class __main__():
    neveras=deque() #Es una pila
    neveras.appendleft(Nevera(1,"haceb"))
    neveras.appendleft(Nevera(2, "lg"))
    neveras.appendleft(Nevera(3, "ibm"))
    neveras.appendleft(Nevera(4, "haceb"))
    neveras.appendleft(Nevera(5, "lg"))
    neveras.appendleft(Nevera(6, "ibm"))
    neveras.appendleft(Nevera(7, "haceb"))
    neveras.appendleft(Nevera(8, "lg"))
    neveras.appendleft(Nevera(9, "ibm"))
    neveras.appendleft(Nevera(8, "lg"))
    neveras.appendleft(Nevera(9, "ibm"))
    
    solicitudes=deque() #Es una cola
    solicitudes.append(Solicitudes("exito", 1))
    solicitudes.append(Solicitudes("olimpica", 4))
    solicitudes.append(Solicitudes("la14", 2))
    solicitudes.append(Solicitudes("eafit",10))
    
    print(Solicitudes.asignarSolicitudes(neveras,solicitudes))
    
    neveras1=deque()
    solicitudes1=deque()
    print(Solicitudes.asignarSolicitudes(neveras1,solicitudes1))
    print(Solicitudes.asignarSolicitudes(neveras1,solicitudes))
    print(Solicitudes.asignarSolicitudes(neveras,solicitudes1))
    
    

