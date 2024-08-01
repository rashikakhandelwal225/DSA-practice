import math
def fullBloomFlowers(flowers, people):
    ans = [0] * len(people)
    flower_bloom_start = [x[0] for x in sorted(flowers, key=lambda x: x[0])]
    flower_bloom_end = [x[1] + 1 for x in sorted(flowers, key=lambda x: x[1])]

    def binary_search(array, date):
        low, high = 0, len(array)
        while low < high:
            mid = (low + high) // 2

            if array[mid] > date:
                high = mid
            else:
                low = mid + 1
        return low

    for i in range(len(people)):
        a = binary_search(flower_bloom_start, people[i])
        b = binary_search(flower_bloom_end, people[i])
        ans[i] = a - b
    return ans

flowers = [[19, 37], [19, 38], [19, 35]]
people = [6, 7, 21, 1, 13, 37, 5, 37, 46, 43]
print(fullBloomFlowers(flowers, people))

    # hashmap = {}
    # result = []
    # maximum_day = -math.inf
    # for i in range(len(flowers)):
    #     for j in range(len(flowers[i])):
    #         if flowers[i][j] > maximum_day:
    #             maximum_day = flowers[i][j]
    #
    # n = max(max(people), maximum_day)
    # for day in range(1, n+1):
    #     hashmap[day] = 0
    #
    # for flower in flowers:
    #     flag = False
    #     start_day = flower[0]
    #     end_day = flower[1]
    #     for day in range(1, maximum_day + 1):
    #         if day == start_day:
    #             hashmap[day] += 1
    #             flag = True
    #         elif flag == True and day < (end_day + 1):
    #             hashmap[day] += 1
    #         elif flag == False:
    #             continue
    #         else:
    #             break
    # print(hashmap)
    #
    # for peep in people:
    #     if peep in hashmap:
    #         result.append(hashmap[peep])
    #
    # return result





# flowers = [[1,6],[3,7],[9,12],[4,13]]
# people = [2,3,7,11]
# print(fullBloomFlowers(flowers, people))
#
# flowers = [[1,10],[3,3]]
# people = [3,3,2]
# print(fullBloomFlowers(flowers, people))

