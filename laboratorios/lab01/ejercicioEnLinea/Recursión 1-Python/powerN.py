
def powerN(base,n):
    if n==1:
        return base #C1=3
    else:
        return powerN(base,n-1)*base #C2=4 T(n)=T(n-1)+C2

print(f'El resultado de 3 elevado a la 3 es: {powerN(3,3)}')

"""
CÁLCULO DE COMPLEJIDAD
T(n)=T(n-1)+C2
T(n)=C2n+C1--->(Al resolverla en WolframAlpha)
T(n) es O(C2n+C1)--->(Notación O)
O(C2n+C1)=O(C2n)--->(Por regla de la suma)
O(C2n)=O(n)----->(Por regla del producto)
entonces T(n) es O(n) 
donde n la potencia a la cual se esta elevando la base
"""