#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 01-02-2024
"""
import unittest
from unittest.mock import MagicMock, Mock, patch
from client import GithubOrgClient
from parameterized import parameterized, param  # type: ignore
from typing import Dict, Sequence, Union

gres = {
    "login": "google",
    "id": 1342004,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
    "url": "https://api.github.com/orgs/google",
    "repos_url": "https://api.github.com/orgs/google/repos",
    "events_url": "https://api.github.com/orgs/google/events",
    "hooks_url": "https://api.github.com/orgs/google/hooks",
    "issues_url": "https://api.github.com/orgs/google/issues",
    "members_url": "https://api.github.com/orgs/google/members{/member}",
    "public_members_url":
    "https://api.github.com/orgs/google/public_members{/member}",
    "avatar_url": "https://avatars.githubusercontent.com/u/1342004?v=4",
    "description": "Google ❤️ Open Source",
    "name": "Google",
    "company": None,
    "blog": "https://opensource.google/",
    "location": None,
    "email": "opensource@google.com",
    "twitter_username": "GoogleOSS",
    "is_verified": True,
    "has_organization_projects": True,
    "has_repository_projects": True,
    "public_repos": 2598,
    "public_gists": 0,
    "followers": 35341,
    "following": 0,
    "html_url": "https://github.com/google",
    "created_at": "2012-01-18T01:30:18Z",
    "updated_at": "2021-12-30T01:40:20Z",
    "archived_at": None,
    "type": "Organization",
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
        ("abs", abcres)
    ])
    @patch("utils.get_json")
    def test_org(self, org: str, response: Dict, mock_get_json: MagicMock):
        """tests basic response of method calls"""
        mock_get_json.return_value = response
        result = GithubOrgClient(org)

        self.assertEqual(result.org, response)
        self.assertEqual(result.org, response)

        mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
