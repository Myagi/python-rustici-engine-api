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


class ConnectorTypeSchema(object):
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
        'content_connector_type': 'str',
        'version': 'PluginVersionSchema',
        'name': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'content_connector_type': 'contentConnectorType',
        'version': 'version',
        'name': 'name',
        'enabled': 'enabled'
    }

    def __init__(self, content_connector_type=None, version=None, name=None, enabled=None):  # noqa: E501
        """ConnectorTypeSchema - a model defined in Swagger"""  # noqa: E501
        self._content_connector_type = None
        self._version = None
        self._name = None
        self._enabled = None
        self.discriminator = None
        if content_connector_type is not None:
            self.content_connector_type = content_connector_type
        if version is not None:
            self.version = version
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled

    @property
    def content_connector_type(self):
        """Gets the content_connector_type of this ConnectorTypeSchema.  # noqa: E501

        type of content connector  # noqa: E501

        :return: The content_connector_type of this ConnectorTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._content_connector_type

    @content_connector_type.setter
    def content_connector_type(self, content_connector_type):
        """Sets the content_connector_type of this ConnectorTypeSchema.

        type of content connector  # noqa: E501

        :param content_connector_type: The content_connector_type of this ConnectorTypeSchema.  # noqa: E501
        :type: str
        """

        self._content_connector_type = content_connector_type

    @property
    def version(self):
        """Gets the version of this ConnectorTypeSchema.  # noqa: E501


        :return: The version of this ConnectorTypeSchema.  # noqa: E501
        :rtype: PluginVersionSchema
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ConnectorTypeSchema.


        :param version: The version of this ConnectorTypeSchema.  # noqa: E501
        :type: PluginVersionSchema
        """

        self._version = version

    @property
    def name(self):
        """Gets the name of this ConnectorTypeSchema.  # noqa: E501

        name of this content connector type  # noqa: E501

        :return: The name of this ConnectorTypeSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectorTypeSchema.

        name of this content connector type  # noqa: E501

        :param name: The name of this ConnectorTypeSchema.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this ConnectorTypeSchema.  # noqa: E501

        Is there an enabled instance of this connector for the specified tenant (or at the system level)  # noqa: E501

        :return: The enabled of this ConnectorTypeSchema.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConnectorTypeSchema.

        Is there an enabled instance of this connector for the specified tenant (or at the system level)  # noqa: E501

        :param enabled: The enabled of this ConnectorTypeSchema.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(ConnectorTypeSchema, dict):
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
        if not isinstance(other, ConnectorTypeSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other