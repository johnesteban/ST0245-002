
def tripleUp(nums):
    for i in range(len(nums)-2):
        if nums[i]==nums[i]  and nums[i+1]==nums[i]+1 and nums[i+2]==nums[i]+2:
            return True
    return False

print(tripleUp([1, 2, 4, 5, 7, 6, 5, 6, 7, 6]))
print(tripleUp([10, 9, 8, -100, -99, -98, 100]))
print(tripleUp([]))
print(tripleUp([1, 2, 4, 5, 7, 6, 5, 7, 7, 6]))