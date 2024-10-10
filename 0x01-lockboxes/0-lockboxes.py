#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked."""
    n = len(boxes)
    unlocked = [False] * n  # Track the status of each lockbox
    unlocked[0] = True  # Box 0 being the first box is unlocked
    keys = boxes[0]  # Start with keys in box 0

    # While we have keys to check
    while keys:
        new_key = keys.pop()
        if 0 <= new_key < n and not unlocked[new_key]:
            unlocked[new_key] = True
            keys.extend(boxes[new_key])  # Add keys from this newly opened box

    # Check if all boxes are unlocked
    return all(unlocked)
