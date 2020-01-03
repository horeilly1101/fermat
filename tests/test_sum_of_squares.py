import unittest
from rsa.diophantine_expressions.sum_of_squares import SumOfSquaresSolution, SumOfSquaresExpression
from rsa.factorizations.prime_factorization import PrimeFactorization
import tests.utils as utils


class TestSumOfSquares(unittest.TestCase):
    def setUp(self) -> None:
        self.sos = SumOfSquaresExpression()

    def test_exists(self):
        valid_cases = [
            1, 2, 5, 9 * 5
        ]

        for case in valid_cases:
            self.assertTrue(self.sos.solution_exists(case))

    def test_raise_to_power(self):
        solution = SumOfSquaresSolution(self.sos, 4, 1)
        solution_raised = solution.raise_to_power(5)
        self.assertEqual(
            pow(17, 5),
            solution_raised.evaluate()
        )

    def test_make(self):
        sos = self.sos.solve_for_pf(
            PrimeFactorization.of(
                *[prime for prime in utils.PRIMES if prime % 4 == 1]
            )
        )
        self.assertEqual(
            sos.evaluate(),
            pow(sos.x, 2) + pow(sos.y, 2)
        )
