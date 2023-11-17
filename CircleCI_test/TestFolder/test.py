import unittest
import sys

sys.path.insert(0, "CircleCI_test/ProjectFolder")
from code import foo


class TestFoo(unittest.TestCase):
    def test_equals_to_one(self):
        self.assertEqual(foo(), 1)

    def test_not_equals_to_one(self):
        self.assertEqual(foo(), 5)


if __name__ == "__main__":
    unittest.main()
