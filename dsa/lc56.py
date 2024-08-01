def merge(intervals):
    ans = []  # output merged interval
    temp = []
    stack = []
    intervals = sorted(intervals)
    stack.append(intervals[0])  # for storing intervals for merging

    for i in range(1, len(intervals)):
        if intervals[i][0] <= stack[-1][1]:
            temp = stack.pop()
            end = max(intervals[i][1], temp[1])
            stack.append([temp[0], end])
        else:
            stack.append([intervals[i][0], intervals[i][1]])

    while len(stack) > 0:
        ans.append(stack.pop())

    return ans

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
intervals = [[1,4],[4,5]]
print(merge(intervals))