#!/usr/bin/env python3
"""Parametired a unittest"""
from typing import Any, Dict, Mapping, Sequence
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from requests import Request

from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """Test get_json utils method"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Test get_json method implementation
        Args:
            test_url (str): url to test with
            payload (dict): return dict from url requests
        """
        with patch("utils.requests.get") as mock_get:
            mock_obj = Mock(autospec=Request)
            mock_obj.json.return_value = test_payload
            mock_get.return_value = mock_obj
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)
