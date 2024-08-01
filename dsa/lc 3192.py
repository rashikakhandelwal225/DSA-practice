def minOperations(nums):
    flips = 0
    expected = 1

    for num in nums:
        if num != expected:
            flips += 1
            expected = 1 - expected

    return flips

nums = [0,1,1,0,1]
print(minOperations(nums))
nums = [1,0,0,0]
print(minOperations(nums))
