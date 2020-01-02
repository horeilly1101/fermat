from typing import NamedTuple

from rsa.continued_fractions.expression import Number
from rsa.continued_fractions.generators import cf_representation_generator
from rsa import utils


class Convergent(NamedTuple):
    p: int
    q: int

    def evaluate(self):
        return self.p / self.q


class ContinuedFraction:
    def __init__(self, generator_factory: utils.GeneratorFactory):
        self.generator_factory = generator_factory

    def __iter__(self):
        return self.generator_factory.create()

    def get_convergent(self, n: int) -> Convergent:
        assert n >= 0
        prev_convergent = Convergent(1, 0)
        global convergent

        for i, a_i in self:
            if i == 0:
                convergent = Convergent(a_i, 1)
                continue

            prev_convergent, convergent = (
                convergent,
                Convergent(
                    a_i * convergent.p + prev_convergent.p,
                    a_i * convergent.q + prev_convergent.q
                )
            )

        return convergent

    @staticmethod
    def make(num_callable):
        factory = utils.GeneratorFactory(
            cf_representation_generator,
            number=Number(num_callable)
        )

        return ContinuedFraction(factory)
