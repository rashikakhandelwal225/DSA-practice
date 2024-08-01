def minPairSum(nums):
    max_sum = 0
    max_pair_sum = 0
    nums.sort()
    for i in range(len(nums)//2):
        left = nums[i]
        right = nums[len(nums)-1-i]
        max_sum = left + right
        
        
        if max_pair_sum <= max_sum:
            max_pair_sum = max_sum

    return max_pair_sum

nums = [3,5,4,2,4,6]
print(minPairSum(nums))
nums = [3,5,2,3]
print(minPairSum(nums))
