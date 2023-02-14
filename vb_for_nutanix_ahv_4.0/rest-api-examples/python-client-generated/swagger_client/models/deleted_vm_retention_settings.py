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

class DeletedVmRetentionSettings(object):
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
        'enabled': 'bool',
        'days': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'days': 'days'
    }

    def __init__(self, enabled=None, days=None):  # noqa: E501
        """DeletedVmRetentionSettings - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._days = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if days is not None:
            self.days = days

    @property
    def enabled(self):
        """Gets the enabled of this DeletedVmRetentionSettings.  # noqa: E501

        Defines whether backups of VMs that are no longer included in the backup job should be deleted.  # noqa: E501

        :return: The enabled of this DeletedVmRetentionSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DeletedVmRetentionSettings.

        Defines whether backups of VMs that are no longer included in the backup job should be deleted.  # noqa: E501

        :param enabled: The enabled of this DeletedVmRetentionSettings.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def days(self):
        """Gets the days of this DeletedVmRetentionSettings.  # noqa: E501

        Number of days to keep the backups.  # noqa: E501

        :return: The days of this DeletedVmRetentionSettings.  # noqa: E501
        :rtype: int
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this DeletedVmRetentionSettings.

        Number of days to keep the backups.  # noqa: E501

        :param days: The days of this DeletedVmRetentionSettings.  # noqa: E501
        :type: int
        """

        self._days = days

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
        if issubclass(DeletedVmRetentionSettings, dict):
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
        if not isinstance(other, DeletedVmRetentionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
