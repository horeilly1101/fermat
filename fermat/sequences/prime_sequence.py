import itertools
from fermat.sequences.sequence import Sequence
from fermat.primality_testing import is_prime


class PrimeSequence(Sequence):
    def __iter__(self):
        return (num for num in itertools.count(2) if is_prime(num))
