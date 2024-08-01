def returnchild(n):

    return ans


def numberOfChild(n, k):
    flag = 0
    ans = 80

    hashmap = {}

    for time in range(k):
        if time not in hashmap:
            hashmap[time] = returnchild(n, flag)

























    # i = 0
    # while i <= k:
    #     if flag == 0:
    #         for j in range(0, n):
    #             ans = j
    #         flag = 1
    #     elif flag == 1:
    #         for j in range(n - 2, -1, -1):
    #             ans = j
    #         flag = 0
    #     i += 1
    #
    # if i == k:
    #     return ans

n = 3
k = 5
print(numberOfChild(n, k))
