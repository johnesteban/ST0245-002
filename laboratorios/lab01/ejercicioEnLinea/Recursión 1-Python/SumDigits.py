def SumDigits(n):
   if n==0:
       return 0 #C1=3
   else:
       return (SumDigits(int(n/10))+(int(n%10))) #C2=5 T(n)=T(n/10)+C2
   
print(f'La suma de los digitos del numero 126 es: {SumDigits(126)}')

"""
CÁLCULO DE COMPLEJIDAD
T(n)=T(n/10)+C2
T(n)=[c2log(n)/log(10)]+c1--->(Al resolverla en WolframAlpha)
T(n)=c2log10(n)+C1--->(Cambio de base)
T(n) es O(c2log10(n)+C1)---->(Notación O)
O(c2log10(n)+C1)=O(c2log10(n))----->(Por regla de la suma)
O(c2log10(n))=O(log10(n))---->(Por regla del producto)
entonces T(n) es O(log10(n))
donde n es el número de digitos¿¿??
"""