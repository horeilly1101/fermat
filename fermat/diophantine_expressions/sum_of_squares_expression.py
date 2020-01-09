import functools
from fermat.factorizations.prime_factorization import PrimeFactorization
from fermat.quadratic_reciprocity import get_quadratic_non_residue
from fermat.primality_testing import is_prime
from fermat.diophantine_expressions.diophantine_expression import DiophantineSolution, \
    DiophantineExpression


class SumOfSquaresSolution(DiophantineSolution):
    """
    Data structure that represents a sum of two squares
    of the form
        x^2 + y^2.
    """
    def __init__(self, expression: "SumOfSquaresExpression", x: int, y: int):
        super().__init__(expression)
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}^2 + {self.y}^2"

    def multiply(self, other: "SumOfSquaresSolution") -> "SumOfSquaresSolution":
        return SumOfSquaresSolution(
            self.expression,
            self.x * other.x + self.y * other.y,
            self.y * other.x - self.x * other.y
        )

    def multiply2(self, other: "SumOfSquaresSolution") -> "SumOfSquaresSolution":
        return SumOfSquaresSolution(
            self.expression,
            self.y * other.x + self.x * other.y,
            self.x * other.x - self.y * other.y
        )

    def raise_to_power(self, power: int) -> "SumOfSquaresSolution":
        return functools.reduce(
            lambda result, _: result.multiply(self),
            range(power - 1),
            self
        )

    def divide_out_root(self, root: int) -> "SumOfSquaresSolution":
        return SumOfSquaresSolution(
            self.expression,
            self.x // root,
            self.y // root
        )


class SumOfSquaresExpression(DiophantineExpression):
    def evaluate(self, solution: SumOfSquaresSolution) -> int:
        return pow(solution.x, 2) + pow(solution.y, 2)

    def get_mult_id(self) -> "SumOfSquaresSolution":
        return SumOfSquaresSolution(self, 1, 0)

    def solution_exists_for_pf(self, pf: PrimeFactorization) -> bool:
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

    def solution_exists(self, value: int) -> bool:
        """
        :param value: a positive integer
        :return: whether or not there exist positive integers a, b
            such that a^2 + b^2 = number
        """
        if is_prime(value) and value % 4 == 1:
            return True

        return self.solution_exists_for_pf(
            PrimeFactorization.factor(value)
        )

    @functools.lru_cache()  # cache repeated queries
    def _solve_for_prime(self, prime: int) -> "SumOfSquaresSolution":
        if prime == 2:
            return SumOfSquaresSolution(self, 1, 1)

        # find integers z, multiple such that
        #   z^2 + 1 = multiple * prime.
        # Justification can be found here:
        #   https://math.stackexchange.com/questions/5877
        non_residue = get_quadratic_non_residue(prime)
        z = pow(non_residue, (prime - 1) // 4, prime)
        multiple = (pow(z, 2) + 1) // prime
        assert pow(z, 2) + 1 == multiple * prime

        # Perform Fermat's Descent Procedure
        descent_sum_of_squares = SumOfSquaresSolution(self, z, 1)

        while multiple > 1:
            # find integers u and v such that
            # u^2 + v^2 = descent_sum_of_squares.a^2 + descent_sum_of_squares.b^2 mod multiple
            u = descent_sum_of_squares.x % multiple
            v = descent_sum_of_squares.y % multiple

            # make sure u and v are in the interval
            # (- multiple / 2, multiple / 2)
            if u > multiple / 2:
                u -= multiple
            if v > multiple / 2:
                v -= multiple

            new_multiple = (pow(u, 2) + pow(v, 2)) // multiple
            new_sum_of_squares = SumOfSquaresSolution(self, u, v)

            descent_sum_of_squares = (
                descent_sum_of_squares
                .multiply(new_sum_of_squares)
                .divide_out_root(multiple)
            )
            multiple = new_multiple

        return descent_sum_of_squares

    def _solve_for_prime_power(self, prime, exponent):
        if exponent % 2 == 0 and prime % 4 != 1:
            return SumOfSquaresSolution(
                self,
                pow(prime, exponent // 2),
                0
            )

        return self._solve_for_prime(prime).raise_to_power(exponent)

    def solve_for_pf(self, pf: PrimeFactorization) -> "SumOfSquaresSolution":
        return functools.reduce(
            lambda result, prime: result.multiply(
                self._solve_for_prime_power(prime, pf.get_exponent(prime))
            ),
            pf.get_distinct_prime_factors(),
            self.get_mult_id()
        )

    def solve(self, value: int) -> "SumOfSquaresSolution":
        return self.solve_for_pf(
            PrimeFactorization.factor(value)
        )
