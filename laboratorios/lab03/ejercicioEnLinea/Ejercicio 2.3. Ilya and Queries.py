from collections import deque

cadena=str(input()) #C1
consultas=int(input()) #C2
cola=deque() #C3

cola.append(0) #C4
contador=0 #C5
contadorPop=1 #C6

#Creo la cola de numeros, sumando 1 cada vez que el anterior caracter donde estoy parado es igual al anterior
for i in range(1,len(cadena)): #C7*(n-1) donde n es la longitud de la cadena ingresada
    if cadena[i]==cadena[i-1]: #C8*(n-1)
        cola.append(1+contador) #C9*(n-1), ya que el metodo append es O(1) en una cola
        contador+=1 #C10*(n-1)
    else:
        cola.append(0+contador)

#Itero para obtener el resultado esperado
StringAcumulativa="" #C11
for i in range(consultas): #C12*m, donde m es el número de consultas que se desean hacer
    copia=cola.copy() #C13*m
    #print("Ingrese la ronda "+str(i+1)+" de numeros") #C14*m
    entrada=input()
    entero1,entero2=entrada.split()
    entero1=int(entero1) #C15*m
    entero2=int(entero2) #C16*m
    if entero1>=entero2 or entero1<1 or entero2>len(cadena):
        continue
    else: #C17*m
        while contadorPop<=entero1: #C18*m*n, se puede decir que en el peor caso es n ya que al entero 1 no se le pueden ingresar valores mayores a la longitud de la cadena y n es la longitud de la cadena
            contadorPop+=1 #C18*m*n
            numero1=cola.popleft() #C19*m*n
        contadorPop-=1 #C20*m
        while contadorPop<entero2: #C21*m*n, se puede decir que en el peor caso es n ya que al entero 2 no se le pueden ingresar valores mayores a la longitud de la cadena y n es la longitud de la cadena
            contadorPop+=1 #C22*m*n
            numero2=cola.popleft() #C23*m*n
    contadorPop=1 #C24*m
    cola=copia #C25*m
    StringAcumulativa+="Resultado de la ronda "+str(i+1)+" de números: "+str(numero2-numero1)+'\n'  #C26*m

print('\n') #C27
print("-RESULTADO FINAL-")  #C28  
print(StringAcumulativa) #C29

"""
CALCULO DE COMPLEJIDAD
T(n,m)=C1+C2+C3+C4+C5+C6+C7*(n-1)+C8*(n-1)+C9*(n-1)+C10*(n-1)+C11+C12*m+C13*m+C14*m+C15*m+C16*m+C17*m+C18*(m*n)+C19*(m*n)+C20*(m*n)+C21*(m*n)+C22*(m*n)+C23*(m*n)+C24*m+C25*m+C26*m+C27+C28
Lo de la linea anterior es igual a O(C1+C2+C3+C4+C5+C6+C7*(n-1)+C8*(n-1)+C9*(n-1)+C10*(n-1)+C11+C12*m+C13*m+C14*m+C15*m+C16*m+C17*m+C18*(m*n)+C19*(m*n)+C20*(m*n)+C21*(m*n)+C22*(m*n)+C23*(m*n)+C24*m+C25*m+C26*m+C27+C28)---->(Notacion O)
Lo anterior es igual a O(((n-1)*(C7+C8+C9+C10))+(m*(C12+C13+C14+C15+C16+C17))+((m*n)(C18+C19+C20+C21+C22+C23))+C')--->(Factor común y regla de la suma)
Lo anterior es igual a O((n-1)*C+m*C+(n*m)*C)--->(Regla de la suma)
Lo anterior es igual a O((n-1)+m+(n*m))--->(Regla del producto) 
O((n-1)+m+(n*m))=O(n+m+(n*m)) --->(Regla de la suma)  
O(n+m+(n*m))=O(n*m)--->(Regla de la suma, sé que n*m es mayor que n y m ya que en el problema se especifica que n siempre sera mayor o igual a 2 y m siempre será mayor o igual a 1)
T(n,m)=O(n*m)
donde n es la longitud de la cadena ingresada
y m es el número de consultas que se desean realizar            
"""
        
        
        
        
        
        

