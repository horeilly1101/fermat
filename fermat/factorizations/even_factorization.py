from fermat.factorizations.factorization import Factorization


class EvenFactorization(Factorization):
    """
    Class that represents an integer with the multiples of 2
    divided out. It represents an integer n as
        n = self.base * (k ^ self.two_power),
    with
        self.base = 1 mod 2.
    """
    def __init__(self, base: int, two_power: int):
        self.base = base
        self.two_power = two_power

    def compute_product(self) -> int:
        """
        Multiply out the factorization.
        :return: product
        """
        return self.base * pow(2, self.two_power)

    @staticmethod
    def factor(num: int) -> "EvenFactorization":
        """
        Compute a number's even factorization.
        """
        base = num
        two_power = 0

        # divide out the greatest power of k
        while base % 2 == 0:
            base //= 2
            two_power += 1

        return EvenFactorization(base, two_power)
