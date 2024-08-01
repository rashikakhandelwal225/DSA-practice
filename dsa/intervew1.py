def chocolate(arr, m):
    min_ans = float('inf')
    n = len(arr)
    arr.sort()
    print(arr)
    for i in range(n-(m-1)):
        max_no = arr[i]
        min_no = arr[i]
        for j in range(m):
            j = i+m-1
            if  arr[j] > max_no:
                max_no = arr[i+m]
            if  arr[i+m] < min_no:
                min_no = arr[i+m]
        local_ans = max_no - min_no
        # print(local_ans)
        min_ans = min(min_ans, local_ans)

    return min_ans


# arr = [1, 3, 6, 8, 9, 9,9,9, 12, 56]

arr = [7, 3,2 , 4,9, 12, 56 ]
m = 3
print(chocolate(arr, m))
arr = [3, 4,1 ,9, 56, 7, 9, 12]
m =5
print(chocolate(arr, m))

1, 3,4, 7, 9, 9, 12, 56