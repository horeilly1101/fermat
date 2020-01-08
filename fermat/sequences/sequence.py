from abc import ABC, abstractmethod
import itertools


class Sequence(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    def get_terms(self, n):
        return itertools.islice(self, 0, n)

    def add_terms(self, n):
        return sum(self.get_terms(n))
