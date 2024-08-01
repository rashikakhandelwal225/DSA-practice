def sortArrayByParity(nums):
    left = 0
    right = len(nums)-1

    while left < right:
        if left < right and nums[left] %2 == 0:
            left +=1
        if left < right and nums[right] %2 !=0:
            right -=1
        nums[left], nums[right] = nums[right] , nums[left]
    return nums

nums = [3,1,2,4]
print(sortArrayByParity(nums))
nums = [0]
print(sortArrayByParity(nums))
nums = [0,1]
print(sortArrayByParity(nums))
