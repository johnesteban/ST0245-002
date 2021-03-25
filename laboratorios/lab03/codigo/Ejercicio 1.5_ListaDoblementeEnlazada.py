class Nodo():
    def __init__(self,obj=None,siguiente=None, anterior=None):
        self.obj=obj
        self.siguiente = siguiente
        self.anterior=anterior
 
    def __str__(self):
        return "" + str(self.obj)

class ListaDoblementeEnlazada():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 
    
        
 ##append: agrega un valor al final de la lista
    def append(self,obj): #O(1)
        new_node=Nodo(obj,None,None)
        if self.head is None:
            self.head=new_node
            self.tail=self.head
        else:
            new_node.anterior=self.tail 
            self.tail.siguiente=new_node
            self.tail=new_node
        self.size+=1
        
    def get(self,index):
        if index<0 or index>=self.size:
            raise IndexError("La posición no existe")
        else:
            temp = self.head
            for i in range(index):
                temp = temp.siguiente
            return temp
    
    def insert(self,data,index):#en el peor de los casos, cuando no se inserta al principio o final es O(n)
        new_node=Nodo(data,None,None)
        
        if self.head is None:
            self.head=new_node
            self.tail=self.head
            self.size+=1
        elif index==self.size:
            self.append(data)
        elif index==0:
            new_node.siguiente=self.head
            self.head=new_node
            self.size+=1
        elif index<self.size:
            pre=self.head
            for i in range(index-1):
                pre=pre.siguiente
            new_node.siguiente=pre.siguiente
            pre.siguiente=new_node
            new_node.anterior=pre
            pre.siguiente.anterior=new_node
            self.size+=1
        else:
            print("Index not reachable")
            
    def remove(self,index): #en el peor de los casos, cuando no se inserta al principio o final es O(n)
        if self.head is None:
            print("Index not reachable")
        if index==0 and self.size==1:
            self.head=None
            self.tail=None
            self.size-=1
        elif index==0:
            self.head=self.head.siguiente
            self.size-=1
        elif index<0 or index>=self.size:
            print("Index not reachable")
        elif index==self.size-1:
            pre=self.head
            for i in range(index-1):
                 pre=pre.siguiente
            self.tail=pre
            pre.siguiente=None
            self.size-=1
        elif index==self.size-2:
            pre=self.head
            for i in range(index-1):
                pre=pre.siguiente
            pre.siguiente.siguiente.anterior=pre
            pre.siguiente=pre.siguiente.siguiente
            pre.siguiente.siguiente=self.tail
            self.size-=1
        else:
            pre=self.head
            for i in range(index-1):
                 pre=pre.siguiente
            pre.siguiente.siguiente.anterior=pre
            pre.siguiente=pre.siguiente.siguiente
            self.size-=1
        
    def contains(self,data):
        aux = self.head
        while aux != None:
            if(aux.obj==data):
                 return True
            aux=aux.siguiente
        return False 
        
        
class __main__():
    lista=ListaDoblementeEnlazada()
    lista.insert(1,0)
    lista.remove(0)
    lista.append(4)
    lista.insert(2,0)
    lista.insert(3,0)
    lista.insert(5,1)
    lista.insert(3,4)
    lista.remove(1)
    lista.remove(2)
    lista.remove(2)
    lista.insert(6,2)
    print(lista.size)
    print(lista.contains(1))
    print(lista.contains(3))
    print(lista.contains(5))
    print(lista.contains(4))
    print(lista.get(0))
    print(lista.get(1))
    print(lista.get(2))
   
