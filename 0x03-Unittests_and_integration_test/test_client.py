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

gres = {
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
    "updated_at": "2021-12-30T01:40:20Z"
}
abcres = {
    'message': 'Not Found',
    'documentation_url':
    'https://docs.github.com/rest/orgs/orgs#get-an-organization'
}


class TestGithubOrgClient(unittest.TestCase):
    """testing responses for a request client for github"""

    @parameterized.expand([
        ("google", gres),
        ("abc", abcres)
    ])
    @patch("utils.get_json")
    def test_org(self, org: str, response: Dict, mock_get_json: MagicMock):
        """tests basic response of method calls"""
        mock_get_json.return_value = response
        # replaces org with mock_get_json
        with patch.object(GithubOrgClient, 'org', new_callable=mock_get_json):
            result = GithubOrgClient(org)
            self.assertEqual(result.org, response)
            self.assertEqual(result.org, response)
            mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """tests the _public_repos_url property"""
        with patch.object(
            GithubOrgClient, 'org', new_callable=PropertyMock
        ) as cm:
            cm.return_value = gres
            cli = GithubOrgClient("google")
            self.assertEqual(cli._public_repos_url,
                             "https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()
