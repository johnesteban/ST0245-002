
def maxSpan(nums):
    temporal=0
    maximo=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                temporal=j-i+1
                maximo=max(temporal,maximo)
    return maximo

print(maxSpan([1, 4, 2, 1, 4, 1, 4]))
print(maxSpan([]))
print(maxSpan([3, 3, 3]))
print(maxSpan([1, 2, 1, 1, 3]))


