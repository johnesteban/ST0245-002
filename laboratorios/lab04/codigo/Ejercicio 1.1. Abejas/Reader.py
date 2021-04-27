
import math
from Octree import Octree as oc
from Abejas___ import bee 
class Reader:
    def __init__(self,archivo):
        self.archivo=archivo
    def leer(self,archivo):
        archivo=open(archivo,'r')
        textoString=archivo.read()
        archivo.close()
        Lineas=textoString.split("\n")
        arreglo=[]
        maximoX=-math.inf
        minimoX=math.inf
        maximoY=-math.inf
        minimoY=math.inf
        minimoZ=math.inf
        maximoZ=-math.inf
        print("---CONJUNTO DE DATOS CON "+str(len(Lineas)-2)+" ABEJAS---")
        for linea in Lineas:
            columnas=linea.split(",")
            if len(columnas)<3:
                break
            if columnas[0]=="Coordenada x de la abeja":
                continue
            x=float(columnas[0])
            y=float(columnas[1])
            z=float(columnas[2])
            if x<minimoX:
                minimoX=x
            if x>maximoX:
                maximoX=x
            if y<minimoY:
                minimoY=y
            if y>maximoY:
                maximoY=y
            if z<minimoZ:
                minimoZ=z
            if z>maximoZ:
                maximoZ=z
            abeja=bee(x,y,z)
            arreglo.append(abeja)
            print(str(x)+","+str(y)+","+str(z))
        print("\n")
        print("---ABEJAS QUE COLISIONAN---")
        self.abejas=arreglo
        midD=(minimoX-maximoX)/2
        midW=(maximoY-minimoY)/2
        midH=(maximoZ-minimoZ)/2
        mins=[minimoX,minimoY,minimoZ]
        ph=math.sqrt(math.pow((midD)*111325,2)+math.pow((midW)*111325,2))
        diagonal=math.sqrt(math.pow(ph,2)+math.pow((midH),2))
        if (diagonal>100):
            arbol=oc()
            arbol.octree(arreglo,mins,midD,midW,midH)
        else:
            self.choque()
            
    def choque(self):
        for abeja in self.abejas:
            print(str(abeja.getLatitude())+","+str(abeja.getLongitude())+","+str(abeja.getAltitude()))
            
    


