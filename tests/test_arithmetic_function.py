import unittest
import random
from rsa.arithmetic_functions import *


class TestArithmeticFunction(unittest.TestCase):
    def test_dirichlet_product(self):
        identities = {
            (phi, u): identity,
            (u, u): d,
            (u, identity): sigma,
            (mu, u): delta
        }

        for _ in range(20):
            num = random.randint(1, 1000)
            for (func1, func2), value in identities.items():
                self.assertEqual(
                    value.evaluate(num),
                    func1.compute_dirichlet_product(func2).evaluate(num)
                )
