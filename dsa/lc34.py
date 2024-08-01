def searchRange(nums,target):
    result = []
    def findFirst(nums,target):
        result = []
        start = 0
        first = -1
        end = len(nums) - 1

        # search for 1st occurrence
        while start <= end:
            mid = start + ((end - start) // 2)

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if nums[mid] == target:
                    first = mid
                    end = mid - 1
        return first

    def findLast(nums, target):
        result = []
        start = 0
        last = -1
        end = len(nums) - 1

        # search for 1st occurrence
        while start <= end:
            mid = start + ((end - start) // 2)

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if nums[mid] == target:
                    last = mid
                    start = mid + 1
        return last


    first = findFirst(nums, target)
    last = findLast(nums, target)
    result.append(first)
    result.append(last)
    return result
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums,target))
target = 6
print(searchRange(nums,target))