import unittest
from fermat.sequences.triangle_sequence import TriangleSequence
from fermat.sequences.square_sequence import SquareSequence
from fermat.sequences.prime_sequence import PrimeSequence


class TestSequence(unittest.TestCase):
    def test_triangle(self):
        seq = TriangleSequence()
        for elem in seq.get_terms(10):
            print(elem)

    def test_square(self):
        seq = SquareSequence()
        for elem in seq.get_terms(10):
            print(elem)

    def test_prime(self):
        seq = PrimeSequence()
        for elem in seq.get_terms(10):
            print(elem)
