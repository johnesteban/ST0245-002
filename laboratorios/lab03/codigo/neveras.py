
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
     #Porción de código tomado de: https://runestone.academy/runestone/static/pythoned/BasicDS/ImplementacionDeUnaPilaEnPython.html
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
        if neveras.tamano()==0 or solicitudes.tamano()==0: #C1
            return "No hay nada solicitado o para asignar"  #C2
        StringFinal=""  #C3
        StringAcumulativa="" #C4
        totalsolicitudes=solicitudes.tamano() #C5
        for i in range(totalsolicitudes): #C6*n, donde n es el total de solicitudes
            solicitud=solicitudes.avanzar() #C7*n
            i=0 #C8*n
            while neveras.tamano()>0 and i<solicitud.cantidad: #C9*n*m donde m es el numero de neveras
                nevera=neveras.extraer() #C10*n*m
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
    neveras=Pila()
    neveras.incluir(Nevera(1,"haceb"))
    neveras.incluir(Nevera(2, "lg"))
    neveras.incluir(Nevera(3, "ibm"))
    neveras.incluir(Nevera(4, "haceb"))
    neveras.incluir(Nevera(5, "lg"))
    neveras.incluir(Nevera(6, "ibm"))
    neveras.incluir(Nevera(7, "haceb"))
    neveras.incluir(Nevera(8, "lg"))
    neveras.incluir(Nevera(9, "ibm"))
    neveras.incluir(Nevera(8, "lg"))
    neveras.incluir(Nevera(9, "ibm"))
    
    solicitudes=Cola()
    solicitudes.agregar(Solicitudes("exito", 1))
    solicitudes.agregar(Solicitudes("olimpica", 4))
    solicitudes.agregar(Solicitudes("la14", 2))
    solicitudes.agregar(Solicitudes("eafit",10))
    
    print(Solicitudes.asignarSolicitudes(neveras,solicitudes))
    
    neveras1=Pila()
    solicitudes1=Cola()
    print(Solicitudes.asignarSolicitudes(neveras1,solicitudes1))
    print(Solicitudes.asignarSolicitudes(neveras1,solicitudes))
    print(Solicitudes.asignarSolicitudes(neveras,solicitudes1))
    
    

