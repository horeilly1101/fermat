import unittest
from rsa.factorizations.prime_factorization import PrimeFactorization


class TestPrimeFactorization(unittest.TestCase):
    def test_factor(self):
        factorizations = {
            2: [2],
            3: [3],
            25: [5, 5],
            52: [2, 2, 13],
            33: [3, 11],
            pow(11, 2) * pow(43, 2): [11, 11, 43, 43],
            # pow(61, 3) * 101: [61, 61, 61, 101]
        }

        for num, factors in factorizations.items():
            self.assertEqual(
                PrimeFactorization.of(*factors),
                PrimeFactorization.factor(num)
            )

    def test_compute_product(self):
        self.assertEqual(
            1,
            PrimeFactorization.of().compute_product()
        )
