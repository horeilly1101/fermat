"""
File that contains various utility functions.
"""
from rsa.ld_expression import LDExpression
from functools import reduce


def compute_modular_inverse(a: int, modulus: int) -> int:
    """
    Function to find a's inverse mod the modulus. i.e.
    compute a positive x such that ax = 1 mod modulus.
    """
    solution = (
        LDExpression(a, modulus)
        # solve ax + modulus * y = gcd(a, modulus)
        .get_solution_to_gcd()
        .make_x_positive()
    )

    # if gcd(a, modulus) != 1, then a modular inverse
    # doesn't exist
    assert solution.evaluate() == 1
    return solution.x


def euler_totient(*distinct_prime_factors: int) -> int:
    """
    Function that computes the euler totient function of
    a number composed of distinct prime factors.

    If
        n = p_1 * p_2 * ... * p_n,
    and all prime factors are distinct, then
        phi(n) = (p_1 - 1)(p_2 - 1) ... (p_n - 1).
    """
    return reduce(
        lambda result, prime: result * (prime - 1),
        distinct_prime_factors,
        1
    )


def gcd(a: int, b: int) -> int:
    """
    Return the greatest common divisor of a and b.
    """
    # Compute using Euclid's algorithm
    if a == 0:
        return b

    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    """
    Return the least common multiple of a and b.
    """
    # it's not hard to prove that:
    #   lcm(a, b) * gcd(a, b) = a * b
    return a * b // gcd(a, b)


class EvenFactorization:
    """
    Class that represents an integer with the factors of 2
    divided out. It represents an integer n as
        n = self.base * (2 ^ self.two_power).
    """
    def __init__(self, base: int, two_power: int):
        self.base = base
        self.two_power = two_power

    def compute_product(self) -> int:
        """
        Multiply out the factorization.
        :return: product
        """
        return self.base * pow(2, self.two_power)

    @staticmethod
    def factor(num: int) -> "EvenFactorization":
        """
        Compute a number's even factorization.
        :param num: input number
        :return: even factorization
        """
        base = num
        two_power = 0

        # divide out the greatest power of 2
        while base % 2 == 0:
            base //= 2
            two_power += 1

        return EvenFactorization(base, two_power)
