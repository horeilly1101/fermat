import math

from fermat.diophantine_expressions.diophantine_expression import DiophantineExpression, \
    DiophantineSolution
from fermat.diophantine_expressions.sum_of_squares_expression import SumOfSquaresExpression
from fermat.factorizations import PrimeFactorization
from fermat import utils


class PPTSolution(DiophantineSolution):
    def __init__(self, expression: "PPTExpression", a: int, b: int):
        super().__init__(expression)
        self.a = a
        self.b = b

    def __str__(self):
        return f"sqrt({self.a}^2 + {self.b}^2)"


class PPTExpression(DiophantineExpression):
    def __init__(self):
        self.sos = SumOfSquaresExpression()

    def evaluate(self, solution: PPTSolution) -> int:
        return int(math.sqrt(pow(solution.a, 2) + pow(solution.b, 2)))

    def solution_exists_for_pf(self, pf: PrimeFactorization) -> bool:
        if any(
            prime % 4 != 1
            for prime in pf.get_distinct_prime_factors()
        ):
            return False

        sos_solution = self.sos.solve_for_pf(pf)
        return utils.gcd(sos_solution.x, sos_solution.y) == 1

    def solution_exists(self, value: int) -> bool:
        return self.solution_exists_for_pf(
            PrimeFactorization.factor(value)
        )

    def solve(self, value: int) -> PPTSolution:
        sos_solution = self.sos.solve(2 * value)
        assert utils.gcd(sos_solution.x, sos_solution.y) == 1

        min_var, max_var = sorted([
            abs(sos_solution.x), abs(sos_solution.y)
        ])

        return PPTSolution(
            self,
            max_var * min_var,
            (pow(max_var, 2) - pow(min_var, 2)) // 2
        )
