from rsa.prime_factorization import PrimeFactorization
from functools import reduce


class SumOfSquares:
    def __init__(self, a: int, b: int, result: int):
        assert pow(a, 2) + pow(b, 2) == result

        self.a = a
        self.b = b
        self.result = result

    def combine(self, other: "SumOfSquares") -> "SumOfSquares":
        return SumOfSquares(
            self.a * other.a + self.b * other.b,
            self.b * other.a - self.a * other.b,
            self.result * other.result
        )

    def raise_to_power(self, power: int) -> "SumOfSquares":
        return reduce(
            lambda result, _: result.combine(self),
            range(power - 1),
            self
        )

    @staticmethod
    def _exists_from_prime_factorization(prime_factorization: PrimeFactorization) -> bool:
        return all(
            prime % 4 == 1 or prime == 2 or exponent % 2 == 0
            for prime, exponent in prime_factorization.prime_factors.items()
        )

    @staticmethod
    def exists(number: int) -> bool:
        return SumOfSquares._exists_from_prime_factorization(
            PrimeFactorization.factor(number)
        )

    @staticmethod
    def _make_from_prime(prime: int) -> "SumOfSquares":
        pass

    @staticmethod
    def _make_from_prime_factorization(prime_factorization: PrimeFactorization) -> "SumOfSquares":
        def raise_prime_to_power(prime):
            return (
                SumOfSquares
                ._make_from_prime(prime)
                .raise_to_power(prime_factorization.prime_factors[prime])
            )

        return reduce(
            lambda result, prime: result.combine(raise_prime_to_power(prime)),
            prime_factorization.prime_factors
        )

    @staticmethod
    def make(number: int) -> "SumOfSquares":
        return SumOfSquares._make_from_prime_factorization(
            PrimeFactorization.factor(number)
        )
