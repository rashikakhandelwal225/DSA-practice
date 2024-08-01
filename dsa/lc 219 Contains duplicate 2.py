def containsNearbyDuplicate(nums, k):
    i = 0
    j = i + 1

    while i < len(nums)  - 1:
        if j == len(nums):
            i+=1
            j = i+1
        if abs(i-j)<=k and i== len(nums)-2 and j == len(nums)-1:
            if nums[i] == nums[j]:
                return True
            else:
                return False

        if abs(i - j) == k and nums[i] == nums[j]:
            return True
        elif abs(i - j) < k and nums[i] == nums[j]:
            return True
        elif abs(i - j) < k and nums[i] != nums[j]:
            j += 1
        else:
            i += 1
            j = i + 1


    return False


nums = [99,99]
k=2
print(containsNearbyDuplicate(nums, k))
#
nums = [1,2,3,4,5,6,7,8,9,9]
k = 3
print(containsNearbyDuplicate(nums, k))

# nums = [1,2,3,1,2,3]
# k=2
# print(containsNearbyDuplicate(nums, k))



# i = 0
    # j = i + 1
    #
    # while i < j and i < len(nums):
    #     if abs(i - j) <= k and j < len(nums):
    #         if nums[i] == nums[j] :
    #             return True
    #         else:
    #             j += 1
    #     else:
    #         i += 1
    #         j=i+1
    # return False