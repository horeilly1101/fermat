import math


class ContinuedFraction:
    pass


class Fraction:
    pass


def compute_continued_fraction(callable):
    constants = []
    alphas = set()

    previous_constant = math.floor(callable())
    previous_alpha = callable()

    while previous_alpha not in alphas:
        print(constants)
        print(alphas)
        constants.append(previous_constant)
        alphas.add(previous_alpha)

        previous_alpha = 1 / (previous_alpha - constants[-1])
        previous_constant = math.floor(previous_alpha)

    return constants


if __name__ == '__main__':
    print(compute_continued_fraction(lambda: math.sqrt(2)))
