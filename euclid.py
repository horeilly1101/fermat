from typing import NamedTuple


class LDSolution(NamedTuple):
    x: int
    y: int


class LDExpression:
    """
    Class that represents a linear diophantine equation of
    the form
        ax + by,
    where x and y are integer variables. For uniformity,
    we maintain the invariant that a >= b.

    LD stands for Linear Diophantine.
    """
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def compute(self, solution: LDSolution):
        return self.a * solution.x + self.b * solution.y

    def get_solution_to_gcd(self):
        solution1 = LDSolution(1, 0)
        solution2 = LDSolution(0, 1)

        while self.compute(solution1) % self.compute(solution2):
            multiple = self.compute(solution1) // self.compute(solution2)

            solution1, solution2 = (
                solution2,
                LDSolution(solution1.x - multiple * solution2.x, solution1.y - multiple * solution2.y)
            )

        return solution2


if __name__ == "__main__":
    expr = LDExpression(19, 17)
    print(expr.get_solution_to_gcd())
