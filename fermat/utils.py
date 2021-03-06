"""
File that contains various utility functions.
"""
import functools
from typing import List, Iterator, Iterable
from fermat.diophantine_expressions.linear_expression import LinearExpression


def compute_modular_inverse(a: int, modulus: int) -> int:
    """
    Function to find a's inverse mod the modulus. i.e.
    compute a positive x such that ax = 1 mod modulus.
    """
    equation = LinearExpression(a, modulus)
    # if gcd(a, modulus) != 1, then a modular inverse
    # doesn't exist
    assert equation.solution_exists(1)

    solution = (
        equation
        # solve ax + modulus * y = 1
        .solve(1)
        .make_x_positive()
    )

    return solution.x


def gcd(a: int, b: int) -> int:
    """
    Return the greatest common divisor of a and b.
    """
    # Compute using Euclid's algorithm
    if a == 0:
        return abs(b)

    if b == 0:
        return abs(a)

    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    """
    Return the least common multiple of a and b.
    """
    # it's not hard to prove that:
    #   lcm(a, b) * gcd(a, b) = a * b
    return a * b // gcd(a, b)


def product(factors: Iterable[int]) -> int:
    return functools.reduce(
        lambda result, num: result * num,
        factors,
        1
    )


def get_divisors(num: int) -> List[int]:
    return [
        i for i in range(1, num + 1)
        if num % i == 0
    ]


def get_divisors_generator(num: int) -> Iterator[int]:
    for divisor_candidate in range(1, num + 1):
        if num % divisor_candidate == 0:
            yield divisor_candidate
