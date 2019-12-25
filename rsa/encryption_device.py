from rsa.random_prime_generator import RandomPrimeGenerator
from rsa import utils
from rsa.serializer import AsciiSerializer


class EncryptionDevice:
    def encrypt(self, message):
        pass

    def decrypt(self, message):
        pass


class AESAlgorithm(EncryptionDevice):
    def __init__(self, key):
        self._key = key

    @staticmethod
    def convert_message_to_matrix(message):
        matrices: list = []
        for i, char in enumerate(message):
            matrix_num, position = divmod(i, 16)

            if position == 0:
                matrices.append(
                    [[32 for _ in range(4)] for _ in range(4)]
                )

            j, i = divmod(position, 4)
            matrices[matrix_num][i][j] = ord(char)
        return matrices

    def encrypt(self, message):
        pass

    def decrypt(self, message):
        pass


class RSAAlgorithm(EncryptionDevice):
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
            utils.euler_totient(p, q)
        )

    def encrypt(self, message):
        serialized_message = AsciiSerializer.serialize(message)
        assert self.modulus > serialized_message
        return pow(serialized_message, self.public_key, self.modulus)

    def decrypt(self, message):
        decrypted_message = pow(message, self.private_key, self.modulus)
        return AsciiSerializer.deserialize(decrypted_message)
