# coding: utf-8

"""
    neuroscout

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import pyns_auto
from pyns_auto.api.auth_api import AuthApi  # noqa: E501
from pyns_auto.rest import ApiException


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = pyns_auto.api.auth_api.AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_auth_post(self):
        """Test case for api_auth_post

        Get JWT authorizaton token.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
