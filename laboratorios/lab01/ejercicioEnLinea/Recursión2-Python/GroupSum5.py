def GroupSum5(start,nums,target):
    if start>=len(nums):
        if target==0:   
            return True 
     
        else:           
            return False  #C1=8
    if(nums[start]==1 and start>0 and nums[start-1]%5==0): 
      return GroupSum5(start+1,nums,target)  #C2=11 T(n)=T(n-1)+C3
    elif nums[start]%5==0:  
        return GroupSum5(start+1,nums,target-nums[start]) #C3=8 T(n)=T(n-1)+C4
    else:  
        return (GroupSum5(start+1,nums,target) or GroupSum5(start+1,nums,target-nums[start]))
        #C4=7  T(n)=2*T(n-1)+C4

print(GroupSum5(0, [2, 5, 10, 4], 11))
print(GroupSum5(0, [], 0))
print(GroupSum5(0, [2, 5, 10, 4], 12))

"""
CÁLCULO DE COMPLEJIDAD
T(n)=2*T(n-1)+C4
T(n)=C4(2^(n)-1)+C1(2^(n-1))--->(Al resolverla en WolframAlpha)
T(n) es O(C4(2^(n)-1)+C1(2^(n-1)))--->(Notación O)
O(C4(2^(n)-1)+C1(2^(n-1)))=O((2^(n)-1)+(2^(n-1)))--->(Por regla del producto)
O((2^(n)-1)+(2^(n-1)))=O(2^n+2^n)--->(Regla de la suma)
O(2^n+2^n)=O(2(2^n))---->(Factor comun)
O(2(2^n))=O(2^n)----->(Regla del producto)
Entonces T(n) es O(2^n) 
Donde n es la
"""