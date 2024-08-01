def bubble_sort(nums):
    # print(set(nums))  # 1. sort using set
    n = len(nums)       # or 2. sort using bubble sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def findFinalValue(nums, original):
    hashmap = {}
    nums = bubble_sort(nums)

    for num in nums:
        if num not in hashmap:
            hashmap[num] = 2 * num

    while original in hashmap:
        original = hashmap[original]
    return int(original)
#
nums = [5,3,6,1,12]
original = 3
print(findFinalValue(nums, original))
# bubble_sort(nums)