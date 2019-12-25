from rsa.ld_expression import LDExpression
from functools import reduce


def compute_modular_inverse(a, modulus):
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


def euler_totient(*distinct_prime_factors):
    return reduce(
        lambda result, prime: result * (prime - 1),
        distinct_prime_factors,
        1
    )
