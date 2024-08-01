
def coinChange(coins, amount):
    if amount == 0:
        return 0
    elif len(coins) == 1 and amount > coins[0]:
        return -1
    else:

        def helper(coins, amount):
            coins.sort(reverse=True)
            print(coins)
            count = 0
            for ele in coins:
                if amount > ele:
                    count += 1
                    amount -= ele

                if amount == 0:
                    return count
    #
        count = helper(coins, amount)
    return count


# coins = [2]
# amount = 3
# print(coinChange(coins, amount))

coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))

# coins = [1]
# amount = 0
# print(coinChange(coins, amount))
#
# coins = [1, 2147483647]
# amount = 2
# print(coinChange(coins, amount))
























    # min_coin = 9999
    # flag = False
    # n = len(coins)
    # if amount == 0:
    #     return 0
    # elif n >= 1:
    #     for coin in coins:
    #         q = amount // coin
    #         r = amount % coin
    #         total_coins = q
    #         if r == 0:
    #             flag = True
    #         if r != 0 and r in coins:
    #             total_coins += r
    #             flag = True
    #         elif r != 0 and r not in coins:
    #             flag = False
    #         if flag == True:
    #             min_coin = min(min_coin, total_coins)
    #         if flag == False:
    #             return -1
    #     return min_coin
    # elif amount % coins[0] != 0:
    #     return -1
    # visited = {amount}
    # queue = [(amount, 0)]
    #
    # while len(queue) > 0:
    #     remained, level = queue.pop(0)
    #     if remained == 0:
    #         return level
    #     for c in coins:
    #         differ = remained - c
    #         if differ not in visited and differ >= 0:
    #             visited.add(differ)
    #             queue.append((differ, level + 1))
    #
    # return -1



