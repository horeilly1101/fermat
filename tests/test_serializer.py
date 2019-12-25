import unittest
from rsa.serializer import AsciiSerializer


class TestSerializer(unittest.TestCase):
    def test_ascii_serializer(self):
        messages = [
            "hi", "aloha", "yo!", ". . 0"
        ]
        serializer = AsciiSerializer()

        for message in messages:
            self.assertEqual(
                message,
                serializer.deserialize(serializer.serialize(message))
            )
