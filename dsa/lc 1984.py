def minimumDifference(nums, k):
    nums.sort()
    n = len(nums)
    ans = float('inf')

    for i in range(n - (k - 1)):
        ans = min((nums[i + k - 1] - nums[i]), ans)
    return ans
    # nums.sort()
    # return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))

nums = [9,4,1,7]
k = 2
print(minimumDifference(nums, k))