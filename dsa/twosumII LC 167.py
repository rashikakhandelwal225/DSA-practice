def twoSum(numbers, target):
    nums = numbers
    for num in nums:
        second_no = (target-num)
        first_index = nums.index(num)
        if second_no in nums:
            if second_no == num:
                return [first_index + 1, first_index+ 2]
            elif second_no != num:
                return [first_index + 1, nums.index(second_no) + 1]

# numbers = [0,0,3,4]
# target = 0
# print(twoSum(numbers, target))
# numbers = [2,7,11,15]
# target = 9
# print(twoSum(numbers, target))
# numbers = [-1,0]
# target =-1
# print(twoSum(numbers, target))
# numbers = [1,2,3,4,4,9,56,90]
# target = 8
# print(twoSum(numbers, target))
numbers = [-1,-1,1,1]
target = -2
print(twoSum(numbers, target))
