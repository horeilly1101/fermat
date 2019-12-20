"""Example testing suite."""
import unittest
from primality_testing import is_prime
from ld_expression import LDExpression
from rsa import RSAAlgorithm
import random


PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 23, 31, 101, 137, 151,
    979982749, 979910219, 980414927, 961768781
]

NON_PRIMES = [
    1, 4, 6, 8, 9, 10, 12, 14, 15, 123, 155, 201,
    961770273, 961832591, 961872727, 961949947
]


class TestPrimalityTesting(unittest.TestCase):
    def test_primes(self):
        for prime in PRIMES:
            self.assertTrue(is_prime(prime))

    def test_non_primes(self):
        for non_prime in NON_PRIMES:
            self.assertFalse(is_prime(non_prime))


class TestLDExpression(unittest.TestCase):
    def test_gcd_primes(self):
        for p1 in PRIMES:
            for p2 in PRIMES:
                if p1 != p2:
                    # since primes are relatively prime, we expect
                    # their gcd to be 1, and we expect the generated
                    # solution to equal 1
                    expr = LDExpression(p1, p2)
                    solution = expr.get_solution_to_gcd()
                    self.assertEqual(
                        1,
                        expr.evaluate(solution)
                    )

    def test_gcd_composites(self):
        for p1 in PRIMES:
            for p2 in PRIMES:
                if p1 != p2:
                    # since primes are relatively prime, we can
                    # construct our own gcd and make sure the solution
                    # equals it
                    gcd = random.randint(2, pow(10, 4))
                    expr = LDExpression(p1 * gcd, p2 * gcd)
                    solution = expr.get_solution_to_gcd()
                    self.assertEqual(
                        gcd,
                        expr.evaluate(solution)
                    )


class TestRSAAlgorithm(unittest.TestCase):
    def test_modular_inverse(self):
        for p1 in PRIMES:
            for p2 in PRIMES:
                if p1 != p2:
                    inv = RSAAlgorithm.compute_modular_inverse(p1, p2)
                    self.assertEqual(
                        1,
                        (p1 * inv) % p2
                    )

    def test_rsa_algorithm(self):
        for message in PRIMES + NON_PRIMES:
            rsa = RSAAlgorithm()
            self.assertEqual(
                message,
                rsa.decrypt(rsa.encrypt(message))
            )
