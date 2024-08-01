# import math
#
# def minDays(bloomDay, m,k):
#     n = len(bloomDay)
#     flowers = m * k
#     ans = math.inf
#     low, high = min(bloomDay), max(bloomDay)
#
#     if flowers > n:
#         return -1
#     else:
#         while low <= high:
#             mid = (low + high) // 2
#             count = findFlowers(bloomDay, mid, k, m)
#
#             if count >= m:
#                 ans = min(ans, mid)
#                 high = mid - 1
#             else:
#                 low = mid + 1
#
#         return ans
#
# def findFlowers(nums, mid, k, m):
#     count = 0
#     curr_streak = 0
#
#     for num in nums:
#         if num <= mid:
#             curr_streak += 1
#             if curr_streak == k:
#                 count += 1
#                 curr_streak = 0
#         else:
#             curr_streak = 0
#
#     return count
#
# bloomDay = [1,10,3,10,2]
# m = 3
# k = 1
# print(minDays(bloomDay, m, k))
# bloomDay = [7,7,7,7,12,7,7]
# m = 2
# k = 3
# print(minDays(bloomDay, m, k))
# bloomDay = [1,10,3,10,2]
# m = 3
# k = 2
# print(minDays(bloomDay, m, k))
# bloomDay =[1000000000,1000000000]
# m=1
# k=1
# print(minDays(bloomDay, m, k))
# bloomDay =[1,10,2,9,3,8,4,7,5,6]
# m=4
# k=2
# print(minDays(bloomDay, m, k))











import math
def minDays(bloomDay, m, k):
    start = min(bloomDay)
    end = max(bloomDay)
    wait = math.inf
    # wait = -1
    total_flower_required = m * k
    if len(bloomDay) < total_flower_required:
        return -1
    else:
        while start <= end:
            mid = (start + end) // 2
            bouquet_ready = returnFlowerBloomDayAdj(mid, bloomDay, m, k)

            if bouquet_ready >= m:
                wait = min(wait, mid)
                end = mid - 1
            else:
                start = mid + 1

    return wait
    #         if bouquet_ready < m:
    #             wait = mid
    #             start = mid + 1
    #         elif bouquet_ready == m:
    #             wait = mid
    #             break
    #     return wait



def returnFlowerBloomDayAdj(mid, bloomDay,m,k):
    bouquet_ready = 0
    current_streak = 0  #finding flowers per bouquet
    for i in range(0, len(bloomDay)):
        if bloomDay[i] <= mid:
            current_streak += 1
            if current_streak == k:
                 bouquet_ready += 1
                 current_streak = 0
        else:
            current_streak = 0
    return bouquet_ready


bloomDay = [1,2,1,2,7,2,2,3,1]
m = 3
k=2
print(minDays(bloomDay, m, k))

# bloomDay = [1,10,3,10,2]
# m = 3
# k = 1
# print(minDays(bloomDay, m, k))
# bloomDay = [7,7,7,7,12,7,7]
# m = 2
# k = 3
# print(minDays(bloomDay, m, k))
# bloomDay = [1,10,3,10,2]
# m = 3
# k = 2
# print(minDays(bloomDay, m, k))
# bloomDay =[1000000000,1000000000]
# m=1
# k=1
# print(minDays(bloomDay, m, k))
# bloomDay =[1,10,2,9,3,8,4,7,5,6]
# m=4
# k=2
# print(minDays(bloomDay, m, k))
