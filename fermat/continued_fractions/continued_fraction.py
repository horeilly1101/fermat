import functools
from typing import Callable, Iterator
from fermat.continued_fractions.convergent import Convergent
from fermat.continued_fractions.expression import Number
from fermat.continued_fractions.generators import cf_representation_generator


class ContinuedFraction:
    def __init__(self, representation_producer: Callable[[], Iterator[int]]):
        self.representation_producer = representation_producer

    def __iter__(self):
        return self.representation_producer()

    def get_terms(self, num_terms: int):
        for _, a_i in zip(range(num_terms), self):
            yield a_i

    def get_convergent(self, n: int) -> Convergent:
        assert n >= 0
        prev_convergent = Convergent(1, 0)
        convergent = None

        for i, a_i in enumerate(self.get_terms(n + 1)):
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
        producer = functools.partial(
            cf_representation_generator,
            number=Number(num_callable)
        )

        return ContinuedFraction(producer)
