def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    start = 0
    end = m
    ans = -1

    while start <= end:
        mid = (start+end)//2
        n_power_mid = pow(mid, n)
        if n_power_mid == m:
            ans = mid
            break
        elif n_power_mid < m:
            start = mid+1
        elif n_power_mid > m:
            end = mid - 1
    return ans


print(NthRoot(3, 27))

print(NthRoot(4, 69))