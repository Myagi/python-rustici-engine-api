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


class CreateRegistrationSchema(object):
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
        'course_id': 'str',
        'learner': 'LearnerSchema',
        'registration_id': 'str',
        'for_credit': 'bool',
        'xapi_registration_id': 'str',
        'post_back': 'PostBackSchema',
        'initial_registration_state': 'RegistrationSchema',
        'initial_settings': 'SettingsPostSchema'
    }

    attribute_map = {
        'course_id': 'courseId',
        'learner': 'learner',
        'registration_id': 'registrationId',
        'for_credit': 'forCredit',
        'xapi_registration_id': 'xapiRegistrationId',
        'post_back': 'postBack',
        'initial_registration_state': 'initialRegistrationState',
        'initial_settings': 'initialSettings'
    }

    def __init__(self, course_id=None, learner=None, registration_id=None, for_credit=True, xapi_registration_id=None, post_back=None, initial_registration_state=None, initial_settings=None):  # noqa: E501
        """CreateRegistrationSchema - a model defined in Swagger"""  # noqa: E501
        self._course_id = None
        self._learner = None
        self._registration_id = None
        self._for_credit = None
        self._xapi_registration_id = None
        self._post_back = None
        self._initial_registration_state = None
        self._initial_settings = None
        self.discriminator = None
        self.course_id = course_id
        self.learner = learner
        self.registration_id = registration_id
        if for_credit is not None:
            self.for_credit = for_credit
        if xapi_registration_id is not None:
            self.xapi_registration_id = xapi_registration_id
        if post_back is not None:
            self.post_back = post_back
        if initial_registration_state is not None:
            self.initial_registration_state = initial_registration_state
        if initial_settings is not None:
            self.initial_settings = initial_settings

    @property
    def course_id(self):
        """Gets the course_id of this CreateRegistrationSchema.  # noqa: E501


        :return: The course_id of this CreateRegistrationSchema.  # noqa: E501
        :rtype: str
        """
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        """Sets the course_id of this CreateRegistrationSchema.


        :param course_id: The course_id of this CreateRegistrationSchema.  # noqa: E501
        :type: str
        """
        if course_id is None:
            raise ValueError("Invalid value for `course_id`, must not be `None`")  # noqa: E501

        self._course_id = course_id

    @property
    def learner(self):
        """Gets the learner of this CreateRegistrationSchema.  # noqa: E501


        :return: The learner of this CreateRegistrationSchema.  # noqa: E501
        :rtype: LearnerSchema
        """
        return self._learner

    @learner.setter
    def learner(self, learner):
        """Sets the learner of this CreateRegistrationSchema.


        :param learner: The learner of this CreateRegistrationSchema.  # noqa: E501
        :type: LearnerSchema
        """
        if learner is None:
            raise ValueError("Invalid value for `learner`, must not be `None`")  # noqa: E501

        self._learner = learner

    @property
    def registration_id(self):
        """Gets the registration_id of this CreateRegistrationSchema.  # noqa: E501


        :return: The registration_id of this CreateRegistrationSchema.  # noqa: E501
        :rtype: str
        """
        return self._registration_id

    @registration_id.setter
    def registration_id(self, registration_id):
        """Sets the registration_id of this CreateRegistrationSchema.


        :param registration_id: The registration_id of this CreateRegistrationSchema.  # noqa: E501
        :type: str
        """
        if registration_id is None:
            raise ValueError("Invalid value for `registration_id`, must not be `None`")  # noqa: E501

        self._registration_id = registration_id

    @property
    def for_credit(self):
        """Gets the for_credit of this CreateRegistrationSchema.  # noqa: E501


        :return: The for_credit of this CreateRegistrationSchema.  # noqa: E501
        :rtype: bool
        """
        return self._for_credit

    @for_credit.setter
    def for_credit(self, for_credit):
        """Sets the for_credit of this CreateRegistrationSchema.


        :param for_credit: The for_credit of this CreateRegistrationSchema.  # noqa: E501
        :type: bool
        """

        self._for_credit = for_credit

    @property
    def xapi_registration_id(self):
        """Gets the xapi_registration_id of this CreateRegistrationSchema.  # noqa: E501


        :return: The xapi_registration_id of this CreateRegistrationSchema.  # noqa: E501
        :rtype: str
        """
        return self._xapi_registration_id

    @xapi_registration_id.setter
    def xapi_registration_id(self, xapi_registration_id):
        """Sets the xapi_registration_id of this CreateRegistrationSchema.


        :param xapi_registration_id: The xapi_registration_id of this CreateRegistrationSchema.  # noqa: E501
        :type: str
        """

        self._xapi_registration_id = xapi_registration_id

    @property
    def post_back(self):
        """Gets the post_back of this CreateRegistrationSchema.  # noqa: E501


        :return: The post_back of this CreateRegistrationSchema.  # noqa: E501
        :rtype: PostBackSchema
        """
        return self._post_back

    @post_back.setter
    def post_back(self, post_back):
        """Sets the post_back of this CreateRegistrationSchema.


        :param post_back: The post_back of this CreateRegistrationSchema.  # noqa: E501
        :type: PostBackSchema
        """

        self._post_back = post_back

    @property
    def initial_registration_state(self):
        """Gets the initial_registration_state of this CreateRegistrationSchema.  # noqa: E501


        :return: The initial_registration_state of this CreateRegistrationSchema.  # noqa: E501
        :rtype: RegistrationSchema
        """
        return self._initial_registration_state

    @initial_registration_state.setter
    def initial_registration_state(self, initial_registration_state):
        """Sets the initial_registration_state of this CreateRegistrationSchema.


        :param initial_registration_state: The initial_registration_state of this CreateRegistrationSchema.  # noqa: E501
        :type: RegistrationSchema
        """

        self._initial_registration_state = initial_registration_state

    @property
    def initial_settings(self):
        """Gets the initial_settings of this CreateRegistrationSchema.  # noqa: E501


        :return: The initial_settings of this CreateRegistrationSchema.  # noqa: E501
        :rtype: SettingsPostSchema
        """
        return self._initial_settings

    @initial_settings.setter
    def initial_settings(self, initial_settings):
        """Sets the initial_settings of this CreateRegistrationSchema.


        :param initial_settings: The initial_settings of this CreateRegistrationSchema.  # noqa: E501
        :type: SettingsPostSchema
        """

        self._initial_settings = initial_settings

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
        if issubclass(CreateRegistrationSchema, dict):
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
        if not isinstance(other, CreateRegistrationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
