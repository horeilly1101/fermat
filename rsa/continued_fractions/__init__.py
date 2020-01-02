import math
from abc import ABC, abstractmethod
from mpmath import sqrt, pi, mp, e


class ContinuedFraction:
    def __init__(self, representation_generator):
        self.representation_generator = representation_generator

    def get_convergent(self, n: int):
        pass

    @staticmethod
    def make(num_callable):
        return ContinuedFraction(
            continued_fraction_generator(Number(num_callable))
        )


class PeriodicContinuedFraction(ContinuedFraction):
    def __init__(self, representation):
        self.representation = representation
        super().__init__(val for val in representation)

    def get_convergent(self, n: int):
        pass

    @staticmethod
    def make_from_square_root(square_root: "SquareRoot") -> "PeriodicContinuedFraction":
        constants = []
        alphas = set()

        # set initial conditions
        a = math.floor(square_root.evaluate())
        alpha = IrrationalFraction(
            IrrationalSum(irrational, 1, 0),
            IrrationalSum(irrational, 0, 1)
        )
        i = 0

        while alpha not in alphas:
            print(i)
            print(alpha)
            print(alpha.evaluate())
            print()
            constants.append(a)
            alphas.add(alpha)

            alpha = IrrationalFraction(
                IrrationalSum(
                    irrational,
                    alpha.sum2.const2 * alpha.sum1.const1,
                    -1 * alpha.sum2.const2 * (alpha.sum1.const2 - a * alpha.sum2.const2)
                ),
                IrrationalSum(
                    irrational,
                    0,
                    pow(alpha.sum1.const1, 2) * irrational.value - pow(alpha.sum1.const2 - a * alpha.sum2.const2, 2)
                )
            ).simplify()
            a = math.floor(alpha.evaluate())
            i += 1

        return constants


class Expression(ABC):
    @abstractmethod
    def evaluate(self) -> float:
        pass


class Number(Expression):
    def __init__(self, value_callable):
        self._value_callable = value_callable

    def __eq__(self, other):
        if not isinstance(other, Number):
            return False

        return self._value_callable() == other._value_callable()

    def __hash__(self):
        return hash(self._value_callable())

    def __repr__(self):
        return f"<Irrational value={self._value_callable()}>"

    def __str__(self):
        return f"Number({self._value_callable()})"

    def evaluate(self) -> float:
        return self._value_callable()


class SquareRoot(Number):
    def __init__(self, square: int):
        self.square = square
        super().__init__(lambda: math.sqrt(square))


class IrrationalSum(Expression):
    def __init__(self, irrational: Number, const1: int, const2: int):
        self._irrational = irrational
        self.const1 = const1
        self.const2 = const2

    def __eq__(self, other):
        if not isinstance(other, IrrationalSum):
            return False

        return (
            self._irrational == other._irrational
            and self.const1 == other.const1
            and self.const2 == other.const2
        )

    def __hash__(self):
        return hash(self._irrational) + hash(self.const1) + hash(self.const2)

    def __repr__(self):
        return f"<IrrationalSum irrational={self._irrational} const1={self.const1} const2={self.const2}>"

    def __str__(self):
        return f"{self.const1} * {self._irrational} + {self.const2}"

    def evaluate(self) -> float:
        return self.const1 * self._irrational.evaluate() + self.const2


class IrrationalFraction(Expression):
    def __init__(self, sum1: IrrationalSum, sum2: IrrationalSum):
        self.sum1 = sum1
        self.sum2 = sum2

    def __eq__(self, other):
        if not isinstance(other, IrrationalFraction):
            return False

        return (
            self.sum1 == other.sum1
            and self.sum2 == other.sum2
        )

    def __hash__(self):
        return hash(self.sum1) + hash(self.sum2)

    def __repr__(self):
        # return f"<IrrationalFraction sum1={self.sum1} sum2={self.sum2}>"
        return str(self)

    def __str__(self):
        return f"{self.sum1} / {self.sum2}"

    def evaluate(self) -> float:
        return self.sum1.evaluate() / self.sum2.evaluate()


def continued_fraction_generator(irrational):
    # set initial conditions
    alpha = IrrationalFraction(
        IrrationalSum(irrational, 1, 0),
        IrrationalSum(irrational, 0, 1)
    )
    a = math.floor(irrational.evaluate())

    while True:
        yield a

        if alpha.evaluate() - a == 0:
            break

        # compute next alpha from recurrence
        alpha = IrrationalFraction(
            alpha.sum2,
            IrrationalSum(
                irrational,
                alpha.sum1.const1 - a * alpha.sum2.const1,
                alpha.sum1.const2 - a * alpha.sum2.const2
            )
        )
        try:
            a = math.floor(alpha.evaluate())
        except ZeroDivisionError:
            break


if __name__ == '__main__':
    mp.prec = pow(10, 5)
    gen = continued_fraction_generator(Number(lambda: mp.e))
    for a in gen:
        print(a)
