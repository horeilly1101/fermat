import unittest
import fermat.utils as utils
from tests.utils import PRIMES


class TestUtils(unittest.TestCase):
    def test_compute_modular_inverse(self):
        for p1 in PRIMES:
            for p2 in PRIMES:
                if p1 != p2:
                    inv = utils.compute_modular_inverse(p1, p2)
                    self.assertEqual(
                        1,
                        (p1 * inv) % p2
                    )
