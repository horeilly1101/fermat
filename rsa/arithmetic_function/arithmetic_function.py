from abc import ABC, abstractmethod

from rsa import utils as utils
from rsa.factorization import PrimeFactorization


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
        class DirichletProductFunction(ArithmeticFunction):
            def evaluate(self, num: int):
                return sum([
                    self.evaluate(divisor) * af.evaluate(num // divisor)
                    for divisor in utils.get_divisors(num)
                ])

            def evaluate_from_prime_factorization(self, pf: PrimeFactorization):
                pass

        return DirichletProductFunction()
