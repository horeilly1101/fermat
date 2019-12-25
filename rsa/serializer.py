"""
File that contains serializers to convert between strings and numbers.
"""


class Serializer:
    """
    An object that can convert between strings and numbers.
    """
    def serialize(self, message):
        pass

    def deserialize(self, number):
        pass


class AsciiSerializer(Serializer):
    """
    A serializer that deals with strings of ASCII characters.
    """
    @staticmethod
    def convert_to_ascii(character):
        number = ord(character)
        assert 0 <= number <= 127
        return number

    @staticmethod
    def convert_to_character(number):
        assert 0 <= number <= 127
        return chr(number)

    def serialize(self, message):
        return sum([
            pow(2, 7 * i) * AsciiSerializer.convert_to_ascii(char)
            for i, char in enumerate(message)
        ])

    def deserialize(self, number):
        message = ""
        remaining_number = number

        while remaining_number > 1:
            remainder = remaining_number % pow(2, 7)
            message += AsciiSerializer.convert_to_character(remainder)
            remaining_number //= pow(2, 7)

        return message
