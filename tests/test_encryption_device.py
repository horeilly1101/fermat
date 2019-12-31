import unittest
from rsa.cryptography.rsa_algorithm import RSAAlgorithm
from tests import testing_utils


class TestEncryptionDevice(unittest.TestCase):
    def test_rsa_algorithm(self):
        for message in testing_utils.PRIMES + testing_utils.NON_PRIMES:
            rsa = RSAAlgorithm()
            self.assertEqual(
                message,
                rsa.decrypt(rsa.encrypt(message))
            )
