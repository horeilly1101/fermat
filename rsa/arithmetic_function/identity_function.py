from rsa.arithmetic_function.arithmetic_function import ArithmeticFunction


class IdentityFunction(ArithmeticFunction):
    def evaluate(self, num: int):
        return num
