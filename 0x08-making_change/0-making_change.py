#!/usr/bin/python3
""" Determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """ Determine the fewest number of coins needed to meet the total.

    Args:
        coins (list): A list of integers representing coin denominations.
        total (int): The total amount you need to make change for.

    Returns:
        int: The fewest number of coins needed to make the total amount.
             If the total cannot be met with the given coins, return -1.
             If the total is 0 or less, return 0.
    """
    if total <= 0:
        return 0

    # Coins validity check
    if (coins is None or len(coins) == 0):
        return -1

    change = 0
    available_coins = sorted(coins, reverse=True)
    change_left = total

    for coin in available_coins:
        while (change_left % coin >= 0 and change_left >= coin):
            change += int(change_left / coin)
            change_left = change_left % coin

    change = change if change_left == 0 else -1

    return change
