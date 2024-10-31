#!/usr/bin/python3
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers, each representing one byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes remaining in the current UTF-8 character sequence
    num_bytes = 0
    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Ensure only the last 8 bits are considered (as per the requirement)
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            # 1-byte character (no additional bytes expected)
            if num_bytes == 0:
                continue

            # If num_bytes is 1 or exceeds 4, the encoding is invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # For subsequent bytes, check if they follow the pattern 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes remaining in the current character sequence
        num_bytes -= 1

    # If num_bytes is zero, all characters were validated successfully
    return num_bytes == 0
