def threeSum(nums):
    result_list = []
    nums.sort()

    for fixed in range(len(nums)-2):
        if fixed > 0 and nums[fixed] == nums[fixed-1]:
            continue
        start = fixed + 1
        end = len(nums) - 1
        while start < end:
            target = nums[fixed] + nums[start] + nums[end]

            if target < 0:
                start += 1
            elif target > 0:
                end -= 1
            else:
                result_list.append([nums[fixed], nums[start], nums[end]])
                # Skip duplicate values of the second and third numbers
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1

                start += 1
                end -= 1
    return result_list

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
nums = [0,1,1]
print(threeSum(nums))
nums = [0,0,0]
print(threeSum(nums))











