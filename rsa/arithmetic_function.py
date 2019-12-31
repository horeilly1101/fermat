from abc import ABC, abstractmethod
from functools import reduce
from rsa.factorization import PrimeFactorization
import rsa.utils as utils


class ArithmeticFunction(ABC):
    @abstractmethod
    def evaluate(self, num: int):
        pass

    def evaluate_from_prime_factorization(self, pf: PrimeFactorization):
        return self.evaluate(pf.compute_product())

    def evaluate_from_primes(self, *distinct_primes):
        return self.evaluate_from_prime_factorization(
            PrimeFactorization.of(*distinct_primes)
        )

    def get_dirichlet_product(self, af: "ArithmeticFunction") -> "ArithmeticFunction":
        class DirichletProduct(ArithmeticFunction):
            def evaluate(self, num: int):
                return sum([
                    self.evaluate(divisor) * af.evaluate(num // divisor)
                    for divisor in utils.get_divisors(num)
                ])
        return DirichletProduct()


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
