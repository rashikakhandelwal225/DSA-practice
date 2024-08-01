def findNumbers(nums):
    c = 0
    c_list = [len(str(num))%2 == 0 for num in nums]
    return c_list.count(True)


nums = [12,345,2,6,7896]
print(findNumbers(nums))
nums = [555,901,482,1771]
print(findNumbers(nums))