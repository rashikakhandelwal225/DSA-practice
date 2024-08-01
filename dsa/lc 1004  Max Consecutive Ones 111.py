import math
def longestOnes(nums, k):
    hashmap = {}
    max_count = -math.inf
    max_value = 0

    for left in range(len(nums)):
        local_count_consecutive = 0
        local_found_zeros = 0
        right = left

        while right < len(nums):
            if local_found_zeros < k:
                if nums[right] == 0:
                    local_found_zeros += 1
                    local_count_consecutive += 1
                else:
                    local_count_consecutive += 1
            elif local_found_zeros == k and nums[right] == 1:
                local_count_consecutive += 1
            elif local_found_zeros == k and nums[right] == 0:
                break

            right += 1

        hashmap[left] = local_count_consecutive

    for value in hashmap.values():
        max_value = max(max_value, value)

    return max_value


# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k= 2
# print(longestOnes(nums, k))

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(longestOnes(nums, k))


# max_count = 0
    # count = 0
    # orig_k = k
    #
    # left = 0
    # right = 0
    #
    # while left<len(nums):
    #     if nums[right] <= len(nums)-1 and nums[right] == 0 and k != 0:
    #         k-=1
    #         if nums[right+1] == 1:
    #             count += 1
    #             right += 1
    #         elif k == 0:
    #             max_count = max(max_count, count)
    #             count = 0
    #             left += 1
    #             right = left
    #             k = orig_k
    #     count += 1
    #     right += 1
    #
    #
    #
    #
    #     if right == len(nums):
    #         left += 1
    #         right = left
    #         k = orig_k
    # return max_count
