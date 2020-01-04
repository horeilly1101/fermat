import unittest
from mpmath import pi, mp, e
from fermat.continued_fractions import PeriodicContinuedFraction, ContinuedFraction
from fermat.diophantine_expressions.pell_like_expression import PellLikeExpression
from tests import utils


class TestContinuedFraction(unittest.TestCase):
    def test_solve(self):
        mp.prec = 10000
        frac = ContinuedFraction.make(lambda: e)
        frac.get_convergent(20)

    def test_solve_periodic(self):
        frac = PeriodicContinuedFraction.make_for_square_root(27)
        print(frac.representation)
        print(frac.period_length)

    def test_pell(self):
        for _ in range(20):
            expr = PellLikeExpression(
                utils.get_random_non_perfect_square()
            )
            solution = expr.solve(1)
            self.assertEqual(
                1,
                solution.evaluate()
            )
