import unittest
from mpmath import pi, mp, e
import random
from rsa.continued_fractions import PeriodicContinuedFraction, ContinuedFraction
from rsa.diophantine_expressions.pell_like_expression import PellLikeExpression


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
                pow(random.randint(2, 10000), 2) - 1
            )
            solution = expr.solve(1)
            self.assertEqual(
                1,
                solution.evaluate()
            )
