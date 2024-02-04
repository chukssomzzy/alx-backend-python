#!/usr/bin/env python3
"""Test client class"""


from typing import Dict
import unittest
from unittest.mock import Mock, PropertyMock, patch

from parameterized import parameterized

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        org = 'google'
        mock_get_json.return_value = TEST_PAYLOAD[0][1]

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock__public_repos_url:
            mock__public_repos_url.return_value = TEST_PAYLOAD[0][
                0]["repos_url"]
            json_payload = TEST_PAYLOAD[0][1]
            public_repos = [
                repo["name"] for repo in json_payload
            ]
            client = GithubOrgClient(org)
            self.assertEqual(client.public_repos(), public_repos)
            mock__public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    # @parameterized.expand([
    #
    # ])
    # def test_has_license(self):
    #     """Test GithubOrgClient has_license method"""
    #
