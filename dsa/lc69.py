def mySqrt(x):
    start = 0
    end = x
    ans = 0

    while start <= end:
        mid = start + ((end - start) // 2)
        if mid * mid > x:
            end = mid - 1
        elif mid*mid <= x:
            ans = mid
            start = mid + 1
    return ans

x =16
print(mySqrt(x))