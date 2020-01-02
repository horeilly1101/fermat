import math
from typing import List

from rsa.continued_fractions.expression import Number, IrrationalFraction, \
    IrrationalSum, SquareRoot
from rsa.continued_fractions.generators import cf_representation_generator, \
    periodic_cf_representation_generator
from rsa import utils


class ContinuedFraction:
    def __init__(self, generator_factory: utils.GeneratorFactory):
        self.generator_factory = generator_factory

    def __iter__(self):
        return self.generator_factory.create()

    def get_convergent(self, n: int):
        pass

    @staticmethod
    def make(num_callable):
        factory = utils.GeneratorFactory(
            cf_representation_generator,
            number=Number(num_callable)
        )

        return ContinuedFraction(factory)


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
