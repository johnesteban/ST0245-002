def SplitOdd10(nums):
    return auxiliar(0,0,0,nums) 

def auxiliar(i,a,b,nums):
  if i>=len(nums):
    return (a%10==0 and b%2==1) or (b%10==0 and a%2==1) #C1=15
  else: 
    return auxiliar(i+1, a+nums[i],b,nums) or auxiliar(i+1,a,b+nums[i],nums)
    #C2=9 T(n)=2*T(n-1)+C2
    
"""
CÁLCULO DE COMPLEJIDAD
T(n)=2*T(n-1)+C2
T(n)=C2(2^(n)-1)+C1(2^(n-1))--->(Al resolverla en WolframAlpha)
T(n) es O(C2(2^(n)-1)+C1(2^(n-1)))--->(Notación O)
O(C2(2^(n)-1)+C1(2^(n-1)))=O((2^(n)-1)+(2^(n-1)))--->(Por regla del producto)
O((2^(n)-1)+(2^(n-1)))=O(2^n+2^n)--->(Regla de la suma)
O(2^n+2^n)=O(2(2^n))---->(Factor comun)
O(2(2^n))=O(2^n)----->(Regla del producto)
Entonces T(n) es O(2^n) 
Donde n es la
"""


