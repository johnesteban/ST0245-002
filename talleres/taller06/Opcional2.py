def Invertir_arreglo(array):
    n = len(array) #C1
    for i in range(0,int(n/2)): #C2*n/2
        temp = array[i]         #C3*n/2
        array[i] = array[n-i]   #C4*n/2
        array[n-i] = temp       #C5*n/2
    return array   #C6
a=[]  #C7
n=int(input("Ingrese un número entero ")) #C8
while n!=-1:  #C9*n
    a.append(n) #C10*n*n
    n=int(input("Ingrese un número entero "))#C11

print(a)  #C12
print(Invertir_arreglo(a)) #C13

#Complejidad:
    #T(n)= C1+C2*n/2+C3*n/2+C4*n/2+C5*n/2+C6+C7+C8+C9*n+C10*n*n+C11+C12+C13
    #T(n)=n/2*(C2+C3+C4+C5)+C9*n+C10*n*n+C----->(Regla de la suma y factor comun)
    #T(n)=n/2*C+C9*n+C10*n*n---------->(Regla de la suma)
    #T(n)=n/2+n+n^2------>(Regla del producto)
    #T(n)=n^2---->(Tomo el valor más grande, los demás se pueden tomar como constantes)
    #T(n)=O(n^2)---->(Notación O)