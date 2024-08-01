import math

class Solution:
    def determine_winner(self, a, b, n):
        turn = 0  # 0 for Bholu, 1 for Dholu

        while n >= 0:
            if turn == 0:
                stones_to_take = math.gcd(a, n)
            else:
                stones_to_take = math.gcd(b, n)

            if stones_to_take > n:
                return 1 - turn  # The current player cannot take the required stones, so the other player wins

            n -= stones_to_take
            turn = 1 - turn  # Switch turns

        return turn  # The player who cannot make a move loses

# Example usage:
solution_instance = Solution()
a, b, n = map(int, input().split())
result = solution_instance.determine_winner(a, b, n)
print(result)