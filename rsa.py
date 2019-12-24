from random_prime_generator import RandomPrimeGenerator
import utils


class EncryptionDevice:
    def encrypt(self, message):
        pass

    def decrypt(self, message):
        pass


class CaesarCipher(EncryptionDevice):
    def __init__(self, shift):
        self._shift = shift

    def encrypt(self, message):
        return "".join(char + self._shift for char in message)

    def decrypt(self, message):
        return "".join(char - self._shift for char in message)


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
