from rsa.diophantine_expressions.diophantine_expression import DiophantineExpression, \
    DiophantineSolution
from rsa.continued_fractions import PeriodicContinuedFraction


class PellLikeSolution(DiophantineSolution):
    def __init__(self, expression, x, y):
        super().__init__(expression)
        self.x = x
        self.y = y


class PellLikeExpression(DiophantineExpression):
    def __init__(self, d: int):
        self.d = d

    def evaluate(self, solution: PellLikeSolution) -> int:
        return pow(solution.x, 2) - self.d * pow(solution.y, 2)

    def solution_exists(self, value: int) -> bool:
        return value == 1

    def solve(self, value: int) -> PellLikeSolution:
        assert value == 1

        continued_fraction = PeriodicContinuedFraction.make_for_square_root(self.d)
        if continued_fraction.period_length % 2 == 0:
            convergent = continued_fraction.get_convergent(
                continued_fraction.period_length - 1
            )
        else:
            convergent = continued_fraction.get_convergent(
                2 * continued_fraction.period_length - 1
            )

        return PellLikeSolution(self, convergent.p, convergent.q)
