import unittest
from rsa.prime_factorization import PrimeFactorization


class TestPrimeFactorization(unittest.TestCase):
    def test_factor(self):
        test_cases = {
            2: PrimeFactorization.of(2),
            3: PrimeFactorization.of(3),
            25: PrimeFactorization.of(5, 5),
            52: PrimeFactorization.of(2, 2, 13),
            33: PrimeFactorization.of(3, 11),
            pow(11, 2) * pow(43, 2): PrimeFactorization.of(11, 11, 43, 43)
        }

        for num, factorization in test_cases.items():
            self.assertEqual(
                factorization,
                PrimeFactorization.factor(num)
            )
