"""Example testing suite."""
import unittest
from primality_testing import is_prime


class TestPrimalityTesting(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_primes(self):
        primes = [
            2, 3, 5, 7, 11, 13, 17, 23, 31, 101, 137, 151,
            979982749, 979910219, 980414927, 961768781
        ]

        for prime in primes:
            self.assertTrue(is_prime(prime))

    def test_non_primes(self):
        non_primes = [
            1, 4, 6, 8, 9, 10, 12, 14, 15, 123, 155, 201,
            961770273, 961832591, 961872727, 961949947
        ]

        for non_prime in non_primes:
            self.assertFalse(is_prime(non_prime))
