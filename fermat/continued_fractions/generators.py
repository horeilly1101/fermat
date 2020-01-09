import math
import itertools
from typing import List, Iterator

from fermat.continued_fractions.expression import Number, IrrationalFraction, IrrationalSum


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


def periodic_cf_representation_generator(representation: List[int], repeat_idx: int) -> Iterator[int]:
    for i, elem in enumerate(representation):
        if i >= repeat_idx:
            break

        yield elem

    yield from itertools.cycle(representation[repeat_idx:])
