import math
from typing import List

from rsa import utils
from rsa.continued_fractions.continued_fraction import ContinuedFraction
from rsa.continued_fractions.expression import IrrationalFraction, IrrationalSum, SquareRoot
from rsa.continued_fractions.generators import periodic_cf_representation_generator


class PeriodicContinuedFraction(ContinuedFraction):
    def __init__(self, representation: List[int], repeat_idx: int):
        self.representation = representation
        self.repeat_idx = repeat_idx
        self.period_length = len(representation) - repeat_idx

        factory = utils.GeneratorFactory(
            periodic_cf_representation_generator,
            representation=representation,
            repeat_idx=repeat_idx
        )
        super().__init__(factory)

    @staticmethod
    def make_for_square_root(square: int) -> "PeriodicContinuedFraction":
        constants = []

        # set initial conditions
        square_root = SquareRoot(square)

        alpha = IrrationalFraction(
            IrrationalSum(square_root, 1, 0),
            IrrationalSum(square_root, 0, 1)
        )
        a = math.floor(square_root.evaluate())

        constants.append(a)
        starting_a = a

        while a != 2 * starting_a:
            # compute next alpha from recurrence
            alpha = IrrationalFraction(
                IrrationalSum(
                    square_root,
                    alpha.sum2.const2 * alpha.sum1.const1,
                    -1 * alpha.sum2.const2 * (alpha.sum1.const2 - a * alpha.sum2.const2)
                ),
                IrrationalSum(
                    square_root,
                    0,
                    pow(alpha.sum1.const1, 2) * square_root.square
                    - pow(alpha.sum1.const2 - a * alpha.sum2.const2, 2)
                )
            ).simplify()
            a = math.floor(alpha.evaluate())
            constants.append(a)

        return PeriodicContinuedFraction(constants, repeat_idx=1)
