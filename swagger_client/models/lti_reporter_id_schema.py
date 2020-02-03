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


class LtiReporterIdSchema(object):
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
        'lti_reporter_id': 'str'
    }

    attribute_map = {
        'lti_reporter_id': 'ltiReporterId'
    }

    def __init__(self, lti_reporter_id=None):  # noqa: E501
        """LtiReporterIdSchema - a model defined in Swagger"""  # noqa: E501
        self._lti_reporter_id = None
        self.discriminator = None
        self.lti_reporter_id = lti_reporter_id

    @property
    def lti_reporter_id(self):
        """Gets the lti_reporter_id of this LtiReporterIdSchema.  # noqa: E501

        The ID of the LTI reporter that was just created.  # noqa: E501

        :return: The lti_reporter_id of this LtiReporterIdSchema.  # noqa: E501
        :rtype: str
        """
        return self._lti_reporter_id

    @lti_reporter_id.setter
    def lti_reporter_id(self, lti_reporter_id):
        """Sets the lti_reporter_id of this LtiReporterIdSchema.

        The ID of the LTI reporter that was just created.  # noqa: E501

        :param lti_reporter_id: The lti_reporter_id of this LtiReporterIdSchema.  # noqa: E501
        :type: str
        """
        if lti_reporter_id is None:
            raise ValueError("Invalid value for `lti_reporter_id`, must not be `None`")  # noqa: E501

        self._lti_reporter_id = lti_reporter_id

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
        if issubclass(LtiReporterIdSchema, dict):
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
        if not isinstance(other, LtiReporterIdSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
