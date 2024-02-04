#!/usr/bin/env python3
"""Test client class"""


import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test githuborg client"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', autospec=True)
    def test_org(self, org: str, mock_get_json: Mock) -> None:
        """Test org object method"""
        payload = {"payload": True}

        mock_get_json.return_value = payload

        client = GithubOrgClient(org)
        org_payload = client.org

        self.assertEqual(payload, org_payload)
        mock_get_json.assert_called_once()
