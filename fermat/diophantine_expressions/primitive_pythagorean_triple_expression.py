import math

from fermat.diophantine_expressions.diophantine_expression import DiophantineExpression, \
    DiophantineSolution
from fermat.diophantine_expressions.sum_of_squares_expression import SumOfSquaresExpression


class PPTSolution(DiophantineSolution):
    def __init__(self, expression: "PPTExpression", a: int, b: int):
        super().__init__(expression)
        self.a = a
        self.b = b


class PPTExpression(DiophantineExpression):
    def __init__(self):
        self.sos = SumOfSquaresExpression()

    def evaluate(self, solution: PPTSolution) -> int:
        return int(math.sqrt(pow(solution.a, 2) + pow(solution.b, 2)))

    def solution_exists(self, value: int) -> bool:
        return self.sos.solution_exists(2 * value)

    def solve(self, value: int) -> PPTSolution:
        sos_solution = self.sos.solve(2 * value)
        return PPTSolution(
            self,
            sos_solution.x,
            sos_solution.y
        )
