#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 01-02-2024
"""
import unittest
from unittest.mock import MagicMock, patch, PropertyMock, Mock
from client import GithubOrgClient
from parameterized import parameterized, param  # type: ignore
from typing import Dict, Sequence, Union

GPAYLOAD = {
    "login": "google",
    "id": 1342004,
    "url": "https://api.github.com/orgs/google",
    "description": "Google ❤️ Open Source",
    "name": "Google",
    "repos_url": "https://api.github.com/orgs/google/repos",
    "email": "opensource@google.com",
    "twitter_username": "GoogleOSS",
    "followers": 35341,
    "following": 0,
    "created_at": "2012-01-18T01:30:18Z",
    "updated_at": "2021-12-30T01:40:20Z",
}
GREPOS = [
    {
        "id": 123456789,
        "name": "example-repo",
        "full_name": "google/example-repo",
        "description": "An example repository from Google",
        "html_url": "https://github.com/google/example-repo",
        "created_at": "2022-01-01T12:00:00Z",
        "updated_at": "2022-02-01T14:30:00Z",
    },
    {
        "id": 123456799,
        "name": "example-repo2",
        "full_name": "google/example-repo",
        "description": "An example repository from Google",
        "html_url": "https://github.com/google/example-repo",
        "created_at": "2022-01-01T12:00:00Z",
        "updated_at": "2022-02-01T14:30:00Z",
    },
]
ABCPAYLOAD = {
    "message": "Not Found",
    "documentation_url":
    "https://docs.github.com/rest/orgs/orgs#get-an-organization",
}


class TestGithubOrgClient(unittest.TestCase):
    """testing responses for a request client for github"""

    @parameterized.expand([("google", GPAYLOAD), ("abc", ABCPAYLOAD)])
    @patch("utils.get_json")
    def test_org(self, org: str, response: Dict, mock_get_json: MagicMock):
        """tests basic response of method calls"""
        mock_get_json.return_value = response
        # replaces org with mock_get_json
        with patch.object(GithubOrgClient, "org", new_callable=mock_get_json):
            result = GithubOrgClient(org)
            self.assertEqual(result.org, response)
            self.assertEqual(result.org, response)
            mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """tests the _public_repos_url property"""
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as cm:
            cm.return_value = GPAYLOAD
            cli = GithubOrgClient("google")
            self.assertEqual(
                cli._public_repos_url,
                "https://api.github.com/orgs/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock):
        """test the public_repos() method with mocking"""
        mock_get_json.return_value = GREPOS
        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as cm:
            cm.return_value = "https://api.github.com/orgs/google/repos"
            cli = GithubOrgClient("google")
            response = cli.public_repos()
            expected = ["example-repo", "example-repo2"]
            for rname in response:
                self.assertIn(rname, expected)
            mock_get_json.assert_called_once()
            cm.assert_called_once()


if __name__ == "__main__":
    unittest.main()
