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


class CourseSchema(object):
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
        'title': 'str',
        'xapi_activity_id': 'str',
        'updated': 'datetime',
        'web_path': 'str',
        'version': 'int',
        'registration_count': 'int',
        'activity_id': 'str',
        'course_learning_standard': 'str',
        'connector': 'CourseConnectorSchema',
        'metadata': 'MetadataSchema',
        'root_activity': 'CourseActivitySchema'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'xapi_activity_id': 'xapiActivityId',
        'updated': 'updated',
        'web_path': 'webPath',
        'version': 'version',
        'registration_count': 'registrationCount',
        'activity_id': 'activityId',
        'course_learning_standard': 'courseLearningStandard',
        'connector': 'connector',
        'metadata': 'metadata',
        'root_activity': 'rootActivity'
    }

    def __init__(self, id=None, title=None, xapi_activity_id=None, updated=None, web_path=None, version=None, registration_count=None, activity_id=None, course_learning_standard=None, connector=None, metadata=None, root_activity=None):  # noqa: E501
        """CourseSchema - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._xapi_activity_id = None
        self._updated = None
        self._web_path = None
        self._version = None
        self._registration_count = None
        self._activity_id = None
        self._course_learning_standard = None
        self._connector = None
        self._metadata = None
        self._root_activity = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if xapi_activity_id is not None:
            self.xapi_activity_id = xapi_activity_id
        if updated is not None:
            self.updated = updated
        if web_path is not None:
            self.web_path = web_path
        if version is not None:
            self.version = version
        if registration_count is not None:
            self.registration_count = registration_count
        if activity_id is not None:
            self.activity_id = activity_id
        if course_learning_standard is not None:
            self.course_learning_standard = course_learning_standard
        if connector is not None:
            self.connector = connector
        if metadata is not None:
            self.metadata = metadata
        if root_activity is not None:
            self.root_activity = root_activity

    @property
    def id(self):
        """Gets the id of this CourseSchema.  # noqa: E501


        :return: The id of this CourseSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CourseSchema.


        :param id: The id of this CourseSchema.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this CourseSchema.  # noqa: E501


        :return: The title of this CourseSchema.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CourseSchema.


        :param title: The title of this CourseSchema.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def xapi_activity_id(self):
        """Gets the xapi_activity_id of this CourseSchema.  # noqa: E501

        xAPI activity id associated with this course  # noqa: E501

        :return: The xapi_activity_id of this CourseSchema.  # noqa: E501
        :rtype: str
        """
        return self._xapi_activity_id

    @xapi_activity_id.setter
    def xapi_activity_id(self, xapi_activity_id):
        """Sets the xapi_activity_id of this CourseSchema.

        xAPI activity id associated with this course  # noqa: E501

        :param xapi_activity_id: The xapi_activity_id of this CourseSchema.  # noqa: E501
        :type: str
        """

        self._xapi_activity_id = xapi_activity_id

    @property
    def updated(self):
        """Gets the updated of this CourseSchema.  # noqa: E501


        :return: The updated of this CourseSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this CourseSchema.


        :param updated: The updated of this CourseSchema.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def web_path(self):
        """Gets the web_path of this CourseSchema.  # noqa: E501

        The web path at which the course's contents are hosted. For AICC courses, refer to the href property of the child activities as this value will not be available.  # noqa: E501

        :return: The web_path of this CourseSchema.  # noqa: E501
        :rtype: str
        """
        return self._web_path

    @web_path.setter
    def web_path(self, web_path):
        """Sets the web_path of this CourseSchema.

        The web path at which the course's contents are hosted. For AICC courses, refer to the href property of the child activities as this value will not be available.  # noqa: E501

        :param web_path: The web_path of this CourseSchema.  # noqa: E501
        :type: str
        """

        self._web_path = web_path

    @property
    def version(self):
        """Gets the version of this CourseSchema.  # noqa: E501


        :return: The version of this CourseSchema.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CourseSchema.


        :param version: The version of this CourseSchema.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def registration_count(self):
        """Gets the registration_count of this CourseSchema.  # noqa: E501


        :return: The registration_count of this CourseSchema.  # noqa: E501
        :rtype: int
        """
        return self._registration_count

    @registration_count.setter
    def registration_count(self, registration_count):
        """Sets the registration_count of this CourseSchema.


        :param registration_count: The registration_count of this CourseSchema.  # noqa: E501
        :type: int
        """

        self._registration_count = registration_count

    @property
    def activity_id(self):
        """Gets the activity_id of this CourseSchema.  # noqa: E501


        :return: The activity_id of this CourseSchema.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this CourseSchema.


        :param activity_id: The activity_id of this CourseSchema.  # noqa: E501
        :type: str
        """

        self._activity_id = activity_id

    @property
    def course_learning_standard(self):
        """Gets the course_learning_standard of this CourseSchema.  # noqa: E501


        :return: The course_learning_standard of this CourseSchema.  # noqa: E501
        :rtype: str
        """
        return self._course_learning_standard

    @course_learning_standard.setter
    def course_learning_standard(self, course_learning_standard):
        """Sets the course_learning_standard of this CourseSchema.


        :param course_learning_standard: The course_learning_standard of this CourseSchema.  # noqa: E501
        :type: str
        """
        allowed_values = ["SCORM11", "SCORM12", "SCORM20042NDEDITION", "SCORM20043RDEDITION", "SCORM20044THEDITION", "AICC", "XAPI", "CMI5"]  # noqa: E501
        if course_learning_standard not in allowed_values:
            raise ValueError(
                "Invalid value for `course_learning_standard` ({0}), must be one of {1}"  # noqa: E501
                .format(course_learning_standard, allowed_values)
            )

        self._course_learning_standard = course_learning_standard

    @property
    def connector(self):
        """Gets the connector of this CourseSchema.  # noqa: E501


        :return: The connector of this CourseSchema.  # noqa: E501
        :rtype: CourseConnectorSchema
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """Sets the connector of this CourseSchema.


        :param connector: The connector of this CourseSchema.  # noqa: E501
        :type: CourseConnectorSchema
        """

        self._connector = connector

    @property
    def metadata(self):
        """Gets the metadata of this CourseSchema.  # noqa: E501


        :return: The metadata of this CourseSchema.  # noqa: E501
        :rtype: MetadataSchema
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CourseSchema.


        :param metadata: The metadata of this CourseSchema.  # noqa: E501
        :type: MetadataSchema
        """

        self._metadata = metadata

    @property
    def root_activity(self):
        """Gets the root_activity of this CourseSchema.  # noqa: E501


        :return: The root_activity of this CourseSchema.  # noqa: E501
        :rtype: CourseActivitySchema
        """
        return self._root_activity

    @root_activity.setter
    def root_activity(self, root_activity):
        """Sets the root_activity of this CourseSchema.


        :param root_activity: The root_activity of this CourseSchema.  # noqa: E501
        :type: CourseActivitySchema
        """

        self._root_activity = root_activity

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
        if issubclass(CourseSchema, dict):
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
        if not isinstance(other, CourseSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
