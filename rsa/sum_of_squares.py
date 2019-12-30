from rsa.prime_factorization import PrimeFactorization
from rsa.quadratic_reciprocity import get_quadratic_non_residue
from functools import reduce


class SumOfSquares:
    def __init__(self, a: int, b: int, result: int):
        assert pow(a, 2) + pow(b, 2) == result

        self.a = a
        self.b = b
        self.result = result

    def __str__(self):
        return f"SumOfSquares(a={self.a}, b={self.b}, result={self.result})"

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

    def divide_out_root(self, root):
        return SumOfSquares(
            self.a // root,
            self.b // root,
            self.result // pow(root, 2)
        )

    @staticmethod
    def get_multiplicative_inverse():
        return SumOfSquares(1, 0, 1)

    @staticmethod
    def exists_from_prime_factorization(prime_factorization: PrimeFactorization) -> bool:
        return all(
            prime % 4 == 1 or prime == 2 or exponent % 2 == 0
            for prime, exponent in prime_factorization.prime_factors.items()
        )

    @staticmethod
    def exists(number: int) -> bool:
        return SumOfSquares.exists_from_prime_factorization(
            PrimeFactorization.factor(number)
        )

    @staticmethod
    def _make_from_prime(prime: int) -> "SumOfSquares":
        print(prime)

        if prime == 2:
            return SumOfSquares(1, 1, 2)

        # find integers z, multiple such that
        #   z^2 + 1 = multiple * prime.
        # Justification can be found here:
        #   https://math.stackexchange.com/questions/5877/efficiently-finding-two-squares-which-sum-to-a-prime
        non_residue = get_quadratic_non_residue(prime)
        z = pow(non_residue, (prime - 1) // 4, prime)
        multiple = (pow(z, 2) + 1) // prime
        assert pow(z, 2) + 1 == multiple * prime

        # Perform Fermat's Descent Procedure
        descent_sum_of_squares = SumOfSquares(z, 1, multiple * prime)

        while multiple > 1:
            u = descent_sum_of_squares.a % multiple
            v = descent_sum_of_squares.b % multiple

            # make sure u and v are in the interval
            # (- multiple / 2, multiple / 2)
            if u > multiple / 2:
                u -= multiple
            if v > multiple / 2:
                v -= multiple

            new_multiple = (pow(u, 2) + pow(v, 2)) // multiple
            new_sum_of_squares = SumOfSquares(u, v, multiple * new_multiple)

            descent_sum_of_squares = (
                descent_sum_of_squares
                .combine(new_sum_of_squares)
                .divide_out_root(multiple)
            )
            multiple = new_multiple

        return descent_sum_of_squares

    @staticmethod
    def make_from_prime_factorization(prime_factorization: PrimeFactorization) -> "SumOfSquares":
        def raise_prime_to_power(prime):
            return (
                SumOfSquares
                ._make_from_prime(prime)
                .raise_to_power(prime_factorization.prime_factors[prime])
            )

        return reduce(
            lambda result, prime: result.combine(raise_prime_to_power(prime)),
            prime_factorization.prime_factors,
            SumOfSquares.get_multiplicative_inverse()
        )

    @staticmethod
    def make(number: int) -> "SumOfSquares":
        return SumOfSquares.make_from_prime_factorization(
            PrimeFactorization.factor(number)
        )
