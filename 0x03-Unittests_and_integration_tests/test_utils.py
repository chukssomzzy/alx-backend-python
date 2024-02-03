#!/usr/bin/env python3
"""Parametired a unittest"""
from typing import Any, Mapping, Sequence
import unittest
from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test Access Nested Map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map=nested_map,
                                           path=path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, error) -> None:
        """Test access_nested_map for exception"""
        with self.assertRaisesRegex(KeyError, error):
            access_nested_map(nested_map=nested_map, path=path)
