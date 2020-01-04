from abc import ABC, abstractmethod


class DiophantineSolution(ABC):
    def __init__(self, expression: "DiophantineExpression"):
        self.expression = expression

    def evaluate(self) -> int:
        return self.expression.evaluate(self)


class DiophantineExpression(ABC):
    @abstractmethod
    def solution_exists(self, value: int) -> bool:
        pass

    @abstractmethod
    def solve(self, value: int) -> DiophantineSolution:
        pass

    @abstractmethod
    def evaluate(self, solution: DiophantineSolution) -> int:
        pass
