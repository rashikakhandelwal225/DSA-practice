from math import comb
def triangularSum(nums):
    ans = 0
    n = len(nums) - 1
    for i, j in enumerate(nums):
        ncr = comb(n, i)
        ans = (ans + ncr * j) % 10
    return ans

nums = [1,2,3,4,5]
print(triangularSum(nums))
nums = [5]
print(triangularSum(nums))
nums = [1 ,2, 3, 4, 5, 6, 7, 8, 9]
print(triangularSum(nums))