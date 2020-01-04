from abc import ABC, abstractmethod


class Factorization(ABC):
    @abstractmethod
    def compute_product(self):
        pass
