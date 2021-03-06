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


class PIIDeletionRequestSchema(object):
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
        'learner_ids': 'list[str]',
        'agents': 'list[object]'
    }

    attribute_map = {
        'learner_ids': 'learnerIds',
        'agents': 'agents'
    }

    def __init__(self, learner_ids=None, agents=None):  # noqa: E501
        """PIIDeletionRequestSchema - a model defined in Swagger"""  # noqa: E501
        self._learner_ids = None
        self._agents = None
        self.discriminator = None
        if learner_ids is not None:
            self.learner_ids = learner_ids
        if agents is not None:
            self.agents = agents

    @property
    def learner_ids(self):
        """Gets the learner_ids of this PIIDeletionRequestSchema.  # noqa: E501


        :return: The learner_ids of this PIIDeletionRequestSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._learner_ids

    @learner_ids.setter
    def learner_ids(self, learner_ids):
        """Sets the learner_ids of this PIIDeletionRequestSchema.


        :param learner_ids: The learner_ids of this PIIDeletionRequestSchema.  # noqa: E501
        :type: list[str]
        """

        self._learner_ids = learner_ids

    @property
    def agents(self):
        """Gets the agents of this PIIDeletionRequestSchema.  # noqa: E501


        :return: The agents of this PIIDeletionRequestSchema.  # noqa: E501
        :rtype: list[object]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this PIIDeletionRequestSchema.


        :param agents: The agents of this PIIDeletionRequestSchema.  # noqa: E501
        :type: list[object]
        """

        self._agents = agents

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
        if issubclass(PIIDeletionRequestSchema, dict):
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
        if not isinstance(other, PIIDeletionRequestSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
