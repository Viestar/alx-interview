#!/usr/bin/python3
""" Module that determines the least number of coins in a total """


def makeChange(coins, total):
    """ Return the least number of coins in a total """
    if total <= 0:
        return 0
    
 # Initialize a list to store the minimum number of coins needed for each total from 0 to the given total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make a total of 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each total amount
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the total amount cannot be met by any combination of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
