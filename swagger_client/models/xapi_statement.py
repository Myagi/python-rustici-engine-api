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


class XapiStatement(object):
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
        'actor': 'XapiAgentGroup',
        'verb': 'XapiVerb',
        'object_activity': 'XapiActivity',
        'object_agent_group': 'XapiAgentGroup',
        'object_statement_reference': 'XapiStatementReference',
        'object_sub_statement': 'XapiStatement',
        'result': 'XapiResult',
        'context': 'XapiContext',
        'timestamp': 'datetime',
        'stored': 'datetime',
        'authority': 'XapiAgentGroup',
        'attachments': 'list[XapiAttachment]'
    }

    attribute_map = {
        'id': 'id',
        'actor': 'actor',
        'verb': 'verb',
        'object_activity': 'objectActivity',
        'object_agent_group': 'objectAgentGroup',
        'object_statement_reference': 'objectStatementReference',
        'object_sub_statement': 'objectSubStatement',
        'result': 'result',
        'context': 'context',
        'timestamp': 'timestamp',
        'stored': 'stored',
        'authority': 'authority',
        'attachments': 'attachments'
    }

    def __init__(self, id=None, actor=None, verb=None, object_activity=None, object_agent_group=None, object_statement_reference=None, object_sub_statement=None, result=None, context=None, timestamp=None, stored=None, authority=None, attachments=None):  # noqa: E501
        """XapiStatement - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._actor = None
        self._verb = None
        self._object_activity = None
        self._object_agent_group = None
        self._object_statement_reference = None
        self._object_sub_statement = None
        self._result = None
        self._context = None
        self._timestamp = None
        self._stored = None
        self._authority = None
        self._attachments = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if actor is not None:
            self.actor = actor
        if verb is not None:
            self.verb = verb
        if object_activity is not None:
            self.object_activity = object_activity
        if object_agent_group is not None:
            self.object_agent_group = object_agent_group
        if object_statement_reference is not None:
            self.object_statement_reference = object_statement_reference
        if object_sub_statement is not None:
            self.object_sub_statement = object_sub_statement
        if result is not None:
            self.result = result
        if context is not None:
            self.context = context
        if timestamp is not None:
            self.timestamp = timestamp
        if stored is not None:
            self.stored = stored
        if authority is not None:
            self.authority = authority
        if attachments is not None:
            self.attachments = attachments

    @property
    def id(self):
        """Gets the id of this XapiStatement.  # noqa: E501


        :return: The id of this XapiStatement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XapiStatement.


        :param id: The id of this XapiStatement.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def actor(self):
        """Gets the actor of this XapiStatement.  # noqa: E501


        :return: The actor of this XapiStatement.  # noqa: E501
        :rtype: XapiAgentGroup
        """
        return self._actor

    @actor.setter
    def actor(self, actor):
        """Sets the actor of this XapiStatement.


        :param actor: The actor of this XapiStatement.  # noqa: E501
        :type: XapiAgentGroup
        """

        self._actor = actor

    @property
    def verb(self):
        """Gets the verb of this XapiStatement.  # noqa: E501


        :return: The verb of this XapiStatement.  # noqa: E501
        :rtype: XapiVerb
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this XapiStatement.


        :param verb: The verb of this XapiStatement.  # noqa: E501
        :type: XapiVerb
        """

        self._verb = verb

    @property
    def object_activity(self):
        """Gets the object_activity of this XapiStatement.  # noqa: E501


        :return: The object_activity of this XapiStatement.  # noqa: E501
        :rtype: XapiActivity
        """
        return self._object_activity

    @object_activity.setter
    def object_activity(self, object_activity):
        """Sets the object_activity of this XapiStatement.


        :param object_activity: The object_activity of this XapiStatement.  # noqa: E501
        :type: XapiActivity
        """

        self._object_activity = object_activity

    @property
    def object_agent_group(self):
        """Gets the object_agent_group of this XapiStatement.  # noqa: E501


        :return: The object_agent_group of this XapiStatement.  # noqa: E501
        :rtype: XapiAgentGroup
        """
        return self._object_agent_group

    @object_agent_group.setter
    def object_agent_group(self, object_agent_group):
        """Sets the object_agent_group of this XapiStatement.


        :param object_agent_group: The object_agent_group of this XapiStatement.  # noqa: E501
        :type: XapiAgentGroup
        """

        self._object_agent_group = object_agent_group

    @property
    def object_statement_reference(self):
        """Gets the object_statement_reference of this XapiStatement.  # noqa: E501


        :return: The object_statement_reference of this XapiStatement.  # noqa: E501
        :rtype: XapiStatementReference
        """
        return self._object_statement_reference

    @object_statement_reference.setter
    def object_statement_reference(self, object_statement_reference):
        """Sets the object_statement_reference of this XapiStatement.


        :param object_statement_reference: The object_statement_reference of this XapiStatement.  # noqa: E501
        :type: XapiStatementReference
        """

        self._object_statement_reference = object_statement_reference

    @property
    def object_sub_statement(self):
        """Gets the object_sub_statement of this XapiStatement.  # noqa: E501


        :return: The object_sub_statement of this XapiStatement.  # noqa: E501
        :rtype: XapiStatement
        """
        return self._object_sub_statement

    @object_sub_statement.setter
    def object_sub_statement(self, object_sub_statement):
        """Sets the object_sub_statement of this XapiStatement.


        :param object_sub_statement: The object_sub_statement of this XapiStatement.  # noqa: E501
        :type: XapiStatement
        """

        self._object_sub_statement = object_sub_statement

    @property
    def result(self):
        """Gets the result of this XapiStatement.  # noqa: E501


        :return: The result of this XapiStatement.  # noqa: E501
        :rtype: XapiResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this XapiStatement.


        :param result: The result of this XapiStatement.  # noqa: E501
        :type: XapiResult
        """

        self._result = result

    @property
    def context(self):
        """Gets the context of this XapiStatement.  # noqa: E501


        :return: The context of this XapiStatement.  # noqa: E501
        :rtype: XapiContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this XapiStatement.


        :param context: The context of this XapiStatement.  # noqa: E501
        :type: XapiContext
        """

        self._context = context

    @property
    def timestamp(self):
        """Gets the timestamp of this XapiStatement.  # noqa: E501


        :return: The timestamp of this XapiStatement.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XapiStatement.


        :param timestamp: The timestamp of this XapiStatement.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def stored(self):
        """Gets the stored of this XapiStatement.  # noqa: E501


        :return: The stored of this XapiStatement.  # noqa: E501
        :rtype: datetime
        """
        return self._stored

    @stored.setter
    def stored(self, stored):
        """Sets the stored of this XapiStatement.


        :param stored: The stored of this XapiStatement.  # noqa: E501
        :type: datetime
        """

        self._stored = stored

    @property
    def authority(self):
        """Gets the authority of this XapiStatement.  # noqa: E501


        :return: The authority of this XapiStatement.  # noqa: E501
        :rtype: XapiAgentGroup
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """Sets the authority of this XapiStatement.


        :param authority: The authority of this XapiStatement.  # noqa: E501
        :type: XapiAgentGroup
        """

        self._authority = authority

    @property
    def attachments(self):
        """Gets the attachments of this XapiStatement.  # noqa: E501


        :return: The attachments of this XapiStatement.  # noqa: E501
        :rtype: list[XapiAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this XapiStatement.


        :param attachments: The attachments of this XapiStatement.  # noqa: E501
        :type: list[XapiAttachment]
        """

        self._attachments = attachments

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
        if issubclass(XapiStatement, dict):
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
        if not isinstance(other, XapiStatement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
