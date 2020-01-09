from abc import ABC, abstractmethod

from fermat import utils as utils
from fermat.factorizations.prime_factorization import PrimeFactorization


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

    def compute_dirichlet_product(self, af: "ArithmeticFunction") -> "ArithmeticFunction":
        original_function = self

        class DirichletProductFunction(ArithmeticFunction):
            def evaluate(self, num: int):
                return sum([
                    original_function.evaluate(divisor) * af.evaluate(num // divisor)
                    for divisor in utils.get_divisors(num)
                ])

            def evaluate_from_prime_factorization(self, pf: PrimeFactorization):
                num = pf.compute_product()
                return sum([
                    original_function.evaluate(divisor) * af.evaluate(num // divisor)
                    for divisor in pf.get_divisors()
                ])

        return DirichletProductFunction()
