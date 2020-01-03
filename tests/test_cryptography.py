import unittest
from rsa.cryptography.rsa_algorithm import RSAAlgorithm
from tests import utils


class TestEncryptionDevice(unittest.TestCase):
    def test_rsa_algorithm(self):
        for message in utils.PRIMES:
            rsa = RSAAlgorithm(
                min_bits=15,
                max_bits=20
            )
            self.assertEqual(
                message,
                rsa.decrypt(rsa.encrypt(message))
            )
