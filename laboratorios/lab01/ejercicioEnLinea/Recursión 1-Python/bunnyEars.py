
def bunnyEars(bunnies):
    if bunnies==0: 
        return 0   #C1=3
    else:
        return bunnyEars(bunnies-1)+2  #C2=4  #T(n)=T(n-1)+C2
    
"""
CÁLCULO DE COMPLEJIDAD
T(n)=T(n-1)+C2
T(n)=C2n+C1---(Al resolverla en WolframAlpha)
T(n) es O(C2n+C1)---(Notación O)
O(C2n+C1)=O(C2n)---(Por regla de la suma)
O(C2n)=O(n)-----(Por regla del producto)
entonces T(n) es O(n)
donde n es el número de conejos
"""
    
print(f'El numero de orejas de 4 conejos es: {bunnyEars(4)}')
