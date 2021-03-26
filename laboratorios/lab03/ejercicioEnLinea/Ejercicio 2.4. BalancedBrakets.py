from collections import deque

class Metodo():   
    def BalancedBrackets(texto):
        pila=deque() #C1
        
        for caracter in texto:  #C2*n donde n es la longitud del texto ingresado
            if (caracter=='{' or caracter=='[' or caracter=='('): #C3*n
                pila.appendleft(caracter)   #C4*n, la complejidad de appendleft es O(1)
            if(caracter=='}' or caracter==']' or caracter==')'): #C5*n
                ultimo=pila.popleft() #C6*n, la complejidad de popleft es O(1)
                if(ultimo=='{' and caracter=='}'): #C7*n
                    continue #C8*n
                if(ultimo=='[' and caracter==']'):
                    continue
                if(ultimo=='(' and caracter==')'):
                    continue
                else:
                    return "NO"
                
        if(len(pila)>0): #C9
            return "NO" #C10
        else:
            return "YES"
"""
CALCULO DE COMPLEJIDAD
T(n)=C1+C2*n+C3*n+C4*n+C5*n+C6*n+C7*n+C8*n+C9+C10
T(n) es O(C1+C2*n+C3*n+C4*n+C5*n+C6*n+C7*n+C8*n+C9+C10)  --->(Notación O)
O(C1+C2*n+C3*n+C4*n+C5*n+C6*n+C7*n+C8*n+C9+C10)=O(n*(C2+C3+C4+C5+C6+C7+C8)+C')--->(Factor comun y regla de la suma)
O(n*(C2+C3+C4+C5+C6+C7+C8)+C')=O(n*C)--->(Regla de la suma)
O(n*C)=O(n)--->(Regla del producto)
T(n) es O(n)
Donde n es la longitud del texto ingresado 
"""                                         
class __main__():
    print(Metodo.BalancedBrackets("{[()]}"))
    print(Metodo.BalancedBrackets("{[(])}"))
    print(Metodo.BalancedBrackets("{{[[(())]]}}"))
                
                
                
        

