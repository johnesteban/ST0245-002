
def bunnyEars2(bunnies):
   if bunnies==0: 
       return 0   #C1=3
   elif bunnies%2==0:
       return 3+bunnyEars2(bunnies-1) #C2=6  T(n)=C2+T(n-1)
   else:
      return 2+bunnyEars2(bunnies-1)  #C3=4 T(n)=C3+T(n-1)
"""
CÁLCULO DE COMPLEJIDAD
T(n)=T(n-1)+C3
T(n)=C3n+C1---(Al resolverla en WolframAlpha)
T(n) es O(C3n+C1)---(Notación O)
O(C3n+C1)=O(C3n)---(Por regla de la suma)
O(C3n)=O(n)-----(Por regla del producto)
entonces T(n) es O(n)
donde n es el número de conejos
"""
print(f'El numero de orejas de 5 conejos es: {bunnyEars2(5)}')

