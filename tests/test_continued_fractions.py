import unittest
from mpmath import pi, mp, e
from rsa.continued_fractions import PeriodicContinuedFraction, ContinuedFraction
from rsa.continued_fractions.expression import SquareRoot


class TestContinuedFraction(unittest.TestCase):
    def test_make(self):
        mp.prec = 10000
        frac = ContinuedFraction.make(lambda: e)
        frac.get_convergent(20)
