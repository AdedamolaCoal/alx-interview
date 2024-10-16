#!/usr/bin/python3
"""
This module defines a function minOperations that calculates the fewest
number of operations needed to result in exactly n 'H' characters in
a text file, starting with one 'H'. The only allowed operations are:
'Copy All' and 'Paste'.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters
    in the text file, starting with a single 'H'. Operations allowed are 'Copy All' and 'Paste'.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required to reach exactly n 'H' characters.
         If n is less than or equal to 1, return 0 as it's impossible to reach.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
