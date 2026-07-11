#!/usr/bin/python3
"""Module that calculates how much rainwater is retained between walls"""


def rain(walls):
    """Calculates the total rainwater retained between walls

    Args:
        walls (list): list of non-negative integers representing wall heights

    Returns:
        int: total square units of water retained
    """
    if not walls:
        return 0

    left = 0
    right = len(walls) - 1
    left_max = walls[left]
    right_max = walls[right]
    total = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, walls[left])
            total += left_max - walls[left]
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            total += right_max - walls[right]

    return total
