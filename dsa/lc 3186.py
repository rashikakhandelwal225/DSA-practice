import math
def maximumTotalDamage(power):
    max_count = -math.inf
    count = 0


    for i in range(len(power)):
        for j in range(i-1, -1, -1):
            if power[i] != power[j] - 2 and power[i] != power[j] - 1 and power[i] != power[j] + 1 and power[i] != power[
                j] + 2:
                count += power[j]
        count += power[i]
`        max_count = max(count, max_count)
        count = 0
    return max_count
#
# power = [1,1,3,4]
# print(maximumTotalDamage(power))
power = [7,1,6,3]
print(maximumTotalDamage(power))
