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


class LaunchLinkRequestSchema(object):
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
        'expiry': 'int',
        'redirect_on_exit_url': 'str',
        'tracking': 'bool',
        'start_sco': 'str',
        'additional_values': 'list[ItemValuePairSchema]'
    }

    attribute_map = {
        'expiry': 'expiry',
        'redirect_on_exit_url': 'redirectOnExitUrl',
        'tracking': 'tracking',
        'start_sco': 'startSco',
        'additional_values': 'additionalValues'
    }

    def __init__(self, expiry=120, redirect_on_exit_url=None, tracking=True, start_sco=None, additional_values=None):  # noqa: E501
        """LaunchLinkRequestSchema - a model defined in Swagger"""  # noqa: E501
        self._expiry = None
        self._redirect_on_exit_url = None
        self._tracking = None
        self._start_sco = None
        self._additional_values = None
        self.discriminator = None
        if expiry is not None:
            self.expiry = expiry
        if redirect_on_exit_url is not None:
            self.redirect_on_exit_url = redirect_on_exit_url
        if tracking is not None:
            self.tracking = tracking
        if start_sco is not None:
            self.start_sco = start_sco
        if additional_values is not None:
            self.additional_values = additional_values

    @property
    def expiry(self):
        """Gets the expiry of this LaunchLinkRequestSchema.  # noqa: E501

        The number of seconds from now that this link will expire in. This parameter should only be specified if the setting 'ApiUseSignedLaunchLinks' is configured with a value of 'true'.  # noqa: E501

        :return: The expiry of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this LaunchLinkRequestSchema.

        The number of seconds from now that this link will expire in. This parameter should only be specified if the setting 'ApiUseSignedLaunchLinks' is configured with a value of 'true'.  # noqa: E501

        :param expiry: The expiry of this LaunchLinkRequestSchema.  # noqa: E501
        :type: int
        """

        self._expiry = expiry

    @property
    def redirect_on_exit_url(self):
        """Gets the redirect_on_exit_url of this LaunchLinkRequestSchema.  # noqa: E501

        The URL the application should redirect to when the learner exits a course. If not specified, configured value will be used.  # noqa: E501

        :return: The redirect_on_exit_url of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._redirect_on_exit_url

    @redirect_on_exit_url.setter
    def redirect_on_exit_url(self, redirect_on_exit_url):
        """Sets the redirect_on_exit_url of this LaunchLinkRequestSchema.

        The URL the application should redirect to when the learner exits a course. If not specified, configured value will be used.  # noqa: E501

        :param redirect_on_exit_url: The redirect_on_exit_url of this LaunchLinkRequestSchema.  # noqa: E501
        :type: str
        """

        self._redirect_on_exit_url = redirect_on_exit_url

    @property
    def tracking(self):
        """Gets the tracking of this LaunchLinkRequestSchema.  # noqa: E501

        Should this launch be tracked? If false, Engine will avoid tracking to the extent possible for the standard being used.  # noqa: E501

        :return: The tracking of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: bool
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this LaunchLinkRequestSchema.

        Should this launch be tracked? If false, Engine will avoid tracking to the extent possible for the standard being used.  # noqa: E501

        :param tracking: The tracking of this LaunchLinkRequestSchema.  # noqa: E501
        :type: bool
        """

        self._tracking = tracking

    @property
    def start_sco(self):
        """Gets the start_sco of this LaunchLinkRequestSchema.  # noqa: E501

        For SCORM, SCO identifier to override launch, overriding the normal sequencing.  # noqa: E501

        :return: The start_sco of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._start_sco

    @start_sco.setter
    def start_sco(self, start_sco):
        """Sets the start_sco of this LaunchLinkRequestSchema.

        For SCORM, SCO identifier to override launch, overriding the normal sequencing.  # noqa: E501

        :param start_sco: The start_sco of this LaunchLinkRequestSchema.  # noqa: E501
        :type: str
        """

        self._start_sco = start_sco

    @property
    def additional_values(self):
        """Gets the additional_values of this LaunchLinkRequestSchema.  # noqa: E501


        :return: The additional_values of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: list[ItemValuePairSchema]
        """
        return self._additional_values

    @additional_values.setter
    def additional_values(self, additional_values):
        """Sets the additional_values of this LaunchLinkRequestSchema.


        :param additional_values: The additional_values of this LaunchLinkRequestSchema.  # noqa: E501
        :type: list[ItemValuePairSchema]
        """

        self._additional_values = additional_values

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
        if issubclass(LaunchLinkRequestSchema, dict):
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
        if not isinstance(other, LaunchLinkRequestSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other