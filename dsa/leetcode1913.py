def maxProductDifference(nums):
    nums = sorted(nums)
    r1 = nums[len(nums)-1]
    r2 = nums[len(nums)-2]
    l1 = nums[0]
    l2 = nums[1]
    return ((r1*r2) - (l1*l2))

nums = [5,6,2,7,4]
print(maxProductDifference(nums))
nums = [4,2,5,9,7,4,8]
print(maxProductDifference(nums))   