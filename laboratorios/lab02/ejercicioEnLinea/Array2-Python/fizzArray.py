def fizzArray(n):
    nums=[0]*n
    for i in range(len(nums)):
        nums[i]=i
    return nums

print(fizzArray(4))
print(fizzArray(0))
print(fizzArray(10))
print(fizzArray(1))

