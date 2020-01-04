"""
File that contains the RandomPrimeGenerator.
"""
from fermath.primality_testing import is_prime
import random


# def create_sieve(limit):
#     nums: list = [i for i in range(2, limit)]
#     for num in nums:
#         if num is None:
#             continue
#
#         for i in range(2, limit // num):
#             nums[num * i - 2] = None
#     return [i for i in nums if i is not None]


class RandomPrimeGenerator:
    """
    Class that randomly generates prime numbers.
    """
    def __init__(self, min_bits: int = 0, max_bits: int = 64):
        self._min_bits = min_bits
        self._max_bits = max_bits

    def generate(self) -> int:
        prime_candidate = random.randint(
            pow(2, self._min_bits),
            pow(2, self._max_bits)
        )
        while not is_prime(prime_candidate):
            prime_candidate += 1
        return prime_candidate
