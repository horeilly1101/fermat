from dataclasses import dataclass


@dataclass
class Convergent:
    p: int
    q: int

    def __str__(self):
        return f"{self.p} / {self.q}"

    def evaluate(self):
        return self.p / self.q
