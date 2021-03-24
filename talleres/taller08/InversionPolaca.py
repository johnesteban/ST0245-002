class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.insert(0,item)

     def extraer(self):
         return self.items.pop(0)

     def tamano(self):
         return len(self.items)
     
     def operate(self,op, a, b):
        if(op=='+'):
            return a+b
        elif(op=='-'):
            return b-a
        elif(op=='*'):
            return a*b
        elif(op=='/'):
            return b/a
        else:
            print("Operacion no valida")

class InversionPolaca():
    def evaluate():
        resultado = 0
        exp = input('Ingrese la expresion a evaluar: ')
        exp = exp.split()
        total=Pila()
        for i in exp:
            if i.isnumeric():
                total.incluir(i)
            else:
                resultado=total.operate(i,int(total.extraer()),int(total.extraer()))
                total.incluir(resultado)
        return total.extraer()

    print(evaluate())

