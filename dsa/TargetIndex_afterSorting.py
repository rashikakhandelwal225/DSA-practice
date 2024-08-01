def targetIndices(nums, target):
    nums.sort()
    low = 0
    high = len(nums) - 1
    output = []

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            output.append(mid)
            if nums[mid+1] == nums[mid]:
                low = mid +1
            elif nums[mid-1] == nums[mid]:
                high =mid-1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        output.sort()
    return output

# nums = [1,2,5,2,3]
# target = 5
# print(targetIndices(nums, target))
nums = [1,2,5,2,3]
target = 2
print(targetIndices(nums, target))