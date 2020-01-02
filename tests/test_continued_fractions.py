import unittest
import math
from itertools import tee

from rsa.continued_fractions.continued_fraction import ContinuedFraction
from rsa.continued_fractions import PeriodicContinuedFraction
from rsa.continued_fractions.expression import SquareRoot


class TestContinuedFraction(unittest.TestCase):
    def test_make(self):
        frac = PeriodicContinuedFraction.make_from_square_root(SquareRoot(7))
        print(frac.representation)
