#!/usr/bin/python3
"""
function to calculate how many square units of water will,
be retained after it rains.
"""


def rain(walls):
    """
    Calculates the total amount of rainwater retained between walls.

    Args:
        walls: list of non-negative integers representing wall heights

    Returns:
        Integer: total amount of rainwater retained
    """
    if not walls:
        return 0

    n = len(walls)
    total = 0

    for i in range(1, n - 1):
        left = max(walls[:i + 1])
        right = max(walls[i:])
        water = min(left, right) - walls[i]
        if water > 0:
            total += water

    return total
