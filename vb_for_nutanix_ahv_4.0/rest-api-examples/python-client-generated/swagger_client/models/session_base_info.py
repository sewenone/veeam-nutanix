# coding: utf-8

"""
    Veeam Backup for Nutanix AHV REST API 4.0

    This REST API reference lists types of Veeam Backup for Nutanix AHV entities,  and contains description of collections and resources which stand for these entities.  Every resource has a JSON object model and includes application data and REST API metadata.  Application data is represented by properties associated with Veeam Backup for Nutanix AHV entities.  REST API metadata is represented by properties specific to the REST API, such as resource IDs, URLs and relationships.  The reference also includes methods that represent operations available to a resource or collection.   # noqa: E501

    OpenAPI spec version: V4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SessionBaseInfo(object):
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
        'name': 'str',
        'session_type': 'SessionType',
        'state': 'SessionState',
        'result': 'SessionResult',
        'job_name': 'str',
        'objects_count': 'int',
        'start_time_utc': 'datetime',
        'finish_time_utc': 'datetime',
        'reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'session_type': 'sessionType',
        'state': 'state',
        'result': 'result',
        'job_name': 'jobName',
        'objects_count': 'objectsCount',
        'start_time_utc': 'startTimeUtc',
        'finish_time_utc': 'finishTimeUtc',
        'reason': 'reason'
    }

    def __init__(self, id=None, name=None, session_type=None, state=None, result=None, job_name=None, objects_count=None, start_time_utc=None, finish_time_utc=None, reason=None):  # noqa: E501
        """SessionBaseInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._session_type = None
        self._state = None
        self._result = None
        self._job_name = None
        self._objects_count = None
        self._start_time_utc = None
        self._finish_time_utc = None
        self._reason = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if session_type is not None:
            self.session_type = session_type
        if state is not None:
            self.state = state
        if result is not None:
            self.result = result
        if job_name is not None:
            self.job_name = job_name
        if objects_count is not None:
            self.objects_count = objects_count
        if start_time_utc is not None:
            self.start_time_utc = start_time_utc
        if finish_time_utc is not None:
            self.finish_time_utc = finish_time_utc
        if reason is not None:
            self.reason = reason

    @property
    def id(self):
        """Gets the id of this SessionBaseInfo.  # noqa: E501

        System ID assigned to a session in the Veeam Backup for Nutanix AHV.  # noqa: E501

        :return: The id of this SessionBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SessionBaseInfo.

        System ID assigned to a session in the Veeam Backup for Nutanix AHV.  # noqa: E501

        :param id: The id of this SessionBaseInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SessionBaseInfo.  # noqa: E501

        Name of the session.  # noqa: E501

        :return: The name of this SessionBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SessionBaseInfo.

        Name of the session.  # noqa: E501

        :param name: The name of this SessionBaseInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def session_type(self):
        """Gets the session_type of this SessionBaseInfo.  # noqa: E501


        :return: The session_type of this SessionBaseInfo.  # noqa: E501
        :rtype: SessionType
        """
        return self._session_type

    @session_type.setter
    def session_type(self, session_type):
        """Sets the session_type of this SessionBaseInfo.


        :param session_type: The session_type of this SessionBaseInfo.  # noqa: E501
        :type: SessionType
        """

        self._session_type = session_type

    @property
    def state(self):
        """Gets the state of this SessionBaseInfo.  # noqa: E501


        :return: The state of this SessionBaseInfo.  # noqa: E501
        :rtype: SessionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SessionBaseInfo.


        :param state: The state of this SessionBaseInfo.  # noqa: E501
        :type: SessionState
        """

        self._state = state

    @property
    def result(self):
        """Gets the result of this SessionBaseInfo.  # noqa: E501


        :return: The result of this SessionBaseInfo.  # noqa: E501
        :rtype: SessionResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this SessionBaseInfo.


        :param result: The result of this SessionBaseInfo.  # noqa: E501
        :type: SessionResult
        """

        self._result = result

    @property
    def job_name(self):
        """Gets the job_name of this SessionBaseInfo.  # noqa: E501

        Name of the job related to the session.  # noqa: E501

        :return: The job_name of this SessionBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this SessionBaseInfo.

        Name of the job related to the session.  # noqa: E501

        :param job_name: The job_name of this SessionBaseInfo.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def objects_count(self):
        """Gets the objects_count of this SessionBaseInfo.  # noqa: E501

        Number of objects processed in the session.  # noqa: E501

        :return: The objects_count of this SessionBaseInfo.  # noqa: E501
        :rtype: int
        """
        return self._objects_count

    @objects_count.setter
    def objects_count(self, objects_count):
        """Sets the objects_count of this SessionBaseInfo.

        Number of objects processed in the session.  # noqa: E501

        :param objects_count: The objects_count of this SessionBaseInfo.  # noqa: E501
        :type: int
        """

        self._objects_count = objects_count

    @property
    def start_time_utc(self):
        """Gets the start_time_utc of this SessionBaseInfo.  # noqa: E501

        Date and time when the session started.  # noqa: E501

        :return: The start_time_utc of this SessionBaseInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time_utc

    @start_time_utc.setter
    def start_time_utc(self, start_time_utc):
        """Sets the start_time_utc of this SessionBaseInfo.

        Date and time when the session started.  # noqa: E501

        :param start_time_utc: The start_time_utc of this SessionBaseInfo.  # noqa: E501
        :type: datetime
        """

        self._start_time_utc = start_time_utc

    @property
    def finish_time_utc(self):
        """Gets the finish_time_utc of this SessionBaseInfo.  # noqa: E501

        Date and time when the session finished or stopped.  # noqa: E501

        :return: The finish_time_utc of this SessionBaseInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._finish_time_utc

    @finish_time_utc.setter
    def finish_time_utc(self, finish_time_utc):
        """Sets the finish_time_utc of this SessionBaseInfo.

        Date and time when the session finished or stopped.  # noqa: E501

        :param finish_time_utc: The finish_time_utc of this SessionBaseInfo.  # noqa: E501
        :type: datetime
        """

        self._finish_time_utc = finish_time_utc

    @property
    def reason(self):
        """Gets the reason of this SessionBaseInfo.  # noqa: E501

        Reason for the restore operation.  # noqa: E501

        :return: The reason of this SessionBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this SessionBaseInfo.

        Reason for the restore operation.  # noqa: E501

        :param reason: The reason of this SessionBaseInfo.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if issubclass(SessionBaseInfo, dict):
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
        if not isinstance(other, SessionBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
