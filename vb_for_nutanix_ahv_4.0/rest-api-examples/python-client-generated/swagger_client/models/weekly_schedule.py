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

class WeeklySchedule(object):
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
        'start_time': 'str',
        'configured_days': 'ConfiguredDays',
        'selected_days': 'list[DayOfWeek]'
    }

    attribute_map = {
        'start_time': 'startTime',
        'configured_days': 'configuredDays',
        'selected_days': 'selectedDays'
    }

    def __init__(self, start_time='10:00', configured_days=None, selected_days=None):  # noqa: E501
        """WeeklySchedule - a model defined in Swagger"""  # noqa: E501
        self._start_time = None
        self._configured_days = None
        self._selected_days = None
        self.discriminator = None
        if start_time is not None:
            self.start_time = start_time
        if configured_days is not None:
            self.configured_days = configured_days
        if selected_days is not None:
            self.selected_days = selected_days

    @property
    def start_time(self):
        """Gets the start_time of this WeeklySchedule.  # noqa: E501

        Time when the job must run.  # noqa: E501

        :return: The start_time of this WeeklySchedule.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this WeeklySchedule.

        Time when the job must run.  # noqa: E501

        :param start_time: The start_time of this WeeklySchedule.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def configured_days(self):
        """Gets the configured_days of this WeeklySchedule.  # noqa: E501


        :return: The configured_days of this WeeklySchedule.  # noqa: E501
        :rtype: ConfiguredDays
        """
        return self._configured_days

    @configured_days.setter
    def configured_days(self, configured_days):
        """Sets the configured_days of this WeeklySchedule.


        :param configured_days: The configured_days of this WeeklySchedule.  # noqa: E501
        :type: ConfiguredDays
        """

        self._configured_days = configured_days

    @property
    def selected_days(self):
        """Gets the selected_days of this WeeklySchedule.  # noqa: E501

        Days when the job must run.  # noqa: E501

        :return: The selected_days of this WeeklySchedule.  # noqa: E501
        :rtype: list[DayOfWeek]
        """
        return self._selected_days

    @selected_days.setter
    def selected_days(self, selected_days):
        """Sets the selected_days of this WeeklySchedule.

        Days when the job must run.  # noqa: E501

        :param selected_days: The selected_days of this WeeklySchedule.  # noqa: E501
        :type: list[DayOfWeek]
        """

        self._selected_days = selected_days

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
        if issubclass(WeeklySchedule, dict):
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
        if not isinstance(other, WeeklySchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
