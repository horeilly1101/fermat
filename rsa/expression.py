from abc import ABC, abstractmethod
from typing import List, Callable
from functools import reduce


class Expression(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass

    def simplify(self) -> "Expression":
        return self

    def multiply(self, expr: "Expression") -> "Expression":
        i


class Add(Expression):
    def __init__(self, terms: List[Expression]):
        self._terms = terms

    def evaluate(self) -> float:
        return sum([
            term.evaluate()
            for term in self._terms
        ])


class Multiply(Expression):
    def __init__(self, factors: List[Expression]):
        self._factors = factors

    def evaluate(self) -> float:
        return reduce(
            lambda result, factor: result * factor.evaluate(),
            self._factors,
            1
        )


class Fraction(Expression):
    def __init__(self, num: Expression, denom: Expression):
        self._num = num
        self._denom = denom

    def evaluate(self) -> float:
        return self._num.evaluate() / self._denom.evaluate()


class Power(Expression):
    def __init__(self, base, exponent):
        self._base = base
        self._exponent = exponent

    def evaluate(self) -> float:
        return pow(self._base, self._exponent)


class Constant(Expression):
    def __init__(self, num: int):
        self._num = num

    def evaluate(self) -> float:
        return self._num


class Symbol(Expression):
    def __init__(self, symbol: str, value_callable: Callable[[], float]):
        self._symbol = symbol
        self._value_callable = value_callable

    def evaluate(self) -> float:
        return self._value_callable()
