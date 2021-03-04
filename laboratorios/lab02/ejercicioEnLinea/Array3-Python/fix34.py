
def fix34(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]==4 and nums[j]==3:
                temporal=nums[j+1]
                nums[j+1]=nums[i]
                nums[i]=temporal
    return nums

print(fix34([1, 3, 1, 4, 4, 3, 1]))
print(fix34([5, 3, 5, 4, 5, 4, 5, 4, 3, 5, 3, 5]))
print(fix34([]))
print(fix34([3, 1, 4, 3, 1, 4]))