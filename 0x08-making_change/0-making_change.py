#!/usr/bin/python3
"""Making changes"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins
    needed to meet a given total.

    Parameters:
    coins (list): A list of the values of the
    coins in your possession.
    total (int): The total amount to achieve.

    Returns:
    int: Fewest number of coins needed to meet total,
    or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for greedy optimization
    coins.sort(reverse=True)

    # Try greedy approach
    remaining = total
    count = 0
    for coin in coins:
        if coin <= remaining:
            count += remaining // coin
            remaining %= coin

    if remaining == 0:
        return count

    # Fall back to DP if greedy fails
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
