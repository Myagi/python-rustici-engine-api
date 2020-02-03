# coding: utf-8

"""
    Rustici Engine API

    Rustici Engine API  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ImportRequestSchema(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'fetch_request': 'ImportFetchRequestSchema',
        'reference_request': 'ImportReferenceRequestSchema',
        'media_file_reference_request': 'ImportMediaFileReferenceRequestSchema',
        'connector_reference_request': 'ImportConnectorRequestSchema',
        'ad_hoc_reference_request': 'ImportAdHocReferenceRequestSchema'
    }

    attribute_map = {
        'fetch_request': 'fetchRequest',
        'reference_request': 'referenceRequest',
        'media_file_reference_request': 'mediaFileReferenceRequest',
        'connector_reference_request': 'connectorReferenceRequest',
        'ad_hoc_reference_request': 'adHocReferenceRequest'
    }

    def __init__(self, fetch_request=None, reference_request=None, media_file_reference_request=None, connector_reference_request=None, ad_hoc_reference_request=None):  # noqa: E501
        """ImportRequestSchema - a model defined in Swagger"""  # noqa: E501
        self._fetch_request = None
        self._reference_request = None
        self._media_file_reference_request = None
        self._connector_reference_request = None
        self._ad_hoc_reference_request = None
        self.discriminator = None
        if fetch_request is not None:
            self.fetch_request = fetch_request
        if reference_request is not None:
            self.reference_request = reference_request
        if media_file_reference_request is not None:
            self.media_file_reference_request = media_file_reference_request
        if connector_reference_request is not None:
            self.connector_reference_request = connector_reference_request
        if ad_hoc_reference_request is not None:
            self.ad_hoc_reference_request = ad_hoc_reference_request

    @property
    def fetch_request(self):
        """Gets the fetch_request of this ImportRequestSchema.  # noqa: E501


        :return: The fetch_request of this ImportRequestSchema.  # noqa: E501
        :rtype: ImportFetchRequestSchema
        """
        return self._fetch_request

    @fetch_request.setter
    def fetch_request(self, fetch_request):
        """Sets the fetch_request of this ImportRequestSchema.


        :param fetch_request: The fetch_request of this ImportRequestSchema.  # noqa: E501
        :type: ImportFetchRequestSchema
        """

        self._fetch_request = fetch_request

    @property
    def reference_request(self):
        """Gets the reference_request of this ImportRequestSchema.  # noqa: E501


        :return: The reference_request of this ImportRequestSchema.  # noqa: E501
        :rtype: ImportReferenceRequestSchema
        """
        return self._reference_request

    @reference_request.setter
    def reference_request(self, reference_request):
        """Sets the reference_request of this ImportRequestSchema.


        :param reference_request: The reference_request of this ImportRequestSchema.  # noqa: E501
        :type: ImportReferenceRequestSchema
        """

        self._reference_request = reference_request

    @property
    def media_file_reference_request(self):
        """Gets the media_file_reference_request of this ImportRequestSchema.  # noqa: E501


        :return: The media_file_reference_request of this ImportRequestSchema.  # noqa: E501
        :rtype: ImportMediaFileReferenceRequestSchema
        """
        return self._media_file_reference_request

    @media_file_reference_request.setter
    def media_file_reference_request(self, media_file_reference_request):
        """Sets the media_file_reference_request of this ImportRequestSchema.


        :param media_file_reference_request: The media_file_reference_request of this ImportRequestSchema.  # noqa: E501
        :type: ImportMediaFileReferenceRequestSchema
        """

        self._media_file_reference_request = media_file_reference_request

    @property
    def connector_reference_request(self):
        """Gets the connector_reference_request of this ImportRequestSchema.  # noqa: E501


        :return: The connector_reference_request of this ImportRequestSchema.  # noqa: E501
        :rtype: ImportConnectorRequestSchema
        """
        return self._connector_reference_request

    @connector_reference_request.setter
    def connector_reference_request(self, connector_reference_request):
        """Sets the connector_reference_request of this ImportRequestSchema.


        :param connector_reference_request: The connector_reference_request of this ImportRequestSchema.  # noqa: E501
        :type: ImportConnectorRequestSchema
        """

        self._connector_reference_request = connector_reference_request

    @property
    def ad_hoc_reference_request(self):
        """Gets the ad_hoc_reference_request of this ImportRequestSchema.  # noqa: E501


        :return: The ad_hoc_reference_request of this ImportRequestSchema.  # noqa: E501
        :rtype: ImportAdHocReferenceRequestSchema
        """
        return self._ad_hoc_reference_request

    @ad_hoc_reference_request.setter
    def ad_hoc_reference_request(self, ad_hoc_reference_request):
        """Sets the ad_hoc_reference_request of this ImportRequestSchema.


        :param ad_hoc_reference_request: The ad_hoc_reference_request of this ImportRequestSchema.  # noqa: E501
        :type: ImportAdHocReferenceRequestSchema
        """

        self._ad_hoc_reference_request = ad_hoc_reference_request

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ImportRequestSchema, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportRequestSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
