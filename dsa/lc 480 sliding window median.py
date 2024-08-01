#Solution is right but it is showing Time limit exceeded so will be doing further using heaps when we learn
def call_odd_window(low, high, nums):
    local_list = nums[low:high + 1]
    local_list.sort()
    position = len(local_list) // 2
    median = local_list[position]
    return median


def call_even_window(low, high, nums):
    local_list = nums[low:high + 1]
    local_list.sort()
    mid = len(local_list) // 2
    print(local_list[mid - 1])
    print(local_list[mid])
    median = (local_list[mid - 1] + local_list[mid]) / 2
    return median


def medianSlidingWindow(nums, k):
    low = 0
    high = low + k - 1
    list1 = []
    n = len(nums)

    while low <= n - k:
        if k % 2 != 0:
            median = call_odd_window(low, high, nums)
            list1.append(median)
        else:
            median = call_even_window(low, high, nums)
            list1.append(median)
        low += 1
        high += 1
    return list1


nums =[1,4,2,3]
k=4
print(medianSlidingWindow(nums, k))