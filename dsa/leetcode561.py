def arrayPairSum(nums):
    nums.sort()
    tot = 0
    for i in range(0,len(nums),2):
        tot = tot + nums[i]
    return tot

nums = [1,4,3,2]
print(arrayPairSum(nums))
nums = [6,2,6,5,1,2]
print(arrayPairSum(nums))