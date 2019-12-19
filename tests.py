"""Example testing suite."""
import unittest
from random_prime_generator import is_prime, is_witness


class TestPrimalityTesting(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_primes(self):
        primes = [
            2, 3, 5, 7, 11, 13, 17, 23, 31,
            101, 137
        ]

        for prime in primes:
            self.assertTrue(is_prime(prime))

    def test_non_primes(self):
        non_primes = [
            1, 4, 6, 8, 9, 10, 12, 14, 15,
            123, 155
        ]

        for non_prime in non_primes:
            self.assertFalse(is_prime(non_prime))
