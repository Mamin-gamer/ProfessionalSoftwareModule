import unittest
import sys

sys.path.insert(0, "ProjectFolder")
from code import foo

class TestFoo(unittest.TestCase):
    def test1(self):
        self.assertEqual(foo(), 1)


if __name__ == "__main__":
    unittest.main()