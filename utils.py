from ld_expression import LDExpression
from functools import reduce


def compute_modular_inverse(a, modulus):
    """
    Function to find a's inverse mod the modulus. i.e.
    compute a positive x such that ax = 1 mod modulus.
    """
    return (
        LDExpression(a, modulus)
        # solve ax + modulus * y = gcd(a, modulus)
        .get_solution_to_gcd()
        .make_x_positive()
        .x
    )


def euler_totient(*distinct_primes):
    return reduce(
        lambda result, prime: result * (prime - 1),
        distinct_primes,
        1
    )
