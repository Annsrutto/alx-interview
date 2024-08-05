#!/usr/bin/python3
"""
0-prime_game module
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game.

    Args:
        x (int): The number of rounds.
        nums (list of int): List of n values for each round.

    Returns:
        str: Name of the player that won the most rounds, or None.
    """
    if not nums or x < 1:
        return None

    def sieve(n):
        """ Helper function to perform the Sieve of Eratosthenes """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for start in range(2, int(n**0.5) + 1):
            if is_prime[start]:
                for i in range(start * start, n + 1, start):
                    is_prime[i] = False
        return is_prime

    max_num = max(nums)
    is_prime = sieve(max_num)
    primes_count = [0] * (max_num + 1)

    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1]
        if is_prime[i]:
            primes_count[i] += 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
