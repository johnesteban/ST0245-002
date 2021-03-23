
class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

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
        if neveras.tamano()==0 or solicitudes.tamano()==0:
            return "No hay nada solicitado o para asignar"
        StringFinal=""
        StringAcumulativa=""
        totalsolicitudes=solicitudes.tamano()
        for i in range(totalsolicitudes): 
            solicitud=solicitudes.avanzar()
            i=0
            while neveras.tamano()>0 and i<solicitud.cantidad:
                nevera=neveras.extraer()
                StringAcumulativa+=nevera.concatenar()+','
                i+=1
            StringFinal+=solicitud.nombreT+'-->'+'['+StringAcumulativa[:len(StringAcumulativa)-1]+']'+'\n'
            StringAcumulativa=""
        return StringFinal
        
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
    solicitudes1=Pila()
    print(Solicitudes.asignarSolicitudes(neveras1,solicitudes1))
    print(Solicitudes.asignarSolicitudes(neveras1,solicitudes))
    print(Solicitudes.asignarSolicitudes(neveras,solicitudes1))
    
    

