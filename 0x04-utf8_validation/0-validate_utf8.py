#!/usr/bin/python3
"""A module for validating UTF-8 encoding."""


def validUTF8(data):
    """
    Determines if a given data set represents a valid
    UTF-8 encoding.

    Args:
        data (list): A list of integers, each representing
        a byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding,
        else False.
    """
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character.
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if byte follows the pattern 10xxxxxx.
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
