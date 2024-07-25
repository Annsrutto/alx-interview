#!/usr/bin/python3
"""Returns the fewest number of coins needed to meet total"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize dp array with total + 1 (impossible value)
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount

    # Iterate through all amounts from 1 to total
    for amount in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
