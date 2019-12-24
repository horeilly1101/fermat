from rsa.random_prime_generator import RandomPrimeGenerator
from rsa import utils


class EncryptionDevice:
    def encrypt(self, message):
        pass

    def decrypt(self, message):
        pass


class AsciiSerializer:
    @staticmethod
    def convert_to_ascii(character):
        number = ord(character)
        assert 0 <= number <= 127
        return number

    @staticmethod
    def convert_to_character(number):
        assert 0 <= number <= 127
        return chr(number)

    @staticmethod
    def serialize(message):
        return sum([
            pow(2, 7 * i) * AsciiSerializer.convert_to_ascii(char)
            for i, char in enumerate(message)
        ])

    @staticmethod
    def deserialize(number):
        message = ""
        remaining_number = number

        while remaining_number > 1:
            remainder = remaining_number % pow(2, 7)
            message += AsciiSerializer.convert_to_character(remainder)
            remaining_number //= pow(2, 7)

        return message


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
    def __init__(self):
        prime_generator = RandomPrimeGenerator()
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
