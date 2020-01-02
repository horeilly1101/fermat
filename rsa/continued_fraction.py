import math
from abc import ABC, abstractmethod
from rsa import utils


class ContinuedFraction:
    def get_convergent(self, n: int):
        pass


class Expression(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass

    @abstractmethod
    def get_constant(self) -> "Number":
        pass

    @abstractmethod
    def is_zero(self) -> bool:
        pass

    def floor(self):
        return math.floor(self.evaluate())

    def simplify(self) -> "Expression":
        return self


class Sum(Expression):
    def __init__(self, num: "Number", irrational: "Irrational"):
        self.num = num
        self.irrational = irrational

    def __eq__(self, other):
        if not isinstance(other, Sum):
            return False

        return (
            self.num == other.num
            and self.irrational == other.irrational
        )

    def __hash__(self):
        return hash(self.num) + hash(self.irrational)

    def evaluate(self) -> float:
        return self.num.evaluate() + self.irrational.evaluate()

    def get_constant(self) -> "Number":
        value = utils.gcd(
            self.num.value,
            self.irrational.get_constant().value
        )
        return Number(value)

    def is_zero(self) -> bool:
        return self.num.is_zero() and self.irrational.is_zero()

    def simplify(self) -> "Expression":
        if self.is_zero():
            return Number(0)


class Fraction(Expression):
    def __init__(self, num: Expression, denom: Expression):
        self._num = num
        self._denom = denom

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False

        return (
            self._num == other._num
            and self._denom == other._denom
        )

    def __hash__(self):
        return hash(self._num) + hash(self._denom)

    def evaluate(self) -> float:
        return self._num.evaluate() / self._denom.evaluate()

    def get_constant(self) -> "Number":
        value = utils.gcd(
            self._num.get_constant().value,
            self._denom.get_constant().value
        )
        return Number(value)


class Number(Expression):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Number):
            return False

        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def evaluate(self) -> float:
        return self.value

    def get_constant(self) -> "Number":
        return self


class Irrational(Expression):
    def __init__(self, value, constant):
        self.value = value
        self.constant = constant

    def __eq__(self, other):
        if not isinstance(other, Irrational):
            return False

        return (
            self.value == other.value
            and self.constant == other.constant
        )

    def __hash__(self):
        return hash(self.value) + hash(self.constant)

    def evaluate(self) -> float:
        return self.value() * self.constant.evaluate()

    def get_constant(self) -> "Number":
        return self.constant


def compute_continued_fraction(irrational: Irrational):
    constants = []
    alphas = set()

    previous_constant = irrational.floor()
    previous_alpha = irrational

    while previous_alpha not in alphas:
        print(constants)
        print(alphas)
        constants.append(previous_constant)
        alphas.add(previous_alpha)

        previous_alpha = 1 / (previous_alpha - constants[-1])
        previous_constant = math.floor(previous_alpha)

    return constants


if __name__ == '__main__':
    print(compute_continued_fraction(lambda: math.sqrt(2)))
