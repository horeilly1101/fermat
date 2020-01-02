from abc import ABC, abstractmethod


class DiophantineSolution(ABC):
    def __init__(self, equation: "DiophantineEquation"):
        self.equation = equation

    def evaluate(self):
        return self.equation.evaluate(self)


class DiophantineEquation(ABC):
    @abstractmethod
    def solution_exists(self) -> bool:
        pass

    @abstractmethod
    def solve(self) -> DiophantineSolution:
        pass

    @abstractmethod
    def evaluate(self, solution: DiophantineSolution):
        pass
