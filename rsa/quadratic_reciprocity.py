from rsa.utils import EvenFactorization


def compute_jacobi_symbol(x, modulus):
    if x == 0:
        return 0

    if not 0 < x < modulus:
        return compute_jacobi_symbol(
            x % modulus, modulus
        )

    if x == 1:
        return 1

    if x == 2:
        if modulus % 8 == 1 or modulus % 8 == 7:
            return 1
        return -1

    # divide out the largest even factor
    even_factorization = EvenFactorization.factor(x)

    if even_factorization.two_power > 0:
        return (
            pow(compute_jacobi_symbol(2, modulus), even_factorization.two_power)
            * compute_jacobi_symbol(even_factorization.base, modulus)
        )

    if x == modulus - 1:
        if modulus % 4 == 1:
            return 1
        return -1

    if x % 4 == 1 or modulus % 4 == 1:
        return compute_jacobi_symbol(modulus, x)

    return -1 * compute_jacobi_symbol(modulus, x)
