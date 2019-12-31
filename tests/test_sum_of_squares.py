import unittest
from rsa.sum_of_squares import SumOfSquares
from rsa.factorization import PrimeFactorization


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
        # print(
        #     SumOfSquares.make_from_prime_factorization(
        #         PrimeFactorization.of(
        #             29, 41, 61, 5, 3, 3, 2,
        #             3, 2, 3, 7, 7, 29, 2, 2,
        #             2, 2, 2, 3, 3, 2, 2, 2,
        #             2, 2, 2, 2, 2, 2, 2, 2,
        #             2, 2, 2, 2, 2, 2, 2, 2,
        #             2, 2, 2, 2, 2, 2, 2, 2,
        #             2, 2, 2, 2, 2, 2, 2, 2,
        #             41, 41, 41, 41, 41, 41,
        #             5, 5, 5, 5, 5, 5, 5, 5,
        #             17, 17
        #         )
        #     )
        # )
        print(
            SumOfSquares.make(29*41*61*5*3*3*2)
        )
