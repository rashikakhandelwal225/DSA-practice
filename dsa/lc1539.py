def findKthPositive(arr, k):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        missing = arr[mid] - (mid+1)
        if missing < k:
            start = mid + 1
        else:
            end = mid - 1

    return (end+1+k)  # or low+k

arr = [2,3,4,7,11]
k = 5
print(findKthPositive(arr, k))
arr = [1,2,3,4]
k = 2
print(findKthPositive(arr, k))