import unittest
import sys

sys.path.insert(0, "CircleCI_test/ProjectFolder")
from code import foo


class TestFoo(unittest.TestCase):
    def test1(self):
        self.assertEqual(foo(), 1)

    def test2(self):
        ...


if __name__ == "__main__":
    unittest.main()
