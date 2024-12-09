#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """A prime is a natural number greater
    than 1 that has no positive divisors
    other than 1 and itself.
    """
    def sieve_of_eratosthenes(limit):
        """Return a list of primes up to limit."""
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, limit + 1, i):
                    sieve[multiple] = False
        return [i for i in range(limit + 1) if sieve[i]]

    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    # Precompute results for all values up to max_num
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1]
        if i in primes:
            prime_counts[i] += 1

    maria_wins, ben_wins = 0, 0

    for n in nums:
        if prime_counts[n] % 2 == 0:  # Ben wins if primes are even
            ben_wins += 1
        else:  # Maria wins if primes are odd
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
