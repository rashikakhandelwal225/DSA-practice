import math
def minimumRateToEatBananas(v: [int], h: int) -> int:
    a = v
    a.sort()
    start = 0
    end = a[-1]
    ans = 0


    while start <= end:
        mid = (start + end) // 2
        calculated_hrs = 0
        for i in range(len(v)):
            calculated_hrs += math.ceil(a[i] / mid)

        if calculated_hrs > h:
            start = mid + 1
        elif calculated_hrs <= h:
            ans = mid
            end = mid - 1
    return ans

v =  [7, 15, 6, 3]
h= 8
print(minimumRateToEatBananas(v,h))