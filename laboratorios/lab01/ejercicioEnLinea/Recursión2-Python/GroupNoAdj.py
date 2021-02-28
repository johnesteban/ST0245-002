def GroupNoAdj(start,nums,target):
    if start>=len(nums):
        if target==0: 
                return True  
        else:   
            return False #C1=8
    return (GroupNoAdj(start+1,nums,target) or GroupNoAdj(start+2,nums,target-nums[start]))
   #C2=6 T(n)=T(n-1)+T(n-2)+C2
   
"""
CÁLCULO DE COMPLEJIDAD
T(n)=T(n-1)+T(n-2)+C2
T(n)=-C2+C1Fn+C2Ln--->(Al resolverla en WolframAlpha)
lo cual es igual a O(2^n)
donde n es es la longitud del arreglo, o en otras palabras es la distancia en términos 
de posiciones que hay desde el parámetro ‘start’ hasta el final del arreglo.
"""
print(GroupNoAdj(0, [2, 5, 10, 4, 2], 7))
print(GroupNoAdj(0, [], 0))
print(GroupNoAdj(0, [9], 1))
    

