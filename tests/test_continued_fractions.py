import unittest
import math
from itertools import tee

from rsa.continued_fractions.continued_fraction import ContinuedFraction, \
    PeriodicContinuedFraction
from rsa.continued_fractions.generators import cf_representation_generator, \
    periodic_cf_representation_generator
from rsa.continued_fractions.expression import SquareRoot


class TestContinuedFraction(unittest.TestCase):
    def test_make(self):
        frac = PeriodicContinuedFraction.make_from_square_root(SquareRoot(7))
        print(frac.representation)
