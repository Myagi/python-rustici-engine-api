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


class ImportReferenceRequestSchema(object):
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
        'url': 'str',
        'web_path_to_course': 'str'
    }

    attribute_map = {
        'url': 'url',
        'web_path_to_course': 'webPathToCourse'
    }

    def __init__(self, url=None, web_path_to_course=None):  # noqa: E501
        """ImportReferenceRequestSchema - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._web_path_to_course = None
        self.discriminator = None
        self.url = url
        self.web_path_to_course = web_path_to_course

    @property
    def url(self):
        """Gets the url of this ImportReferenceRequestSchema.  # noqa: E501

        URL path to the manifest that defines this course  # noqa: E501

        :return: The url of this ImportReferenceRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImportReferenceRequestSchema.

        URL path to the manifest that defines this course  # noqa: E501

        :param url: The url of this ImportReferenceRequestSchema.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def web_path_to_course(self):
        """Gets the web_path_to_course of this ImportReferenceRequestSchema.  # noqa: E501

        This is the URL to the root of the course, where the course content is already available.  # noqa: E501

        :return: The web_path_to_course of this ImportReferenceRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._web_path_to_course

    @web_path_to_course.setter
    def web_path_to_course(self, web_path_to_course):
        """Sets the web_path_to_course of this ImportReferenceRequestSchema.

        This is the URL to the root of the course, where the course content is already available.  # noqa: E501

        :param web_path_to_course: The web_path_to_course of this ImportReferenceRequestSchema.  # noqa: E501
        :type: str
        """
        if web_path_to_course is None:
            raise ValueError("Invalid value for `web_path_to_course`, must not be `None`")  # noqa: E501

        self._web_path_to_course = web_path_to_course

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
        if issubclass(ImportReferenceRequestSchema, dict):
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
        if not isinstance(other, ImportReferenceRequestSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
