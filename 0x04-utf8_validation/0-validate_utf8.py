#!/usr/bin/python3


def validUTF8(data):
    """
    Determines if a given data set
    represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers,
        each representing a byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding,
        else False.
    """
    num_bytes = 0
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        byte = byte & 0xFF  # Keep only the last 8 bits

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # If it's a 1-byte character or invalid byte count
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For subsequent bytes, check if they
            # follow the pattern 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
