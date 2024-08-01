def countKDifference(nums, k):
    count = 0
    hashmap = {}

    i = 0
    j = 1

    while i < j and i < len(nums) - 1 and j < len(nums):
        if abs(nums[i] - nums[j]) == k:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        j += 1

        if j > len(nums) - 1:
            i += 1
            j = i+1

    for c in hashmap.values():
        count += c
    return count

nums = [1,2,2,1]
k = 1
print(countKDifference(nums, k))
nums = [1,3]
k = 3
print(countKDifference(nums, k))
nums = [3,2,1,5,4]
k = 2
print(countKDifference(nums, k))