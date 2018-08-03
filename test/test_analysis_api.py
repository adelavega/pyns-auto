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
from pyns_auto.api.analysis_api import AnalysisApi  # noqa: E501
from pyns_auto.rest import ApiException


class TestAnalysisApi(unittest.TestCase):
    """AnalysisApi unit test stubs"""

    def setUp(self):
        self.api = pyns_auto.api.analysis_api.AnalysisApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_analyses_analysis_id_bundle_get(self):
        """Test case for api_analyses_analysis_id_bundle_get

        Get analysis tarball bundle.  # noqa: E501
        """
        pass

    def test_api_analyses_analysis_id_clone_post(self):
        """Test case for api_analyses_analysis_id_clone_post

        Clone analysis.  # noqa: E501
        """
        pass

    def test_api_analyses_analysis_id_compile_post(self):
        """Test case for api_analyses_analysis_id_compile_post

        Compile and lock analysis.  # noqa: E501
        """
        pass

    def test_api_analyses_analysis_id_delete(self):
        """Test case for api_analyses_analysis_id_delete

        Delete analysis.  # noqa: E501
        """
        pass

    def test_api_analyses_analysis_id_full_get(self):
        """Test case for api_analyses_analysis_id_full_get

        Get analysis (including nested fields).  # noqa: E501
        """
        pass

    def test_api_analyses_analysis_id_get(self):
        """Test case for api_analyses_analysis_id_get

        Get analysis by id.  # noqa: E501
        """
        pass

    def test_api_analyses_analysis_id_put(self):
        """Test case for api_analyses_analysis_id_put

        Edit analysis.  # noqa: E501
        """
        pass

    def test_api_analyses_analysis_id_resources_get(self):
        """Test case for api_analyses_analysis_id_resources_get

        Get analysis resources.  # noqa: E501
        """
        pass

    def test_api_analyses_analysis_id_status_get(self):
        """Test case for api_analyses_analysis_id_status_get

        Check if analysis has compiled.  # noqa: E501
        """
        pass

    def test_api_analyses_get(self):
        """Test case for api_analyses_get

        Returns list of public analyses.  # noqa: E501
        """
        pass

    def test_api_analyses_post(self):
        """Test case for api_analyses_post

        Add new analysis!  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()