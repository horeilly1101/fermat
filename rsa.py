import random


# class RSAAlgorithm:
#     def __init__(self, p, q, k):
#         self._p = p
#         self._q = q
#         self._k = k
#
#     def encrypt(self, message):
#         return pow(
#             message,
#             self._k,
#             self._p * self._q
#         )


class EncryptionDevice:
    def encrypt(self, message):
        pass


class DecryptionDevice:
    def decrypt(self, message):
        pass



def encrypt(message, public_key, pq):
    return pow(message, public_key, pq)


def decrypt(encrypted_message, mult_id, pq):
    return pow(encrypted_message, mult_id, pq)


def compute_inverse(p, q):
    if q == 0:
        return p
    if p == 0:
        return q
    return compute_inverse(q, p % q)


def convert_string_to_int_list(string):
    ints = []



if __name__ == "__main__":
    m = 123
    e = encrypt(123, 17, 3233)
    print(e)
    print(decrypt(e, 2753, 3233))
    print(compute_inverse(7, 28))
