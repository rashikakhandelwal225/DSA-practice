#

def stonebreaker(nums):
    while len(nums) > 1:
        # Find the two lightest stones
        min_index_1 = nums.index(min(nums))
        x = nums.pop(min_index_1)

        min_index_2 = nums.index(min(nums))
        y = nums.pop(min_index_2)

        # Smash the stones and update the array
        if x != y:
            nums.append(y - x)

    # If there's a stone left, return its weight; otherwise, return 0
    return nums[0] if nums else 0

nums = [2,7,4,1,8,1]
print(stonebreaker(nums))