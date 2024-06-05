#!/usr/bin/python3
"""Given a pile of coins of different values,
determine the fewest number of
coins needed to meet a given amount total."""

def makeChange(coins, total):
    """ A script that determine the fewest number
     of coins needed to meet a given amount total."""

    if total <= 0:
        return 0

    d = [float('inf')] * (total + 1)
    d[0] = 0


    for coin in coins:
        for x in range(coin, total + 1):
            d[x] = min(d[x], d[x - coin] + 1)

    return d[total] if d[total] != float('inf') else -1
