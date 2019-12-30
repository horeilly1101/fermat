from functools import reduce


class PrimeFactorization:
    def __init__(self, prime_factors):
        self.prime_factors = prime_factors

    def compute_product(self):
        return reduce(
            lambda result, num: result * pow(num, self.prime_factors[num]),
            self.prime_factors,
            1
        )

    @staticmethod
    def factor(num) -> "PrimeFactorization":
        pass
