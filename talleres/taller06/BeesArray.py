class ArrayList():
    
    __elements = []

    def __init__(self):   #T(n)=O(1)
        self.__elements = []

    def size(self): #T(n)=O(1)
        return len(self.__elements)

    def get(self, index):   #T(n)=O(1)
        if(index>=0 and index<self.__elements.size):
            return self.__elements[index]

    def add(self, object): #T(n)=O(n)
        self.__elements.append(object)

    def addInIndex(self, index, object): #T(n)=O(n)
        self.__elements = self.__elements[:index]+[object]+self.__elements[index:]

    def removeInIndex(self,index): #T(n)=O(n)
       self.__elements.pop(index)
    
arr = ArrayList()
arr.add(23)

"""
Complejidad de añadir
O(n)
"""
