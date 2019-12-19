

class _EvenFactorization:
    """
    Class that represents an integer with the factors of 2
    divided out. It represents an integer n as
        n = self.base * (2 ^ self.two_power).
    """
    def __init__(self, base, two_power):
        self.base = base
        self.two_power = two_power

    def compute_product(self):
        """
        Multiply out the factorization.
        :return: product
        """
        return self.base * pow(2, self.two_power)

    @staticmethod
    def factor(num):
        """
        Compute a number's even factorization.
        :param num: input number
        :return: even factorization
        """
        base = num
        two_power = 0

        # divide out the greatest power of 2
        while base % 2 == 0:
            base //= 2
            two_power += 1

        return _EvenFactorization(base, two_power)


def is_prime(num):
    """
    Compute whether an input positive integer is prime.
    :param num: positive integer
    :return: whether or not num is prime
    """
    # prime-ness only makes sense for positive integers
    assert num > 0
    assert isinstance(num, int)

    # handle a couple small cases
    if num == 1:
        return False
    if num == 2:
        return True

    # perform Rabin-Miller test for composite numbers
    for witness_candidate in range(2, min(num, 102)):  # check up to 100 witnesses
        if is_witness(num, witness_candidate):
            return False

    return True


def is_witness(possible_prime, witness_candidate):
    even_factorization = _EvenFactorization.factor(possible_prime - 1)

    if pow(witness_candidate, even_factorization.base, possible_prime) == 1:
        return False

    for i in range(even_factorization.two_power + 1):
        exponent = even_factorization.base * pow(2, i)
        if pow(witness_candidate, exponent, possible_prime) == possible_prime - 1:
            return False

    return True


# class RandomPrimeGenerator:
#     def __init__(self, size):
#         self._size = size
#
#     def get_random
#
#     def get(self):
#         num = 0
#         for _ in range(self._size):
#             num += num * 10 + random.randint(0, 9)
