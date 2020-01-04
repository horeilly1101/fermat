from functools import reduce

from numbers.arithmetic_functions.arithmetic_function import ArithmeticFunction
from numbers.factorizations.prime_factorization import PrimeFactorization


class EulerTotientFunction(ArithmeticFunction):
    def evaluate(self, num: int):
        return self.evaluate_from_prime_factorization(
            PrimeFactorization.factor(num)
        )

    def evaluate_from_prime_factorization(self, pf: PrimeFactorization):
        def evaluate_from_prime_power(prime):
            return (
                pow(prime, pf.get_exponent(prime))
                - pow(prime, pf.get_exponent(prime) - 1)
            )

        return reduce(
            lambda result, prime: result * evaluate_from_prime_power(prime),
            pf.get_distinct_prime_factors(),
            1
        )
