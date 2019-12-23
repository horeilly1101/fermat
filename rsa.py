from random_prime_generator import RandomPrimeGenerator
from ld_expression import LDExpression


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
    @staticmethod
    def compute_modular_inverse(a, modulus):
        """
        Function to find a's inverse mod the modulus. i.e.
        compute a positive x such that ax = 1 mod modulus.
        """
        return (
            LDExpression(a, modulus)
            # solve ax + modulus * y = gcd(a, modulus)
            .get_solution_to_gcd()
            .make_x_positive()
            .x
        )

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
