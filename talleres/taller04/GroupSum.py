from time import time

def Suma_grupo(start, nums, target):
    if start>=len(nums):
        if target ==0:
            return True
        else:
            return False
    return Suma_grupo(start+1, nums, target) or Suma_grupo(start+1, nums, target-nums[start])

#Tamaño del prob
for i in range(5,25):
    inicio=time()
    print(Suma_grupo(0,[0]*i,10))
    fin=time()
    total=fin-inicio
    print(total)
    
#La gráfica está en Excel y la gráfica da de manera exponencial, entonces 
#para datos pequeños el programa funcionará bien
#ya que tomará poco tiempo, pero a medida que crecen, consumirá demasiado tiempo.
    
    