from rsa.prime_factorization import PrimeFactorization


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

    @staticmethod
    def exists(prime_factorization: PrimeFactorization) -> bool:
        return all(
            prime % 4 == 1
            for prime, exponent in prime_factorization.prime_factors.items()
            if exponent % 2 == 1
        )

    @staticmethod
    def make_from_prime(prime: int):
        pass

    @staticmethod
    def make_from_prime_factorization(prime_factorization: PrimeFactorization) -> "SumOfSquares":
        return

    @staticmethod
    def make(number: int) -> "SumOfSquares":
        return SumOfSquares.make_from_prime_factorization(
            PrimeFactorization.factor(number)
        )


def find_sum_of_squares(p):
    pass
