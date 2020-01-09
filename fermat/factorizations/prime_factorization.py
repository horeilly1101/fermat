import collections
import functools
import math
from typing import List
import itertools

from fermat.factorizations.factorization import Factorization
from fermat import utils


class PrimeFactorization(Factorization):
    def __init__(self, prime_factors):
        self.prime_factors = prime_factors

    def __eq__(self, other):
        if not isinstance(other, PrimeFactorization):
            return False

        return self.prime_factors == other.prime_factors

    def __hash__(self):
        return hash(self.prime_factors)

    def __str__(self):
        return " * ".join(
            f"{prime}^{exponent}"
            for prime, exponent in self.prime_factors.items()
        )

    def __repr__(self):
        return str(self)

    def compute_product(self):
        """
        :return: the positive integer represented by the prime
            factorization.
        """
        return functools.reduce(
            lambda result, num: result * pow(num, self.get_exponent(num)),
            self.prime_factors,
            1
        )

    def get_divisors(self):
        primes = self.get_distinct_prime_factors()
        exponent_combinations = itertools.product(*[
            range(self.get_exponent(prime) + 1)
            for prime in primes
        ])

        for exponents in exponent_combinations:
            yield utils.multiply(
                pow(prime, exponent)
                for prime, exponent in zip(primes, exponents)
            )

    def get_exponent(self, prime):
        if prime in self.prime_factors:
            return self.prime_factors[prime]

        return 0

    def get_distinct_prime_factors(self) -> List[int]:
        return list(self.prime_factors.keys())

    @staticmethod
    @functools.lru_cache()
    def factor(num: int) -> "PrimeFactorization":
        # ------------------------
        # Algorithm: out-of-the-box sieve of Eratosthenes
        # ------------------------

        # create list of prime numbers <= num
        prime_candidates: list = [j for j in range(2, num + 1)]

        for i in range(2, math.ceil(math.sqrt(num))):
            # check if i is composite
            if prime_candidates[i - 2] is None:
                continue

            for multiple in range(2, num // i + 1):
                prime_candidates[i * multiple - 2] = None

        # filter out None values
        sieve = [value for value in prime_candidates if value is not None]

        # count up the prime factors
        prime_factors = collections.Counter()
        num_remaining = num
        for prime in sieve:
            if num_remaining == 1:
                break

            while num_remaining % prime == 0:
                prime_factors[prime] += 1
                num_remaining //= prime

        return PrimeFactorization(prime_factors)

    @staticmethod
    def of(*primes: int) -> "PrimeFactorization":
        counter = collections.Counter()
        for prime in primes:
            counter[prime] += 1
        return PrimeFactorization(counter)
