from fermat.cryptography import EncryptionDevice


class AESAlgorithm(EncryptionDevice):
    """
    Encryption device that uses the Advanced Encryption Standard.
    """
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
