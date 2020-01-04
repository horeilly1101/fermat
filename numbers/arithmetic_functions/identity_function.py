from numbers.arithmetic_functions.arithmetic_function import ArithmeticFunction


class IdentityFunction(ArithmeticFunction):
    def evaluate(self, num: int):
        return num
