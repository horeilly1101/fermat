import unittest
from rsa.sum_of_squares import SumOfSquares
from rsa.factorizations.prime_factorization import PrimeFactorization
import tests.testing_utils as utils


class TestSumOfSquares(unittest.TestCase):
    def test_exists(self):
        valid_cases = [
            1, 2, 5, 9 * 5
        ]

        for case in valid_cases:
            self.assertTrue(SumOfSquares.exists(case))

    def test_raise_to_power(self):
        sos = SumOfSquares(1, 4, 17)
        sos_raised = sos.raise_to_power(5)
        self.assertEqual(
            pow(17, 5),
            sos_raised.result
        )

        self.assertEqual(
            pow(17, 5),
            pow(sos_raised.a, 2) + pow(sos_raised.b, 2)
        )

    def test_make(self):
        sos = SumOfSquares.make_from_prime_factorization(
            PrimeFactorization.of(
                *[prime for prime in utils.PRIMES if prime % 4 == 1]
            )
        )
        self.assertEqual(
            sos.result,
            pow(sos.a, 2) + pow(sos.b, 2)
        )
