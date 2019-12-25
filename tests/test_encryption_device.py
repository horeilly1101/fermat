import unittest
from rsa.encryption_device import RSAAlgorithm


class TestEncryptionDevice(unittest.TestCase):
    def test_rsa_algorithm(self):
        messages = [
            "hi", "password", ". . . #$% !", "0123456789"
        ]

        for message in messages:
            rsa = RSAAlgorithm()
            self.assertEqual(
                message,
                rsa.decrypt(rsa.encrypt(message))
            )
