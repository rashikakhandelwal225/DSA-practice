def numSubarraysWithSum(nums, goal):

    subarray_count = 0
    left = 0
    right = left + 1
    goal_count = nums[left]

    while right <= len(nums) - 1 and goal_count <= goal:
        if goal_count < goal:
            goal_count += nums[right]
            right += 1
        elif goal_count == goal:
            subarray_count += 1
            if right < len(nums) - 1 and nums[right] == 0:
                subarray_count += 1
            left += 1
            right = left + 1
            goal_count = nums[left]

    while left <= len(nums)-1:
        if goal_count == goal:
            subarray_count +=1
            goal_count -= nums[left]
            left += 1
        else:
            break


    return subarray_count

# nums = [1,0,1,0,1]
# goal = 2
# print(numSubarraysWithSum(nums, goal))
nums = [0,0,0,0,0]
goal = 0
print(numSubarraysWithSum(nums, goal))
