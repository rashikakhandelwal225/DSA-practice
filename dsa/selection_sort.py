def selectSort(l):
    n = len(l)
    for i in range(0, n-1):
        min_index = i
        for j in range(i, n):
            if l[j] < l[min_index]:
                min_index = j
        l[min_index], l[i] = l[i], l[min_index]

l = [7, 5, 9, 2, 8]
selectSort(l)
print(l)

