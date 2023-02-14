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

class MonthlySchedule(object):
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
        'configured_week_or_day': 'ConfiguredWeekOrDay',
        'day_of_week': 'DayOfWeek',
        'day_of_month': 'int',
        'months': 'list[Month]'
    }

    attribute_map = {
        'start_time': 'startTime',
        'configured_week_or_day': 'configuredWeekOrDay',
        'day_of_week': 'dayOfWeek',
        'day_of_month': 'dayOfMonth',
        'months': 'months'
    }

    def __init__(self, start_time='10:00', configured_week_or_day=None, day_of_week=None, day_of_month=None, months=None):  # noqa: E501
        """MonthlySchedule - a model defined in Swagger"""  # noqa: E501
        self._start_time = None
        self._configured_week_or_day = None
        self._day_of_week = None
        self._day_of_month = None
        self._months = None
        self.discriminator = None
        if start_time is not None:
            self.start_time = start_time
        if configured_week_or_day is not None:
            self.configured_week_or_day = configured_week_or_day
        if day_of_week is not None:
            self.day_of_week = day_of_week
        if day_of_month is not None:
            self.day_of_month = day_of_month
        if months is not None:
            self.months = months

    @property
    def start_time(self):
        """Gets the start_time of this MonthlySchedule.  # noqa: E501

        Time when the job must run.  # noqa: E501

        :return: The start_time of this MonthlySchedule.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this MonthlySchedule.

        Time when the job must run.  # noqa: E501

        :param start_time: The start_time of this MonthlySchedule.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def configured_week_or_day(self):
        """Gets the configured_week_or_day of this MonthlySchedule.  # noqa: E501


        :return: The configured_week_or_day of this MonthlySchedule.  # noqa: E501
        :rtype: ConfiguredWeekOrDay
        """
        return self._configured_week_or_day

    @configured_week_or_day.setter
    def configured_week_or_day(self, configured_week_or_day):
        """Sets the configured_week_or_day of this MonthlySchedule.


        :param configured_week_or_day: The configured_week_or_day of this MonthlySchedule.  # noqa: E501
        :type: ConfiguredWeekOrDay
        """

        self._configured_week_or_day = configured_week_or_day

    @property
    def day_of_week(self):
        """Gets the day_of_week of this MonthlySchedule.  # noqa: E501


        :return: The day_of_week of this MonthlySchedule.  # noqa: E501
        :rtype: DayOfWeek
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this MonthlySchedule.


        :param day_of_week: The day_of_week of this MonthlySchedule.  # noqa: E501
        :type: DayOfWeek
        """

        self._day_of_week = day_of_week

    @property
    def day_of_month(self):
        """Gets the day_of_month of this MonthlySchedule.  # noqa: E501

        Day of month when the job must run.  # noqa: E501

        :return: The day_of_month of this MonthlySchedule.  # noqa: E501
        :rtype: int
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """Sets the day_of_month of this MonthlySchedule.

        Day of month when the job must run.  # noqa: E501

        :param day_of_month: The day_of_month of this MonthlySchedule.  # noqa: E501
        :type: int
        """

        self._day_of_month = day_of_month

    @property
    def months(self):
        """Gets the months of this MonthlySchedule.  # noqa: E501

        Months when the job must run.  # noqa: E501

        :return: The months of this MonthlySchedule.  # noqa: E501
        :rtype: list[Month]
        """
        return self._months

    @months.setter
    def months(self, months):
        """Sets the months of this MonthlySchedule.

        Months when the job must run.  # noqa: E501

        :param months: The months of this MonthlySchedule.  # noqa: E501
        :type: list[Month]
        """

        self._months = months

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
        if issubclass(MonthlySchedule, dict):
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
        if not isinstance(other, MonthlySchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
