#!/usr/bin/env python3
"""Test client class"""


from collections import Mapping
from typing import Dict
import unittest
from unittest.mock import Mock, PropertyMock, patch

from parameterized import parameterized, parameterized_class
from requests import HTTPError

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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, license_mapping: Dict[str, Dict], license: str,
                         has_licence: bool) -> None:
        """Test GithubOrgClient has_license method"""
        org = "google"
        client = GithubOrgClient(org)
        self.assertEqual(client.has_license(license_mapping,
                                            license), has_licence)


@parameterized_class([{"org_payload": TEST_PAYLOAD[0][0],
                       "repos_payload": TEST_PAYLOAD[0][1],
                       "expected_repos": TEST_PAYLOAD[0][2],
                       "apache2_repos": TEST_PAYLOAD[0][3]
                       }])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient"""

    @classmethod
    def setUpClass(cls) -> None:
        """Setup integration test suits"""
        expected_payload = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def get_url_payload(url: str) -> None:
            """ check if a  url is expected and return
            payload
            """
            if url in expected_payload:
                return Mock(**{"json.return_value": expected_payload[url]})
            else:
                raise HTTPError

        cls.get_patcher = patch("requests.get",
                                side_effect=get_url_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Integration test for test_public_repos"""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Test public repos with license"""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        """Teardown integration test suits"""
        cls.get_patcher.stop()
