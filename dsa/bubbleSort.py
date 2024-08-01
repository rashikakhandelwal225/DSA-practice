def bubbleSort(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]

    return nums

nums = [2, 1, 10, 23]
print(bubbleSort(nums))





