def GroupSum6(start, nums, target):
    if start>=len(nums): 
        if target==0: 
                return True  
        else:   
                return False #C1=8
    if nums[start]==6: 
        return GroupSum6(start+1,nums,target-nums[start]) #C2=7 T(n)=T(n-1)+C2
    else: 
        return (GroupSum6(start+1,nums,target) or GroupSum6(start+1,nums,target-nums[start])) 
  #C3=7 y T(n)=2*T(n-1)+C3

print(GroupSum6(0, [1, 6, 2, 6, 4], 12))
print(GroupSum6(0, [1, 6, 2, 6, 4], 4))

"""
CÁLCULO DE COMPLEJIDAD
T(n)=2*T(n-1)+C3
T(n)=C3(2^(n)-1)+C1(2^(n-1))--->(Al resolverla en WolframAlpha)
T(n) es O(C3(2^(n)-1)+C1(2^(n-1)))---->(Notación O)
O(C3(2^(n)-1)+C1(2^(n-1)))=O((2^(n)-1)+(2^(n-1)))---->(Regla del producto)
O((2^(n)-1)+(2^(n-1)))=O(2^n+2^n)--->(Regla de la suma)
O(2^n+2^n)=O(2(2^n))---->(Factor comun)
O(2(2^n))=O(2^n)----->(Regla del producto)
Entonces T(n) es O(2^n) 
donde n es la
"""