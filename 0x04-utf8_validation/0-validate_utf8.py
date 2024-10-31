#!/usr/bin/env python3
"""A UTF8 validator"""


def validUTF8(data):
    """A UTF8 validator"""
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for bytes in data:
        bytes = bytes & 0xFF

        if num_bytes == 0:
            mask = 1 << 7
            while mask & bytes:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

            num_bytes -= 1
        else:
            if not (bytes & mask1 and not (bytes & mask2)):
                return False

        num_bytes -= 1
    return num_bytes == 0
