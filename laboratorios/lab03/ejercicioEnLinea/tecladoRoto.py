class Lista():  
        def __init__(self):
            self.items = []
    
        def estaVacia(self):
            return self.items == []
    
        def agregarDerecha(self, item):
            self.items.append(item)
        
        def agregarIzquierda(self,item):
            self.items.insert(0,item)
    
        def avanzar(self):
            return self.items.pop(0)
    
        def tamano(self):
            return len(self.items)

class __main__():
    lista=Lista() #C1
    texto=str(input("Ingrese el texto")) #C2
    #asd[gfh[[dfh]hgh]fdfhd[dfg[d]g[d]dg 
    #dddfgdfhgfhasdhghfdfhdgdg
    #This_is_a_[Beiju]_text
    #BeijuThis_is_a__text 
    cadenaTemporal="" #C3
    i=0  #C4
    aux=0 #C5
    while i<len(texto): #C6*n donde n es la longitud del texto ingresado
        if(texto[i]=="["): #C7*n
            if aux==0: #C8*n
                lista.agregarIzquierda(cadenaTemporal)#C9*n
            else:
                lista.agregarDerecha(cadenaTemporal)
            cadenaTemporal="" #C10*n
            aux=0 #C11*n
            i+=1 #C12*n
        elif(texto[i]=="]"):
            if aux==0:
                lista.agregarIzquierda(cadenaTemporal)
            else:
                lista.agregarDerecha(cadenaTemporal)
            cadenaTemporal=""
            aux=1
            i+=1
        else:
            cadenaTemporal+=texto[i]
            i+=1
    if aux == 0: #C13
      lista.agregarIzquierda(cadenaTemporal) #C14
    else:
      lista.agregarDerecha(cadenaTemporal) 
       
    StringFinal=""  #C15
    for i in range(lista.tamano()): #C16*m donde m es la longitud de la cadena sin los corchetes
      StringFinal+=lista.avanzar() #C17*m
    print (StringFinal) #C18
        
            
"""
CALCULO DE COMPLEJIDAD
T(n,m)=C1+C2+C3+C4+C5+C6*n+C7*n+C8*n+C9*n+C10*n+C11*n+C12*n+C13+C14+C15+C16*m+C17*m+C18
T(n,m) es O(C1+C2+C3+C4+C5+C6*n+C7*n+C8*n+C9*n+C10*n+C11*n+C12*n+C13+C14+C15+C16*m+C17*m+C18)--->(Notación O)
O(C1+C2+C3+C4+C5+C6*n+C7*n+C8*n+C9*n+C10*n+C11*n+C12*n+C13+C14+C15+C16*m+C17*m+C18)=O((n*(C6+C8+C8+C9+C10+C11+C12))+(m*(C16+C17))+C')--->(Regla de la suma y factor comun)
O((n*(C6+C8+C8+C9+C10+C11+C12))+(m*(C16+C17))+C')=O(n*C+m*C)--->(Regla de la suma)
O(n*C+m*C)=O(n+m)--->(Regla del producto)
O(n+m)=O(n)--->(Regla de la suma, se que n es mayor ya que esta contiene los corchetes mientras que m no)
T(n,m) es O(n)
donde n es la longitud de la cadena de texto ingresada                                                                          
"""