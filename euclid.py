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
        pass
