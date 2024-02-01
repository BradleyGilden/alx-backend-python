#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 01-02-2024
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized  # type: ignore
from typing import Dict, Sequence, Union


class TestAccessNestedMap(unittest.TestCase):
    """Test class for utils.nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Sequence, result:
                               Union[Dict, int]):
        """tests the utils.nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), result)


if __name__ == '__main__':
    unittest.main()
