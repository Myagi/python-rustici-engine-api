# coding: utf-8

"""
    Rustici Engine API

    Rustici Engine API  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import rustici_engine
from api.ping_api import PingApi  # noqa: E501
from rustici_engine.rest import ApiException


class TestPingApi(unittest.TestCase):
    """PingApi unit test stubs"""

    def setUp(self):
        self.api = api.ping_api.PingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_ping(self):
        """Test case for ping

        Get back a message indicating that the API is working.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
