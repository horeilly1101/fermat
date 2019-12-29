import unittest
from rsa.quadratic_reciprocity import compute_jacobi_symbol


class TestQuadraticReciprocity(unittest.TestCase):
    def test_residues(self):
        residues = {
            4: 5,
            9: 5,
            -1: 5,
            13: 17,
            39: 7,
            11: 37,
            14: 137,
            7: 137,
            37603: 48611
        }

        for residue, modulus in residues.items():
            self.assertEqual(
                1,
                compute_jacobi_symbol(residue, modulus)
            )

    def test_non_residues(self):
        non_residues = {
            5: 3593,
            3: 7,
            55: 179,
            299: 397
        }

        for non_residue, modulus in non_residues.items():
            self.assertEqual(
                -1,
                compute_jacobi_symbol(non_residue, modulus)
            )
