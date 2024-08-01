def generate(numRows):
    dp = [[0] * (numRows) for _ in range(numRows)]
    dp[0][0] = 1

    # for i in range(1, numRows):
    #     dp.append(self.helper(numRows, i))

    for i in range(1, numRows):

        for j in range(0, numRows):
            if j == 0:
                dp[i][j] = dp[i - 1][j]
            elif i == j:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    for list1 in dp:
        for i in range(len(list1)):
            if list1[-1] == 0:
                list1.pop(-1)

    return dp

numRows = 5
print(generate(numRows))
