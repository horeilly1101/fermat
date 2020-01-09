import unittest
from functools import reduce

from fermat.diophantine_expressions.sum_of_squares_expression import SumOfSquaresSolution, SumOfSquaresExpression
from fermat.diophantine_expressions.ppt_expression import PPTExpression
from fermat.factorizations.prime_factorization import PrimeFactorization
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

    def test_solve(self):
        valid_prime_factors = [prime for prime in utils.PRIMES if prime % 4 == 1]
        sos = self.sos.solve_for_pf(
            PrimeFactorization.of(
                *valid_prime_factors
            )
        )
        multiple = reduce(lambda result, prime: result * prime, valid_prime_factors, 1)
        self.assertEqual(
            sos.evaluate(),
            multiple
        )

    def test_multiply(self):
        sol = SumOfSquaresSolution(self.sos, 2, 1)

        # 5^2
        # sold52_1 = SumOfSquaresSolution(self.sos, 5, 0)
        sol52_2 = SumOfSquaresSolution(self.sos, 3, 4)

        # 5^3
        sol53_1 = SumOfSquaresSolution(self.sos, 11, 2)
        sol53_2 = SumOfSquaresSolution(self.sos, 10, 5)

        # 5^4
        sol54_1 = SumOfSquaresSolution(self.sos, 15, 20)
        sol54_2 = SumOfSquaresSolution(self.sos, 24, 7)
        # sol54_3 = SumOfSquaresSolution(self.sos, 25, 0)

        # 5^5
        sol55_1 = SumOfSquaresSolution(self.sos, 55, 10)  # 54_2
        sol55_2 = SumOfSquaresSolution(self.sos, 50, 25)  # 54_3
        sol55_3 = SumOfSquaresSolution(self.sos, 38, 41)  # 54_2

        # 5^6
        sol56_1 = SumOfSquaresSolution(self.sos, 117, 44)
        sol56_2 = SumOfSquaresSolution(self.sos, 120, 35)
        # sol56_3 = SumOfSquaresSolution(self.sos, 125, 0)
        sol56_4 = SumOfSquaresSolution(self.sos, 100, 75)

        print(sol.multiply2(sol53_1))
        print(sol.multiply2(sol53_2))

    def test_ppt(self):
        ppt = PPTExpression()
        # for i in range(1000):
        #     if ppt.solution_exists(i):
        #         print(i, ppt.solve(i), ppt.solve(i).evaluate())
        #         ppt.solve(i)
