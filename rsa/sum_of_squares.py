from rsa.factorizations.prime_factorization import PrimeFactorization
from rsa.quadratic_reciprocity import get_quadratic_non_residue
from rsa.primality_testing import is_prime
from functools import reduce


class SumOfSquares:
    """
    Data structure that represents a sum of two squares
    of the form
        a^2 + b^2 = result.
    """
    def __init__(self, a: int, b: int, result: int):
        assert pow(a, 2) + pow(b, 2) == result

        self.a = a
        self.b = b
        self.result = result

    def __str__(self):
        return f"SumOfSquares(a={self.a}, b={self.b}, result={self.result})"

    def multiply(self, other: "SumOfSquares") -> "SumOfSquares":
        return SumOfSquares(
            self.a * other.a + self.b * other.b,
            self.b * other.a - self.a * other.b,
            self.result * other.result
        )

    def raise_to_power(self, power: int) -> "SumOfSquares":
        return reduce(
            lambda result, _: result.multiply(self),
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
    def get_multiplicative_identity():
        return SumOfSquares(1, 0, 1)

    @staticmethod
    def exists_from_prime_factorization(pf: PrimeFactorization) -> bool:
        """
        :param pf: a prime factorization object
        :return: whether or not there exist positive integers a, b
            such that a^2 + b^2 = number
        """
        return all(
            prime % 4 == 1
            or prime == 2
            or pf.get_exponent(prime) % 2 == 0

            for prime in pf.get_distinct_prime_factors()
        )

    @staticmethod
    def exists(number: int) -> bool:
        """
        :param number: a positive integer
        :return: whether or not there exist positive integers a, b
            such that a^2 + b^2 = number
        """
        if is_prime(number) and number % 4 == 1:
            return True

        return SumOfSquares.exists_from_prime_factorization(
            PrimeFactorization.factor(number)
        )

    @staticmethod
    def _make_from_prime(prime: int) -> "SumOfSquares":
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
            # find integers u and v such that
            # u^2 + v^2 = descent_sum_of_squares.a^2 + descent_sum_of_squares.b^2 mod multiple
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
                .multiply(new_sum_of_squares)
                .divide_out_root(multiple)
            )
            multiple = new_multiple

        return descent_sum_of_squares

    @staticmethod
    def make_from_prime_factorization(pf: PrimeFactorization) -> "SumOfSquares":
        def make_from_prime_power(prime):
            exponent = pf.get_exponent(prime)

            if exponent % 2 == 0:
                return SumOfSquares(
                    pow(prime, exponent // 2),
                    0,
                    pow(prime, exponent)
                )

            return (
                SumOfSquares
                ._make_from_prime(prime)
                .raise_to_power(exponent)
            )

        return reduce(
            lambda result, prime: result.multiply(make_from_prime_power(prime)),
            pf.get_distinct_prime_factors(),
            SumOfSquares.get_multiplicative_identity()
        )

    @staticmethod
    def make(number: int) -> "SumOfSquares":
        return SumOfSquares.make_from_prime_factorization(
            PrimeFactorization.factor(number)
        )
