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
                               path: Sequence, expected: Any):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map=nested_map,
                                           path=path), expected)