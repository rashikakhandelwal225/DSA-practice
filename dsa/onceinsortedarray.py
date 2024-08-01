def onceInASortedArray(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        left_count = (mid - start) + 1
        right_count = (end - (mid + 1)) + 1

        if start == end:
            print(mid)
            break
        elif left_count % 2 != 0:
            end = mid
        elif right_count % 2 != 0:
            start = mid + 1

    return mid

arr = [1,1 ,2 ,3, 3, 4, 4, 8, 8]
print(onceInASortedArray(arr))