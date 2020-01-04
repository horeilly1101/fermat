"""Testing for primality testing."""
import unittest
from numbers.primality_testing import is_prime
from tests.utils import PRIMES, NON_PRIMES


class TestPrimalityTesting(unittest.TestCase):
    """Testing Suite for primality testing."""
    def test_primes(self):
        for prime in PRIMES:
            self.assertTrue(
                is_prime(prime)
            )

    def test_non_primes(self):
        for non_prime in NON_PRIMES:
            self.assertFalse(
                is_prime(non_prime)
            )
