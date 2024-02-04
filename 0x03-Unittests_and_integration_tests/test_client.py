#!/usr/bin/env python3
"""Test client class"""


from typing import Dict
import unittest
from unittest.mock import Mock, PropertyMock, patch

from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test githuborg client"""

    @parameterized.expand([
        ("google", {"payload": "google"}),
        ("abc", {"payload": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org: str, payload: Dict, mock_get_json: Mock) -> None:
        """Test org object method"""
        mock_get_json.return_value = payload

        client = GithubOrgClient(org)

        self.assertEqual(payload, client.org)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self):
        """Test Public_repos_url"""
        org = "google"
        payload = {"repos_url": f"https://api.github.com/orgs/{org}"}
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock
                          ) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient(org)

            self.assertEqual(client._public_repos_url, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """Test method on GithubOrgClient public repos"""
        org = "google"
        payload = {"repos_url": f"https://api.github.com/orgs/{org}"}

        mock_get_json.return_value = payload
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock__public_repos_url:
            repos_payload = "https://google.com"
            mock__public_repos_url.return_value = repos_payload
            client = GithubOrgClient(org)
            self.assertEqual(payload, client.repos_payload)
            mock_get_json.assert_called_with(repos_payload)
            mock__public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()
