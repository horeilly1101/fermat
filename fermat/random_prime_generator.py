"""
File that contains the RandomPrimeGenerator.
"""
from fermat.primality_testing import is_prime
import random


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
