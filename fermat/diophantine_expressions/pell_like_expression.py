from fermat.diophantine_expressions.diophantine_expression import DiophantineExpression, \
    DiophantineSolution
from fermat.continued_fractions import PeriodicContinuedFraction


class PellLikeSolution(DiophantineSolution):
    def __init__(self, expression, x, y):
        super().__init__(expression)
        self.x = x
        self.y = y

    def __str__(self):
        return f"x={self.x} y={self.y} expression={self.expression}"


class PellLikeExpression(DiophantineExpression):
    def __init__(self, d: int):
        self.d = d

    def __str__(self):
        return f"x^2 - {self.d} * y^2"

    def evaluate(self, solution: PellLikeSolution) -> int:
        return pow(solution.x, 2) - self.d * pow(solution.y, 2)

    def solution_exists(self, value: int) -> bool:
        return value == 1

    def solve(self, value: int) -> PellLikeSolution:
        assert value == 1

        cf = PeriodicContinuedFraction.make_for_square_root(self.d)
        if cf.period_length % 2 == 0:
            convergent = cf.get_convergent(
                cf.period_length - 1
            )
        else:
            convergent = cf.get_convergent(
                2 * cf.period_length - 1
            )

        return PellLikeSolution(self, convergent.p, convergent.q)
