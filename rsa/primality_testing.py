"""
File that contains various utility methods for primality testing.
"""
from rsa.factorizations.even_factorization import EvenFactorization


def _is_witness(possible_prime: int, witness_candidate: int) -> bool:
    """
    Compute whether or not a number is a Rabin-Miller witness for a
    possible prime. If the number is a Rabin-Miller witness, then the
    possible prime must be composite. Otherwise, the test is inconclusive.

    :param possible_prime: possible prime
    :param witness_candidate: possible witness
    :return: whether or not the witness candidate is a witness for the
        possible prime
    """
    # the witness candidate can't be divisible by the possible prime
    assert witness_candidate % possible_prime != 0

    even_factorization = EvenFactorization.factor(possible_prime - 1)

    if pow(witness_candidate, even_factorization.base, possible_prime) == 1:
        return False

    for i in range(even_factorization.two_power + 1):
        exponent = even_factorization.base * pow(2, i)
        if pow(witness_candidate, exponent, possible_prime) == possible_prime - 1:
            return False

    return True


def is_prime(num: int) -> bool:
    """
    Compute whether an input positive integer is prime.
    :param num: positive integer
    :return: whether or not num is prime
    """
    # prime-ness only makes sense for positive integers
    assert num > 0

    # handle a few small cases
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:  # if num is even
        return False

    # perform Rabin-Miller test for composite numbers
    for witness_candidate in range(2, min(num, 52)):  # check up to 100 witnesses
        if _is_witness(num, witness_candidate):
            return False

    return True
