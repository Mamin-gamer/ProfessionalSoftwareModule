import unittest
import sys

sys.path.insert(0, "FinalProject/Notebooks/Functions")
from BasicFunctions import filter_dict


class TestFilter(unittest.TestCase):
    def test_valid_input(self):
        input_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
        keys_to_filter = ["b", "d"]
        result = filter_dict(input_dict, keys_to_filter)
        self.assertEqual(result, {"a": 1, "c": 3})

    def test_empty_input_dict(self):
        input_dict = {}
        keys_to_filter = ["b", "d"]
        result = filter_dict(input_dict, keys_to_filter)
        self.assertEqual(result, {})

    def test_empty_keys_to_filter(self):
        input_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
        keys_to_filter = []
        result = filter_dict(input_dict, keys_to_filter)
        self.assertEqual(result, input_dict)

    def test_keys_not_in_dict(self):
        input_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
        keys_to_filter = ["b", "e"]
        result = filter_dict(input_dict, keys_to_filter)
        self.assertEqual(result, {"a": 1, "c": 3, "d": 4})

    def test_invalid_keys_type(self):
        input_dict = {"a": 1, "b": 2, "c": 3}
        keys_to_filter = ["a", 123]
        with self.assertRaises(ValueError):
            filter_dict(input_dict, keys_to_filter)


if __name__ == "__main__":
    unittest.main()
