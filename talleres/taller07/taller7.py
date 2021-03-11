class Nodo():
    def __init__(self,obj=None,siguiente=None):
        self.obj=obj
        self.siguiente = siguiente
      
 
    def __str__(self):
        return "" + self.obj
 
class Lsimple():
    def __init__(self):
        self.first_Node = None
        self.last_Node = None
        self.size = 0
 
    def __void(self):
        return self.first_Node == None
 
    def size(self):
        self.size 
   
    def contains(self, obj):
        aux = self.first_Node
        contador=0
        while aux != None:
            if(aux.obj==obj):
                 return "La abeja si se encuentra en la posición "+str(contador)
            aux=aux.siguiente
            contador+=1  
        return "La abeja no se encuentra" 
 
    def insert(self, element, index):
        nuevo=Nodo(obj=element)
        if index<0 or index>self.size: 
            raise IndexError("Posición inválida")
        elif index==0:
            nuevo.siguiente=self.first_Node
            self.first_Node=nuevo
            self.size+=1
        else:
            pre=self.first_Node
            for i in range(1,index):
                pre=pre.siguiente
            nuevo.siguiente=pre.siguiente
            pre.siguiente=nuevo
            self.size+=1
 
    def remove(self, index):
        if index==None: 
            index=self.size-1
            if index==0:
                self.first_Node=self.first_Node.siguiente
                self.size-=1
            else:
                pre=self.first_Node
                actual=pre.siguiente
                for i in range(1,index):
                    pre=actual
                    actual=pre.siguiente
                pre.siguiente=actual.siguiente
                self.size-=1
        elif index<0 or index>=self.size:
            raise IndexError("Índice fuera de rango")
        elif index==0:
            self.first_Node=self.first_Node.siguiente
            self.size-=1
        else:
            pre=self.first_Node
            actual=pre.siguiente
            for i in range(1,index):
                 pre=actual
                 actual=pre.siguiente
            pre.siguiente=actual.siguiente
            self.size-=1
        
        
class bee():
  def __init__(self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
        

        
class __main__():
    listas=Lsimple()
    bee1=bee(1,2,3)
    bee2=bee(-10,4,20)
    bee3=bee(4,6,5)
    bee4=bee(200,45,50)
    bee5=bee(-100,-200,300)
    bee6=bee(-10,20,30)
    bee7=bee(40,50,30)
    bee8=bee(-1,-1,-1)
    bee9=bee(0,0,0)
    listas.insert(bee1,0)
    listas.insert(bee2,1)
    listas.insert(bee3,1)
    listas.remove(0)
    listas.remove(1)
    listas.insert(bee4,0)
    listas.insert(bee9,0)
    listas.insert(bee1,2)
    listas.remove(None)
    print(listas.contains(bee1))
    print(listas.contains(bee5))
    print(listas.contains(bee4))
    print(listas.contains(bee3))
    print("La longitud de la lista es: "+str(listas.size))
    
   
    
        
    
