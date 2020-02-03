# coding: utf-8

"""
    Rustici Engine API

    Rustici Engine API  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.dispatch_api import DispatchApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDispatchApi(unittest.TestCase):
    """DispatchApi unit test stubs"""

    def setUp(self):
        self.api = api.dispatch_api.DispatchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_destinations(self):
        """Test case for create_destinations

        Create multiple destinations  # noqa: E501
        """
        pass

    def test_create_dispatches(self):
        """Test case for create_dispatches

        Create multiple dispatches  # noqa: E501
        """
        pass

    def test_delete_destination(self):
        """Test case for delete_destination

        Delete the destination with id `destinationId`  # noqa: E501
        """
        pass

    def test_delete_destination_dispatches(self):
        """Test case for delete_destination_dispatches

        Delete all dispatches associated with this destination  # noqa: E501
        """
        pass

    def test_delete_dispatch(self):
        """Test case for delete_dispatch

        Delete the dispatch with id `dispatchId`  # noqa: E501
        """
        pass

    def test_enable_registration_instancing(self):
        """Test case for enable_registration_instancing

        Enable or disable registration instancing  # noqa: E501
        """
        pass

    def test_get_destination(self):
        """Test case for get_destination

        Get the destination with id `destinationId`  # noqa: E501
        """
        pass

    def test_get_destination_dispatch_registration_count(self):
        """Test case for get_destination_dispatch_registration_count

        Get the registration count for all related dispatch registrations  # noqa: E501
        """
        pass

    def test_get_destination_dispatch_zip(self):
        """Test case for get_destination_dispatch_zip

        Get a ZIP file containing all dispatch packages related to a destination.  # noqa: E501
        """
        pass

    def test_get_destination_dispatches(self):
        """Test case for get_destination_dispatches

        Get a list of related dispatches  # noqa: E501
        """
        pass

    def test_get_destinations(self):
        """Test case for get_destinations

        Get a list of destinations  # noqa: E501
        """
        pass

    def test_get_dispatch(self):
        """Test case for get_dispatch

        Get the dispatch with id `dispatchId`  # noqa: E501
        """
        pass

    def test_get_dispatch_enabled(self):
        """Test case for get_dispatch_enabled

        Returns boolean indicating if dispatch with id `dispatchId` is enabled  # noqa: E501
        """
        pass

    def test_get_dispatch_registration_count(self):
        """Test case for get_dispatch_registration_count

        Get the registration count for this dispatch, and the date and time of the last count reset, if any.  # noqa: E501
        """
        pass

    def test_get_dispatch_zip(self):
        """Test case for get_dispatch_zip

        Get the ZIP dispatch package.  # noqa: E501
        """
        pass

    def test_get_dispatches(self):
        """Test case for get_dispatches

        Get a list of dispatches  # noqa: E501
        """
        pass

    def test_get_lti_dispatch(self):
        """Test case for get_lti_dispatch

        Get the information necessary to launch this dispatch using the IMS LTI specification.  # noqa: E501
        """
        pass

    def test_post_dispatch_lti_reporters(self):
        """Test case for post_dispatch_lti_reporters

        Set up a temporary LTI reporter; for use by products that use their own LTI entry points  # noqa: E501
        """
        pass

    def test_reset_destination_dispatch_registration_count(self):
        """Test case for reset_destination_dispatch_registration_count

        Reset the registration count for related dispatches.  # noqa: E501
        """
        pass

    def test_reset_dispatch_registration_count(self):
        """Test case for reset_dispatch_registration_count

        Reset the registration count for this dispatch.  # noqa: E501
        """
        pass

    def test_set_destination(self):
        """Test case for set_destination

        Create or update the destination with id `destinationId`  # noqa: E501
        """
        pass

    def test_set_destination_dispatch_enabled(self):
        """Test case for set_destination_dispatch_enabled

        Enable or disable all related dispatches  # noqa: E501
        """
        pass

    def test_set_dispatch_enabled(self):
        """Test case for set_dispatch_enabled

        Enable or disable the dispatch  # noqa: E501
        """
        pass

    def test_update_dispatch(self):
        """Test case for update_dispatch

        Update the dispatch with id `dispatchId`  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
