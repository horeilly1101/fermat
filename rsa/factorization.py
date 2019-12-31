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
        """
        :return: the positive integer represented by the prime
            factorization.
        """
        return reduce(
            lambda result, num: result * pow(num, self.get_exponent(num)),
            self.prime_factors,
            1
        )

    def get_exponent(self, prime):
        if prime in self.prime_factors:
            return self.prime_factors[prime]

        return 0

    def get_distinct_prime_factors(self):
        return list(self.prime_factors.keys())

    @staticmethod
    def factor(num) -> "PrimeFactorization":
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