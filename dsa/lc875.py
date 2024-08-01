import math
def minEatingSpeed(piles, h):
    start = 1
    end = max(piles)

    ans =end

    while start <= end:
        mid = (start + end) // 2
        h1 = 0
        for i in range(len(piles)):
            print(h1)
            h1 += math.ceil(piles[i] / mid)
        if h1 > h:
            start = mid + 1
        elif h1 < h:
            ans = mid
            end = mid - 1
    return ans

# piles = [3,6,7,11]
# h = 8
# print(minEatingSpeed(piles, h))
# piles = [30,11,23,4,20]
# h = 5
# print(minEatingSpeed(piles, h))
piles = [312884470]
h = 312884469
print(minEatingSpeed(piles, h))