import math
from typing import List, Iterator

from rsa.continued_fractions.expression import Number, IrrationalFraction, IrrationalSum


def cf_representation_generator(number: Number) -> Iterator[int]:
    # set initial conditions
    alpha = IrrationalFraction(
        IrrationalSum(number, 1, 0),
        IrrationalSum(number, 0, 1)
    )
    a = math.floor(number.evaluate())

    while True:
        yield a

        if alpha.evaluate() - a == 0:
            break

        # compute next alpha from recurrence
        alpha = IrrationalFraction(
            alpha.sum2,
            IrrationalSum(
                number,
                alpha.sum1.const1 - a * alpha.sum2.const1,
                alpha.sum1.const2 - a * alpha.sum2.const2
            )
        )
        try:
            a = math.floor(alpha.evaluate())
        except ZeroDivisionError:
            break


def periodic_cf_representation_generator(
    representation: List[int],
    repeat_idx: int
) -> Iterator[int]:

    current_idx = 0

    while True:
        yield representation[current_idx]

        current_idx += 1
        if current_idx >= len(representation):
            current_idx = repeat_idx
