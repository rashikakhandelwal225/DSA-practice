def smallerNumbersThanCurrent(nums):
    temp = sorted(nums)
    mapping = {}
    result = []
    for i in range(len(temp)):
        if temp[i] not in mapping:
            mapping[temp[i]] = i
    for i in range(len(nums)):
        result.append(mapping[nums[i]])
    return result

nums = [8,1, 2,2, 3]
print(smallerNumbersThanCurrent(nums))
nums = [6,5,4,8]
print(smallerNumbersThanCurrent(nums))
nums = [7,7,7,7]
print(smallerNumbersThanCurrent(nums))

#TC:O(n)
#SC: O(n)

