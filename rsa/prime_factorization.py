from functools import reduce
import math
import collections


class PrimeFactorization:
    def __init__(self, prime_factors):
        self.prime_factors = prime_factors

    def __eq__(self, other):
        if not isinstance(other, PrimeFactorization):
            return False

        return self.prime_factors == other.prime_factors

    def __hash__(self):
        return hash(self.prime_factors)

    def __str__(self):
        return f"PrimeFactorization({self.prime_factors})"

    def __repr__(self):
        return str(self)

    def compute_product(self):
        return reduce(
            lambda result, num: result * pow(num, self.prime_factors[num]),
            self.prime_factors,
            1
        )

    @staticmethod
    def factor(num) -> "PrimeFactorization":
        # create list of prime numbers <= num
        prime_candidates: list = [j for j in range(2, num + 1)]
        for i in range(2, math.ceil(math.sqrt(num))):
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
