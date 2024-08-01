def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    flag = False
    output = []

    for ele in nums1:
        flag = False
        flag = bsearch(ele, nums2)
        if flag == True:
            output.append(ele)

    return list(set(output))


def bsearch(ele, nums2):
    low = 0
    high = len(nums2)-1

    while low <= high:
        mid = low + (high - low) // 2

        if ele == nums2[mid]:
            return True
        elif ele > nums2[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))