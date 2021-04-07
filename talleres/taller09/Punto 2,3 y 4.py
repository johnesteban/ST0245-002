# Punto 2
print('Punto 2:')
empresas = {'Google': 'Estados Unidos',
            'La Locura': 'Colombia',
            'Nokia': 'Finlandia',
            'Sony': 'Japon'}

for key, values in empresas.items():
    print(key, values) 

#Punto 3
def Punto3(key):
    return empresas.get(key)

# Punto 4
def LlaveAsociada(value):
    paises=empresas.values()
    if(value in paises):
        return True
    return False

print("Punto 3")
print(Punto3('Google'))
print(Punto3('Motorola'))
print("Punto 4")
print(LlaveAsociada('China'))
print(LlaveAsociada('Colombia'))
