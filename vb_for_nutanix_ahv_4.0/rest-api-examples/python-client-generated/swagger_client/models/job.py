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

class Job(object):
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
        'description': 'str',
        'mode': 'JobMode',
        'settings': 'JobSettings',
        'status': 'JobStatus',
        'objects': 'int',
        'next_run_info': 'str',
        'next_run_utc': 'datetime',
        'last_run_utc': 'datetime',
        'last_session_id': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'mode': 'mode',
        'settings': 'settings',
        'status': 'status',
        'objects': 'objects',
        'next_run_info': 'nextRunInfo',
        'next_run_utc': 'nextRunUtc',
        'last_run_utc': 'lastRunUtc',
        'last_session_id': 'lastSessionId',
        'enabled': 'enabled'
    }

    def __init__(self, id=None, name=None, description=None, mode=None, settings=None, status=None, objects=None, next_run_info=None, next_run_utc=None, last_run_utc=None, last_session_id=None, enabled=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._mode = None
        self._settings = None
        self._status = None
        self._objects = None
        self._next_run_info = None
        self._next_run_utc = None
        self._last_run_utc = None
        self._last_session_id = None
        self._enabled = None
        self.discriminator = None
        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.mode = mode
        self.settings = settings
        if status is not None:
            self.status = status
        if objects is not None:
            self.objects = objects
        if next_run_info is not None:
            self.next_run_info = next_run_info
        if next_run_utc is not None:
            self.next_run_utc = next_run_utc
        if last_run_utc is not None:
            self.last_run_utc = last_run_utc
        if last_session_id is not None:
            self.last_session_id = last_session_id
        if enabled is not None:
            self.enabled = enabled

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501

        System ID assigned to a job in the Veeam Backup for Nutanix AHV.  # noqa: E501

        :return: The id of this Job.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        System ID assigned to a job in the Veeam Backup for Nutanix AHV.  # noqa: E501

        :param id: The id of this Job.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Job.  # noqa: E501

        Name of the job.  # noqa: E501

        :return: The name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        Name of the job.  # noqa: E501

        :param name: The name of this Job.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Job.  # noqa: E501

        Description of the job.  # noqa: E501

        :return: The description of this Job.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Job.

        Description of the job.  # noqa: E501

        :param description: The description of this Job.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def mode(self):
        """Gets the mode of this Job.  # noqa: E501


        :return: The mode of this Job.  # noqa: E501
        :rtype: JobMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Job.


        :param mode: The mode of this Job.  # noqa: E501
        :type: JobMode
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def settings(self):
        """Gets the settings of this Job.  # noqa: E501


        :return: The settings of this Job.  # noqa: E501
        :rtype: JobSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Job.


        :param settings: The settings of this Job.  # noqa: E501
        :type: JobSettings
        """
        if settings is None:
            raise ValueError("Invalid value for `settings`, must not be `None`")  # noqa: E501

        self._settings = settings

    @property
    def status(self):
        """Gets the status of this Job.  # noqa: E501


        :return: The status of this Job.  # noqa: E501
        :rtype: JobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.


        :param status: The status of this Job.  # noqa: E501
        :type: JobStatus
        """

        self._status = status

    @property
    def objects(self):
        """Gets the objects of this Job.  # noqa: E501

        Total number of objects added to the job.  # noqa: E501

        :return: The objects of this Job.  # noqa: E501
        :rtype: int
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this Job.

        Total number of objects added to the job.  # noqa: E501

        :param objects: The objects of this Job.  # noqa: E501
        :type: int
        """

        self._objects = objects

    @property
    def next_run_info(self):
        """Gets the next_run_info of this Job.  # noqa: E501

        Job run type (manual or automatic).  # noqa: E501

        :return: The next_run_info of this Job.  # noqa: E501
        :rtype: str
        """
        return self._next_run_info

    @next_run_info.setter
    def next_run_info(self, next_run_info):
        """Sets the next_run_info of this Job.

        Job run type (manual or automatic).  # noqa: E501

        :param next_run_info: The next_run_info of this Job.  # noqa: E501
        :type: str
        """

        self._next_run_info = next_run_info

    @property
    def next_run_utc(self):
        """Gets the next_run_utc of this Job.  # noqa: E501

        Date and time of the next planned job run.  # noqa: E501

        :return: The next_run_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._next_run_utc

    @next_run_utc.setter
    def next_run_utc(self, next_run_utc):
        """Sets the next_run_utc of this Job.

        Date and time of the next planned job run.  # noqa: E501

        :param next_run_utc: The next_run_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._next_run_utc = next_run_utc

    @property
    def last_run_utc(self):
        """Gets the last_run_utc of this Job.  # noqa: E501

        Date and time of the latest job run.  # noqa: E501

        :return: The last_run_utc of this Job.  # noqa: E501
        :rtype: datetime
        """
        return self._last_run_utc

    @last_run_utc.setter
    def last_run_utc(self, last_run_utc):
        """Sets the last_run_utc of this Job.

        Date and time of the latest job run.  # noqa: E501

        :param last_run_utc: The last_run_utc of this Job.  # noqa: E501
        :type: datetime
        """

        self._last_run_utc = last_run_utc

    @property
    def last_session_id(self):
        """Gets the last_session_id of this Job.  # noqa: E501

        System ID assigned to the latest job session.  # noqa: E501

        :return: The last_session_id of this Job.  # noqa: E501
        :rtype: str
        """
        return self._last_session_id

    @last_session_id.setter
    def last_session_id(self, last_session_id):
        """Sets the last_session_id of this Job.

        System ID assigned to the latest job session.  # noqa: E501

        :param last_session_id: The last_session_id of this Job.  # noqa: E501
        :type: str
        """

        self._last_session_id = last_session_id

    @property
    def enabled(self):
        """Gets the enabled of this Job.  # noqa: E501

        Defines whether the job is enabled.  # noqa: E501

        :return: The enabled of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Job.

        Defines whether the job is enabled.  # noqa: E501

        :param enabled: The enabled of this Job.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(Job, dict):
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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
