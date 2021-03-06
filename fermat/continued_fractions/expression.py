import math
from abc import ABC, abstractmethod
from fermat import utils


class Expression(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass

    def get_constant_factor(self) -> "Integer":
        return MULT_ID


class Number(Expression):
    def __init__(self, value_callable):
        self._value_callable = value_callable

    def __str__(self):
        return f"Number({self._value_callable()})"

    def evaluate(self) -> float:
        return self._value_callable()


class Integer(Number):
    def __init__(self, value: int):
        self.value = value
        super().__init__(lambda: value)

    def get_constant_factor(self) -> "Integer":
        return self


class SquareRoot(Number):
    def __init__(self, square: int):
        self.square = square
        super().__init__(lambda: math.sqrt(square))


class IrrationalSum(Expression):
    def __init__(self, number: Number, const1: int, const2: int):
        self._number = number
        self.const1 = const1
        self.const2 = const2

    def __str__(self):
        return f"{self.const1} * {self._number} + {self.const2}"

    def evaluate(self) -> float:
        return self.const1 * self._number.evaluate() + self.const2

    def get_constant_factor(self) -> "Integer":
        factor = utils.gcd(
            self.const1,
            self.const2
        )
        return Integer(factor)

    def divide_by(self, divisor: int) -> "IrrationalSum":
        return IrrationalSum(
            self._number,
            self.const1 // divisor,
            self.const2 // divisor
        )


class IrrationalFraction(Expression):
    def __init__(self, sum1: IrrationalSum, sum2: IrrationalSum):
        self.sum1 = sum1
        self.sum2 = sum2

    def __str__(self):
        return f"{self.sum1} / {self.sum2}"

    def evaluate(self) -> float:
        return self.sum1.evaluate() / self.sum2.evaluate()

    def get_constant_factor(self) -> "Integer":
        factor = utils.gcd(
            self.sum1.get_constant_factor().value,
            self.sum2.get_constant_factor().value
        )
        return Integer(factor)

    def simplify(self) -> "IrrationalFraction":
        factor = self.get_constant_factor()
        return IrrationalFraction(
            self.sum1.divide_by(factor.value),
            self.sum2.divide_by(factor.value)
        )


MULT_ID = Integer(1)
ADD_ID = Integer(0)
