from fermat.diophantine_expressions.diophantine_expression import DiophantineExpression, \
    DiophantineSolution


class LinearSolution(DiophantineSolution):
    """
    This is a solution to a Linear Diophantine expression of
    the form
        ax + by,
    where x and y are integer variables.

    Note that if ax + by = g for some integer g, then there
    are infinitely many solutions x,y. You can compute any
    of the other solutions with a linear shift.
    """
    def __init__(self, expression: "LinearExpression", x: int, y: int):
        super().__init__(expression)
        self.x = x
        self.y = y

    def shift(self, k: int) -> "LinearSolution":
        value = self.evaluate()
        return self.expression.make_solution(
            self.x + k * (self.expression.b // value),
            self.y - k * (self.expression.a // value)
        )

    def make_x_positive(self) -> "LinearSolution":
        if self.x > 0:
            return self

        return self.shift(1)


class LinearExpression(DiophantineExpression):
    """
    Class that represents a linear diophantine expression of
    the form
        ax + by = c,
    where x and y are integer variables.
    """
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"{self.a}x + {self.b}y"

    def __repr__(self) -> str:
        return str(self)

    def solution_exists(self, value: int) -> bool:
        from fermat import utils
        return value % utils.gcd(self.a, self.b) == 0

    def solve(self, value: int) -> LinearSolution:
        from fermat import utils

        multiple = value // utils.gcd(self.a, self.b)
        gcd_solution = self.solve_for_gcd()
        solution = LinearSolution(
            self,
            multiple * gcd_solution.x,
            multiple * gcd_solution.y
        )

        assert solution.evaluate() == value
        return solution

    def evaluate(self, solution: LinearSolution) -> int:
        return self.a * solution.x + self.b * solution.y

    def make_solution(self, x: int, y: int) -> LinearSolution:
        return LinearSolution(self, x, y)

    def solve_for_gcd(self) -> LinearSolution:
        """
        Compute a solution the the LDExpression that evaluates to
        the greatest common divisor of a and b. This is computed
        using Euclid's Extended Algorithm.

        e.g. find integers x,y such that
            ax + by = gcd(a, b)

        :return: LDSolution
        """
        # set initial conditions
        prev_solution = self.make_solution(1, 0)
        solution = self.make_solution(0, 1)

        while prev_solution.evaluate() % solution.evaluate():
            multiple = prev_solution.evaluate() // solution.evaluate()

            # update the stored solutions
            prev_solution, solution = (
                solution,
                self.make_solution(
                    prev_solution.x - multiple * solution.x,
                    prev_solution.y - multiple * solution.y
                )
            )

        return solution
