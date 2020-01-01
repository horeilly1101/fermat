from rsa.arithmetic_functions.arithmetic_function import ArithmeticFunction


class DeltaFunction(ArithmeticFunction):
    def evaluate(self, num: int):
        if num == 1:
            return 1

        return 0
