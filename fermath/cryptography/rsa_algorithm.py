from fermath import utils
from fermath.arithmetic_functions import phi
from fermath.cryptography import EncryptionDevice
from fermath.random_prime_generator import RandomPrimeGenerator


class RSAAlgorithm(EncryptionDevice):
    """
    Encryption device that uses the RSA algorithm.
    """
    def __init__(self, min_bits=0, max_bits=64):
        prime_generator = RandomPrimeGenerator(min_bits, max_bits)
        p = prime_generator.generate()
        q = prime_generator.generate()

        self.modulus = p * q
        self.public_key = prime_generator.generate()

        # solve for the modular inverse of the public key mod phi(pq),
        # where phi is the euler totient function
        self.private_key = utils.compute_modular_inverse(
            self.public_key,
            phi.evaluate_from_primes(p, q)
        )

    def encrypt(self, message):
        assert self.modulus > message
        return pow(message, self.public_key, self.modulus)

    def decrypt(self, message):
        return pow(message, self.private_key, self.modulus)
