from numbers.arithmetic_functions.arithmetic_function import ArithmeticFunction
from numbers import utils


class SigmaKFunction(ArithmeticFunction):
    def __init__(self, k: int):
        self._k = k

    def evaluate(self, num: int):
        return sum([
            pow(divisor, self._k)
            for divisor in utils.get_divisors(num)
        ])


class SigmaFunction(SigmaKFunction):
    def __init__(self):
        super().__init__(1)


class DivisorFunction(SigmaKFunction):
    def __init__(self):
        super().__init__(0)

    def evaluate(self, num: int):
        # optimize this case
        return len(utils.get_divisors(num))
