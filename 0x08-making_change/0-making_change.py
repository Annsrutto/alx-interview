#!/usr/bin/python3
"""Returns the fewest number of coins needed to meet total"""


def makeChange(coins, total):
    if total <= 0:
        return (0)

    # Initialize the dp array with a large number
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
