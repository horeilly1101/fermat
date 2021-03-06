import unittest
import random
from fermat.diophantine_expressions.linear_expression import LinearExpression
from tests.utils import PRIMES


class TestLDExpression(unittest.TestCase):
    def test_gcd_primes(self):
        for p1 in PRIMES:
            for p2 in PRIMES:
                if p1 != p2:
                    # since primes are relatively prime, we expect
                    # their gcd to be 1, and we expect the generated
                    # solution to equal 1
                    expr = LinearExpression(p1, p2)
                    solution = expr.solve(1)
                    self.assertEqual(
                        1,
                        solution.evaluate()
                    )

    def test_gcd_composites(self):
        for p1 in PRIMES:
            for p2 in PRIMES:
                if p1 != p2:
                    # since primes are relatively prime, we can
                    # construct our own gcd and make sure the solution
                    # equals it
                    gcd = random.randint(2, pow(10, 4))
                    expr = LinearExpression(p1 * gcd, p2 * gcd)
                    solution = expr.solve(gcd)
                    self.assertEqual(
                        gcd,
                        solution.evaluate()
                    )
