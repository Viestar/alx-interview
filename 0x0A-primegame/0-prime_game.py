#!/usr/bin/python3
"""
Prime Game Module
"""


def is_prime(num):
    """Check if a number is prime"""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(n):
    """Generate all prime numbers up to n"""
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def round_winner(primes_left):
    """Determine the winner of a round"""
    if len(primes_left) % 2 == 0:
        return "Maria"
    else:
        return "Ben"


def isWinner(x, nums):
    """Determine the winner of the game"""
    wins = {"Maria": 0, "Ben": 0}
    for n in nums:
        primes = get_primes(n)
        winner = round_winner(primes)
        wins[winner] += 1

    if wins["Maria"] == wins["Ben"]:
        return None
    elif wins["Maria"] > wins["Ben"]:
        return "Ben"
    else:
        return "Maria"


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
