import random
from random_prime_generator import RandomPrimeGenerator
from ld_expression import LDExpression


class RSAAlgorithm:
    @staticmethod
    def compute_modular_inverse(x, modulus):
        return LDExpression(x, -1 * modulus).get_solution_to_gcd().x

    def __init__(self):
        prime_generator = RandomPrimeGenerator()
        p = prime_generator.generate()
        q = prime_generator.generate()

        self.modulus = p * q
        self.public_key = prime_generator.generate()
        self.private_key = RSAAlgorithm.compute_modular_inverse(
            self.public_key, (p-1) * (q-1)
        )

    def encrypt(self, message):
        return pow(message, self.public_key, self.modulus)

    def decrypt(self, message):
        return pow(message, self.private_key, self.modulus)


if __name__ == "__main__":
    algo = RSAAlgorithm()
    print(algo.public_key)
    print(algo.private_key)
    message = 56
    e = algo.encrypt(message)
    print(e)
    print(algo.decrypt(e))
