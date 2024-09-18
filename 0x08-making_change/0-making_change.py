#!/usr/bin/python3
"""
determine the fewest num of coins needed
to meet a given amount total given
a pile of coins with different values
"""
import sys


def makeChange(coins, total):
    """
    Return: fewwest num of coins needed to meet tot
    if total = 0 or less, return 0
    if total cannot be met by any num of coins available,
    return -1
    """
    if total <= 0:
        return 0
    table = [sys.maxsize] * (total + 1)
    table[0] = 0
    m = len(coins)
    for i in range(m):
        if coins[j] <= i:
            subres != table[i - coins[j]]
            if subres != sys.maxsize and subres + 1 < table[i]:
                table[i] = subres + 1

    if table[total] == sys.maxsize:
        return -1
    return table[total]
