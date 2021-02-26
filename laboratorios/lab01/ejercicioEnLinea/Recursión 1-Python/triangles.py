def triangle(rows):
    if rows==0:
        return 0 #C1=3
    else:
        return triangle(rows-1)+rows #C2=4  T(n)=T(n-1)+C2
    
print(f'El numero de triangulos en 6 filas es: {triangle(6)}')

"""
CÁLCULO DE COMPLEJIDAD
T(n)=T(n-1)+C2
T(n)=C2n+C1--->(Al resolverla en WolframAlpha)
T(n) es O(C2n+C1)--->(Notación O)
O(C2n+C1)=O(C2n)--->(Por regla de la suma)
O(C2n)=O(n)----->(Por regla del producto)
entonces T(n) es O(n) 
donde n es el número de filas
"""