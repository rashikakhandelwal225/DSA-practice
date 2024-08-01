def valueAfterKSeconds(n, k):

    time = 1
    arr = arr = [1] * n
    hashmap = {}
    hashmap[0] = arr
    while time <= k:
        result = [1]
        for i in range(1,n):
            result.append(result[i - 1] + arr[i])
        hashmap[time] = result
        arr = result
        result = []
        time += 1

    return hashmap[k][-1]

n = 4
k = 5
print(valueAfterKSeconds(n, k))
