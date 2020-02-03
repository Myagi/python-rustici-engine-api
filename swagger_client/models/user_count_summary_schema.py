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


class UserCountSummarySchema(object):
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
        'combined_tenants': 'UserCountDetailSchema',
        'by_tenant': 'list[UserCountDetailSchema]'
    }

    attribute_map = {
        'combined_tenants': 'combinedTenants',
        'by_tenant': 'byTenant'
    }

    def __init__(self, combined_tenants=None, by_tenant=None):  # noqa: E501
        """UserCountSummarySchema - a model defined in Swagger"""  # noqa: E501
        self._combined_tenants = None
        self._by_tenant = None
        self.discriminator = None
        self.combined_tenants = combined_tenants
        self.by_tenant = by_tenant

    @property
    def combined_tenants(self):
        """Gets the combined_tenants of this UserCountSummarySchema.  # noqa: E501


        :return: The combined_tenants of this UserCountSummarySchema.  # noqa: E501
        :rtype: UserCountDetailSchema
        """
        return self._combined_tenants

    @combined_tenants.setter
    def combined_tenants(self, combined_tenants):
        """Sets the combined_tenants of this UserCountSummarySchema.


        :param combined_tenants: The combined_tenants of this UserCountSummarySchema.  # noqa: E501
        :type: UserCountDetailSchema
        """
        if combined_tenants is None:
            raise ValueError("Invalid value for `combined_tenants`, must not be `None`")  # noqa: E501

        self._combined_tenants = combined_tenants

    @property
    def by_tenant(self):
        """Gets the by_tenant of this UserCountSummarySchema.  # noqa: E501


        :return: The by_tenant of this UserCountSummarySchema.  # noqa: E501
        :rtype: list[UserCountDetailSchema]
        """
        return self._by_tenant

    @by_tenant.setter
    def by_tenant(self, by_tenant):
        """Sets the by_tenant of this UserCountSummarySchema.


        :param by_tenant: The by_tenant of this UserCountSummarySchema.  # noqa: E501
        :type: list[UserCountDetailSchema]
        """
        if by_tenant is None:
            raise ValueError("Invalid value for `by_tenant`, must not be `None`")  # noqa: E501

        self._by_tenant = by_tenant

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
        if issubclass(UserCountSummarySchema, dict):
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
        if not isinstance(other, UserCountSummarySchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
