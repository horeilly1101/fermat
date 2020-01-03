"""Testing utility functions."""
import random

PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 23, 31, 101, 137, 151,
    979982749, 979910219, 980414927, 961768781
]
NON_PRIMES = [
    1, 4, 6, 8, 9, 10, 12, 14, 15, 123, 155, 201,
    961770273, 961832591, 961872727, 961949947,
    1624
]


def get_random_non_perfect_square():
    num = random.randint(2, 100)
    square = pow(num, 2)
    return square - random.randint(1, 2 * num - 2)
