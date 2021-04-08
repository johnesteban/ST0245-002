
class hash_table:
    def __init__(self):
        self.tabla=[None]*500
    
    def Hash_func(self,key):
        clave= 0
        for i in range(len(key)):
            clave+=ord(key[i]) 
        return clave%500
    
    def get(self, key):
        if self.tabla[self.Hash_func(key)] is None:
            return "El elemento no existe"
        else:
            return self.tabla[self.Hash_func(key)][1]

    def Insert(self,key,valor):
       if self.tabla[self.Hash_func(key)] is None:
            self.tabla[self.Hash_func(key)]=(key,valor)
    
            
class archivo():
    archivo=open("usda-dc-directory.csv",'r') #NO uso C: ni D:
    texto_en_string=archivo.read()
    archivo.close()
    separado_por_lineas=texto_en_string.split("\n") # \n quiere decir salto de linea
    tabla_de_hash=hash_table()
    
    for linea in separado_por_lineas:
        columnas = linea.split(",")
        apellido = columnas[0]
        nombre = columnas[1]
        telefono = columnas[3]
        tabla_de_hash.Insert(nombre+" "+apellido,telefono)
        
    print(tabla_de_hash.tabla)
        
    """for nombre_y_apellido in tabla_de_hash.tabla:
        print(nombre_y_apellido + ": " + tabla_de_hash.get(nombre_y_apellido))

class __main__():      
    H = hash_table()
    H.Insert("Neil G","31323203")
    H.Insert("Nelly","23892991")
    H.Insert("Nick Dane","9901902292")
    H.Insert("Rodney George","39021091")

    print(H.get("Nelly"))
    print(H.get("Aakla"))
    print(H.tabla)
"""
