import math
from typing import List

from rsa import utils
from rsa.continued_fractions import ContinuedFraction, IrrationalFraction, IrrationalSum
from rsa.continued_fractions.generators import periodic_cf_representation_generator


class PeriodicContinuedFraction(ContinuedFraction):
    def __init__(self, representation: List[int], repeat_idx):
        self.representation = representation
        self.repeat_idx = repeat_idx

        factory = utils.GeneratorFactory(
            periodic_cf_representation_generator,
            representation=representation,
            repeat_idx=repeat_idx
        )
        super().__init__(factory)

    @staticmethod
    def make_from_square_root(square_root: "SquareRoot") -> "PeriodicContinuedFraction":
        constants = []
        alphas = set()

        # set initial conditions
        a = math.floor(square_root.evaluate())
        alpha = IrrationalFraction(
            IrrationalSum(square_root, 1, 0),
            IrrationalSum(square_root, 0, 1)
        )

        while alpha not in alphas:
            constants.append(a)
            alphas.add(alpha)

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

        return PeriodicContinuedFraction(constants, repeat_idx=1)
