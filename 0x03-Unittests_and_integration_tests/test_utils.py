#!/usr/bin/env python3
"""
testing the utils module
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from typing import Dict, Mapping, Sequence, Tuple, Union
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    tests the nested maps function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map: Dict,
            path: Tuple[str], expected: Union[Dict, str]) -> None:
        """
        tests the test nested maops
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self, nested_map: Dict,
            path: Tuple[str], exception: Exception) -> None:
        """
        Tests access nested maps with expansion
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    test the get json
    """
    def test_get_json(
            self, test_url: str,
            test_payload: Dict) -> None:
        """
        test the output of json
        """
        atr = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**atr)) as get_req:
            self.assertEqual(get_json(test_url), test_payload)
            get_req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    test memoize
    """
    def test_memoize(self) -> None:
        """
        test output of memoize
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass, "a_method",
                return_value=42) as memo_fix:
            test_cl = TestClass()
            self.assertEqual(test_cl.a_property(), 42)
            self.assertEqual(test_cl.a_property(), 42)
            memo_fix.assert_called_once()
