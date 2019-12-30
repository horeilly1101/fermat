import unittest
from rsa.sum_of_squares import SumOfSquares


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
