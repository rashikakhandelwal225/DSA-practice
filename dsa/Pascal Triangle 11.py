def getRow(rowIndex):
    dp = [[0] * (rowIndex+1) for _ in range(rowIndex+1)]
    dp[0][0] = 1

    for i in range(1, rowIndex + 1):
        for j in range(0, rowIndex + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j]
            elif i == j:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[rowIndex]

rowIndex = 4
print(getRow(rowIndex))

rowIndex = 0
print(getRow(rowIndex))

rowIndex = 1
print(getRow(rowIndex))