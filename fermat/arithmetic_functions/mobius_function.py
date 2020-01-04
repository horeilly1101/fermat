from fermat.arithmetic_functions.arithmetic_function import ArithmeticFunction
from fermat.factorizations.prime_factorization import PrimeFactorization


class MobiusFunction(ArithmeticFunction):
    def evaluate(self, num: int):
        return self.evaluate_from_prime_factorization(
            PrimeFactorization.factor(num)
        )

    def evaluate_from_prime_factorization(self, pf: PrimeFactorization):
        if any(
            pf.get_exponent(prime) > 1
            for prime in pf.get_distinct_prime_factors()
        ):
            return 0

        num_distinct_prime_factors = len(pf.get_distinct_prime_factors())
        return pow(-1, num_distinct_prime_factors)
