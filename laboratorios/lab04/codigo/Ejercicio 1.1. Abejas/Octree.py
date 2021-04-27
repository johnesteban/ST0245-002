
import math
class Octree:
    def octree(self,abejas,mins,midD,midW,midH):
        self.midD=midD
        self.midW=midW
        self.midH=midH
        self.abejas=abejas
        octree=[]
        for i in range(8):
            ab=[]
            octree.append(ab)
        for i in range(len(abejas)):
            abeja=abejas.pop(0)
            sector=self.hashing(abeja,mins)
            octree[sector].insert(0,abeja)   
        diagonal=math.sqrt((midD*111325)**2+(midW*111325)**2+midH**2)
        if diagonal>100:
            for i in range(8):
                if(len(octree[i])>1):
                    self.nuevoOctree(octree[i],mins,i)
        else:
            for i in range(8):
                if(len(octree[i])>0):
                    self.choque(octree[i])
                
    def hashing(self,abeja,mins):
        if abeja.getLatitude()<=mins[0]+self.midD:
            if abeja.getLongitude()<=mins[1]+self.midW:
                if abeja.getAltitude()<=mins[2]+self.midH:
                    return 0
                else:
                    return 1
            else:
                if abeja.getAltitude()<=mins[2]+self.midH:
                    return 2
                else:
                    return 3
        else:
            if abeja.getLongitude()<=mins[1]+self.midW:
                if abeja.getAltitude()<=mins[2]+self.midH:
                    return 4
                else:
                    return 5
            else:
                if abeja.getAltitude()<=mins[2]+self.midH:
                    return 6
                else:
                    return 7
    
    def nuevoOctree(self,abejas,mins,sector):
        if sector==0:
           self.octree(abejas,mins,self.midD/2,self.midW/2,self.midH/2)
        elif sector==1:
            nuevoH=mins[2]+self.midH
            mins[2]=nuevoH
            self.octree(abejas,mins,self.midD/2,self.midW/2,self.midH/2)
        elif sector==2:
            nuevoW=mins[1]+self.midW
            mins[1]=nuevoW
            self.octree(abejas,mins,self.midD/2,self.midW/2,self.midH/2)
        elif sector==3:
            nuevoH=mins[2]+self.midH
            mins[2]=nuevoH
            nuevoW=mins[1]+self.midW
            mins[1]=nuevoW
            self.octree(abejas,mins,self.midD/2,self.midW/2,self.midH/2)
        elif sector==4:
            nuevoD=mins[0]+self.midD
            mins[0]=nuevoD
            self.octree(abejas,mins,self.midD/2,self.midW/2,self.midH/2);
        elif sector==5:
            nuevoD=mins[0]+self.midD
            mins[0]=nuevoD
            nuevoH=mins[2]+self.midH
            mins[2]=nuevoH
            self.octree(abejas,mins,self.midD/2,self.midW/2,self.midH/2)
        elif sector==6:
            nuevoD=mins[0]+self.midD
            mins[0]=nuevoD
            nuevoW=mins[1]+self.midW
            mins[1]=nuevoW
            self.octree(abejas,mins,self.midD/2,self.midW/2,self.midH/2)
        else:
            nuevoD=mins[0]+self.midD
            mins[0]=nuevoD
            nuevoW=mins[1]+self.midW
            mins[1]=nuevoW
            nuevoH=mins[2]+self.midH
            mins[2]=nuevoH
            self.octree(abejas,mins,self.midD/2,self.midW/2,self.midH/2)
        
    def choque(self,abejas):
        for abeja in abejas:
           print(str(abeja.getLatitude())+","+str(abeja.getLongitude())+","+str(abeja.getAltitude()))

#Se hizo con ayuda del spoiler que se encuentra en la carpeta de github: https://github.com/mauriciotoro/ST0245-Eafit/tree/master/laboratorios/lab04/spoiler/java/ejercicio-abejas
