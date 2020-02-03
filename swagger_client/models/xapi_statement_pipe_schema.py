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


class XapiStatementPipeSchema(object):
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
        'id': 'str',
        'last_forwarded_statement_date': 'str',
        'more_url': 'str',
        'attempts': 'int',
        'visible_after': 'str',
        'source': 'XapiEndpointSchema',
        'target': 'XapiEndpointSchema',
        'local_source': 'XapiSelfSourcedPipeSchema'
    }

    attribute_map = {
        'id': 'id',
        'last_forwarded_statement_date': 'lastForwardedStatementDate',
        'more_url': 'moreUrl',
        'attempts': 'attempts',
        'visible_after': 'visibleAfter',
        'source': 'source',
        'target': 'target',
        'local_source': 'localSource'
    }

    def __init__(self, id=None, last_forwarded_statement_date=None, more_url=None, attempts=None, visible_after=None, source=None, target=None, local_source=None):  # noqa: E501
        """XapiStatementPipeSchema - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._last_forwarded_statement_date = None
        self._more_url = None
        self._attempts = None
        self._visible_after = None
        self._source = None
        self._target = None
        self._local_source = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if last_forwarded_statement_date is not None:
            self.last_forwarded_statement_date = last_forwarded_statement_date
        if more_url is not None:
            self.more_url = more_url
        if attempts is not None:
            self.attempts = attempts
        if visible_after is not None:
            self.visible_after = visible_after
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if local_source is not None:
            self.local_source = local_source

    @property
    def id(self):
        """Gets the id of this XapiStatementPipeSchema.  # noqa: E501


        :return: The id of this XapiStatementPipeSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XapiStatementPipeSchema.


        :param id: The id of this XapiStatementPipeSchema.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_forwarded_statement_date(self):
        """Gets the last_forwarded_statement_date of this XapiStatementPipeSchema.  # noqa: E501


        :return: The last_forwarded_statement_date of this XapiStatementPipeSchema.  # noqa: E501
        :rtype: str
        """
        return self._last_forwarded_statement_date

    @last_forwarded_statement_date.setter
    def last_forwarded_statement_date(self, last_forwarded_statement_date):
        """Sets the last_forwarded_statement_date of this XapiStatementPipeSchema.


        :param last_forwarded_statement_date: The last_forwarded_statement_date of this XapiStatementPipeSchema.  # noqa: E501
        :type: str
        """

        self._last_forwarded_statement_date = last_forwarded_statement_date

    @property
    def more_url(self):
        """Gets the more_url of this XapiStatementPipeSchema.  # noqa: E501


        :return: The more_url of this XapiStatementPipeSchema.  # noqa: E501
        :rtype: str
        """
        return self._more_url

    @more_url.setter
    def more_url(self, more_url):
        """Sets the more_url of this XapiStatementPipeSchema.


        :param more_url: The more_url of this XapiStatementPipeSchema.  # noqa: E501
        :type: str
        """

        self._more_url = more_url

    @property
    def attempts(self):
        """Gets the attempts of this XapiStatementPipeSchema.  # noqa: E501


        :return: The attempts of this XapiStatementPipeSchema.  # noqa: E501
        :rtype: int
        """
        return self._attempts

    @attempts.setter
    def attempts(self, attempts):
        """Sets the attempts of this XapiStatementPipeSchema.


        :param attempts: The attempts of this XapiStatementPipeSchema.  # noqa: E501
        :type: int
        """

        self._attempts = attempts

    @property
    def visible_after(self):
        """Gets the visible_after of this XapiStatementPipeSchema.  # noqa: E501


        :return: The visible_after of this XapiStatementPipeSchema.  # noqa: E501
        :rtype: str
        """
        return self._visible_after

    @visible_after.setter
    def visible_after(self, visible_after):
        """Sets the visible_after of this XapiStatementPipeSchema.


        :param visible_after: The visible_after of this XapiStatementPipeSchema.  # noqa: E501
        :type: str
        """

        self._visible_after = visible_after

    @property
    def source(self):
        """Gets the source of this XapiStatementPipeSchema.  # noqa: E501


        :return: The source of this XapiStatementPipeSchema.  # noqa: E501
        :rtype: XapiEndpointSchema
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this XapiStatementPipeSchema.


        :param source: The source of this XapiStatementPipeSchema.  # noqa: E501
        :type: XapiEndpointSchema
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this XapiStatementPipeSchema.  # noqa: E501


        :return: The target of this XapiStatementPipeSchema.  # noqa: E501
        :rtype: XapiEndpointSchema
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this XapiStatementPipeSchema.


        :param target: The target of this XapiStatementPipeSchema.  # noqa: E501
        :type: XapiEndpointSchema
        """

        self._target = target

    @property
    def local_source(self):
        """Gets the local_source of this XapiStatementPipeSchema.  # noqa: E501


        :return: The local_source of this XapiStatementPipeSchema.  # noqa: E501
        :rtype: XapiSelfSourcedPipeSchema
        """
        return self._local_source

    @local_source.setter
    def local_source(self, local_source):
        """Sets the local_source of this XapiStatementPipeSchema.


        :param local_source: The local_source of this XapiStatementPipeSchema.  # noqa: E501
        :type: XapiSelfSourcedPipeSchema
        """

        self._local_source = local_source

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
        if issubclass(XapiStatementPipeSchema, dict):
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
        if not isinstance(other, XapiStatementPipeSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
