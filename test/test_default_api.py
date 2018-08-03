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
from pyns_auto.api.default_api import DefaultApi  # noqa: E501
from pyns_auto.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = pyns_auto.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_user_get(self):
        """Test case for api_user_get

        Get current user information.  # noqa: E501
        """
        pass

    def test_api_user_post(self):
        """Test case for api_user_post

        Add a new user.  # noqa: E501
        """
        pass

    def test_api_user_put(self):
        """Test case for api_user_put

        Edit user information.  # noqa: E501
        """
        pass

    def test_api_user_resend_confirmation_post(self):
        """Test case for api_user_resend_confirmation_post

        Resend confirmation email.  # noqa: E501
        """
        pass

    def test_api_user_reset_password_post(self):
        """Test case for api_user_reset_password_post

        """
        pass

    def test_api_user_submit_token_post(self):
        """Test case for api_user_submit_token_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
