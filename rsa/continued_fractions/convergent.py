from typing import NamedTuple


class Convergent(NamedTuple):
    p: int
    q: int

    def __str__(self):
        return f"{self.p} / {self.q}"

    def evaluate(self):
        return self.p / self.q