import unittest
import sys

sys.path.insert(0, "FinalProject/Notebooks/Functions")
import BasicFunctions as BF


class TestFilter(unittest.TestCase):
    def test_valid_input(self):
        # Test with valid input
        input_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
        keys_to_filter = ["b", "d"]
        result = BF.filter_dict(input_dict, keys_to_filter)
        self.assertEqual(result, {"a": 1, "c": 3})

    def test_empty_input_dict(self):
        # Test with an empty input dictionary
        input_dict = {}
        keys_to_filter = ["b", "d"]
        result = BF.filter_dict(input_dict, keys_to_filter)
        self.assertEqual(result, {})

    def test_empty_keys_to_filter(self):
        # Test with an empty list of keys to filter
        input_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
        keys_to_filter = []
        result = BF.filter_dict(input_dict, keys_to_filter)
        self.assertEqual(result, input_dict)

    def test_keys_not_in_dict(self):
        # Test when some keys in keys_to_filter are not present in the dictionary
        input_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
        keys_to_filter = ["b", "e"]
        result = BF.filter_dict(input_dict, keys_to_filter)
        self.assertEqual(result, {"a": 1, "c": 3, "d": 4})


if __name__ == "__main__":
    unittest.main()
