from abc import ABC, abstractmethod


class DiophantineSolution(ABC):
    def __init__(self, equation: "DiophantineExpression"):
        self.equation = equation

    def evaluate(self):
        return self.equation.evaluate(self)


class DiophantineExpression(ABC):
    @abstractmethod
    def solution_exists(self, value: int) -> bool:
        pass

    @abstractmethod
    def solve(self, value: int) -> DiophantineSolution:
        pass

    @abstractmethod
    def evaluate(self, solution: DiophantineSolution):
        pass
