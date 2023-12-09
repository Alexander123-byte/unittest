import unittest
from unittest_proj.utils import arrs1


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs1.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs1.get([], 0, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs1.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs1.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs1.my_slice([], 1), [])
        self.assertEqual(arrs1.my_slice([1, 2, 3], 0, 1), [1])
