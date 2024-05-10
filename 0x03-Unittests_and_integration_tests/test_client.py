#!/usr/bin/env python3
"""
module for testing
"""
from unittest import TestCase
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock, MagicMock
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    tests the client
    """
    @parameterized.expand([
        ("google", {'login': "google"}), ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, res: Dict, mock: MagicMock) -> None:
        """
        test the github client
        """
        mock.return_value = MagicMock(return_value=res)
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), res)
        mock.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org_name))

    def test_public_repos_url(self):
        """
        test the clients repos
        """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock,
                          return_value={"repos_url": "Test value"}) as mock:
            test_json = {"repos_url": "Test value"}
            client = GithubOrgClient(test_json.get("repos_url"))
            result = client._public_repos_url
            self.assertEqual(result, mock.return_value.get("repos_url"))
            mock.assert_called_once

    @patch("client.get_json", return_value=[{"name": "Test value"}])
    def test_public_repos(self, mock):
        """
        test the client public repo
        """
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="(link unavailable)") as rep:
            client = GithubOrgClient("Test value")
            result = client.public_repos()
            self.assertEqual(result, [{"name": "Test value"}])
            mock.assert_called_once()
            rep.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, ret):
        """
        test if client has license
        """
        client = GithubOrgClient("Test value")
        result = client.has_license(repo, key)
        self.assertEqual(ret, result)

@parameterized_class(("org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    class that tests integration
    """

    @classmethod
    def setUpClass(cls):
        """
        prepares for testing
        """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        deletes after testing
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        test the clients repos
        """
        result = GithubOrgClient("Test value")
        self.assertTrue(result)
