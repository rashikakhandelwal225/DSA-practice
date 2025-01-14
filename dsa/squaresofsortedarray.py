def sortedSquares(nums):
    left = 0
    right = len(nums)-1
    out = [0] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        if abs(nums[right]) >= abs(nums[left]):
            out[i] = nums[right] **2
            right -=1
        else:
            out[i] = nums[left] **2
            left +=1
    return out

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))
nums = [-7,-3,2,3,11]
print(sortedSquares(nums))


