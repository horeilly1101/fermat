import unittest
from rsa.prime_factorization import PrimeFactorization


class TestPrimeFactorization(unittest.TestCase):
    def test_factor(self):
        test_cases = {
            2: PrimeFactorization({2: 1}),
            3: PrimeFactorization({3: 1}),
            25: PrimeFactorization({5: 2}),
            52: PrimeFactorization({2: 2, 13: 1}),
            33: PrimeFactorization({3: 1, 11: 1}),
            pow(11, 2) * pow(43, 2): PrimeFactorization({11: 2, 43: 2})
        }

        for num, factorization in test_cases.items():
            self.assertEqual(
                factorization,
                PrimeFactorization.factor(num)
            )
