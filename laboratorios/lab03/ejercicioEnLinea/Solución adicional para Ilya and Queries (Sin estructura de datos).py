texto=input()
consultas=int(input())
contador=0
StringAcumulativa=""
for i in range(consultas): #C1*n
    contador=0 #C2*n
    print("Ingrese la ronda "+str(i+1)+" de números ")
    consulta1=int(input()) #C3*n
    consulta2=int(input()) #C4*n
    if consulta1>=consulta2 or consulta1<1 or consulta2>len(texto):
        continue
    for j in range(consulta1,consulta2): #C5*m*n, en donde m es la diferencia entre el entero 2 y entero 1, en el peor caso será igual a la longitud de la cadena
        if texto[j]==texto[j-1]: #C6*m*n
            contador+=1  #C7*m*n
    StringAcumulativa+="resultado de la ronda "+str(i+1)+": "+str(contador)+"\n" #C8*m*n
print("\n")
print("---RESULTADO---")
print(StringAcumulativa)
"""
CALCULO DE COMPLEJIDAD
T(n,m)=C1*n+C2*n+C3*n+C4*n+C5*(m*n)+C6*(m*n)+C7*(m*n)+C8*(m*n)
T(n,m) es O(C1*n+C2*n+C3*n+C4*n+C5*(m*n)+C6*(m*n)+C7*(m*n)+C8*(m*n))--->(Notación O)
O(C1*n+C2*n+C3*n+C4*n+C5*(m*n)+C6*(m*n)+C7*(m*n)+C8*(m*n))=O((n*(C1+C2+C3+C4))+((n*m)(C5+C6+C7+C8)))--->(Factor común)
O((n*(C1+C2+C3+C4))+((n*m)(C5+C6+C7+C8)))=O(n*C+(n*m)*C)--->(Regla de la suma)
O(n*C+(n*m)*C)=O(n+(n*m))--->(Regla del producto)
O(n+(n*m))=O(n*m)--->(Regla de la suma)
T(n,m) es O(n*m)
en donde n es el número de consultas a realizar y m la longitud de la cadena
"""
