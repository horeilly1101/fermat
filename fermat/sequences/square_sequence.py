import itertools
from fermat.sequences.sequence import Sequence


class SquareSequence(Sequence):
    def __iter__(self):
        return (pow(val, 2) for val in itertools.count(1))
