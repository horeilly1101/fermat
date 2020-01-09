import itertools
from fermat.sequences.sequence import Sequence


class TriangleSequence(Sequence):
    def __iter__(self):
        return itertools.accumulate(itertools.count(1))
