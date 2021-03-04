
def fix45(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]==5 and nums[j]==4:
                temporal=nums[j+1]
                nums[j+1]=nums[i]
                nums[i]=temporal
    return nums

print(fix45([4, 2, 4, 5, 5]))
print(fix45([]))
print(fix45([4, 9, 4, 9, 5, 5, 4, 9, 5]))
print(fix45([1, 4, 1, 5, 5, 4, 1]))