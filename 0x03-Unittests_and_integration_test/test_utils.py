#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 01-02-2024
"""
import unittest
from unittest.mock import MagicMock, Mock, patch
from utils import access_nested_map, get_json
from parameterized import parameterized, param  # type: ignore
from typing import Dict, Sequence, Union


class TestAccessNestedMap(unittest.TestCase):
    """Test class for utils.nested_map"""

    @parameterized.expand([
        param(nested_map={"a": 1}, path=("a",), result=1),
        param(nested_map={"a": {"b": 2}}, path=("a",), result={"b": 2}),
        param(nested_map={"a": {"b": 2}}, path=("a", "b"), result=2)
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Sequence, result:
                               Union[Dict, int]):
        """tests the utils.nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        param(nested_map={}, path=("a",)),
        param(nested_map={"a": 1}, path=("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Sequence):
        """test key error exception raise in utils.nested_map"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        msg = str(context.exception).strip("'")
        self.assertEqual(msg, path[-1])


class TestGetJson(unittest.TestCase):
    """creates a mock for testing HTTP requests in get_json"""

    @parameterized.expand([
        param(test_url="http://example.com", test_payload={"payload": True}),
        param(test_url="http://holberton.io", test_payload={"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, response: Union[MagicMock, Mock],
                      test_url: str, test_payload: Dict[str, bool]):
        """test json response from http request"""
        # json.return_value = test_payload
        json = Mock(return_value=test_payload)
        # assign response objects json method to the mock json method
        response.return_value.json = json
        self.assertEqual(test_payload, get_json(test_url))


if __name__ == '__main__':
    unittest.main()
