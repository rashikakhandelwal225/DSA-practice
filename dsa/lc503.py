def nextGreaterElements(nums):
    stack = []
    n = len(nums)
    ans = [-1] * n

    stack.append(0)

    for i in range(1, n):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            ans[stack[-1]] = nums[i]
            stack.pop()

        stack.append(i)

    for i in range(0, n):
        while len(stack) > 0 and nums[i] > nums[stack[-1]]:
            ans[stack[-1]] = nums[i]
            stack.pop()


    return ans

nums = [1,2,1]
print(nextGreaterElements(nums))
nums = [1,2,3,4,3]
print(nextGreaterElements(nums))