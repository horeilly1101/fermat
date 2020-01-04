from fermat.arithmetic_functions.arithmetic_function import ArithmeticFunction
from fermat.factorizations.prime_factorization import PrimeFactorization


class UnitFunction(ArithmeticFunction):
    def evaluate(self, num: int):
        return 1

    def evaluate_from_prime_factorization(self, pf: PrimeFactorization):
        return 1

    def evaluate_from_primes(self, *distinct_primes):
        return 1
