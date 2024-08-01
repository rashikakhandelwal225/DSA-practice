def GoldNuggets(nums):
    nums.sort()
    total_value = sum(nums)
    target_value = total_value // 2
    current_value = 0
    operations = 0

    for nugget in nums:
        current_value += nugget

        if current_value >= target_value:
            break
        else:
            operations += 1

    return operations

nums = [5, 19, 8, 1]
print(GoldNuggets(nums))

nums = [3, 8, 20]
print(GoldNuggets(nums))

nums = [3, 1 ,6, 6, 3 ,6]
print(GoldNuggets(nums))


