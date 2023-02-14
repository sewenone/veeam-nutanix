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

class RetentionSettings(object):
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
        'type': 'RetentionType',
        'restore_points_to_keep': 'int',
        'days_to_keep': 'int'
    }

    attribute_map = {
        'type': 'type',
        'restore_points_to_keep': 'restorePointsToKeep',
        'days_to_keep': 'daysToKeep'
    }

    def __init__(self, type=None, restore_points_to_keep=None, days_to_keep=None):  # noqa: E501
        """RetentionSettings - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._restore_points_to_keep = None
        self._days_to_keep = None
        self.discriminator = None
        self.type = type
        if restore_points_to_keep is not None:
            self.restore_points_to_keep = restore_points_to_keep
        if days_to_keep is not None:
            self.days_to_keep = days_to_keep

    @property
    def type(self):
        """Gets the type of this RetentionSettings.  # noqa: E501


        :return: The type of this RetentionSettings.  # noqa: E501
        :rtype: RetentionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RetentionSettings.


        :param type: The type of this RetentionSettings.  # noqa: E501
        :type: RetentionType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def restore_points_to_keep(self):
        """Gets the restore_points_to_keep of this RetentionSettings.  # noqa: E501

        Number of restore points to keep in a backup chain.  # noqa: E501

        :return: The restore_points_to_keep of this RetentionSettings.  # noqa: E501
        :rtype: int
        """
        return self._restore_points_to_keep

    @restore_points_to_keep.setter
    def restore_points_to_keep(self, restore_points_to_keep):
        """Sets the restore_points_to_keep of this RetentionSettings.

        Number of restore points to keep in a backup chain.  # noqa: E501

        :param restore_points_to_keep: The restore_points_to_keep of this RetentionSettings.  # noqa: E501
        :type: int
        """

        self._restore_points_to_keep = restore_points_to_keep

    @property
    def days_to_keep(self):
        """Gets the days_to_keep of this RetentionSettings.  # noqa: E501

        Number of days to keep restore points in a backup chain.  # noqa: E501

        :return: The days_to_keep of this RetentionSettings.  # noqa: E501
        :rtype: int
        """
        return self._days_to_keep

    @days_to_keep.setter
    def days_to_keep(self, days_to_keep):
        """Sets the days_to_keep of this RetentionSettings.

        Number of days to keep restore points in a backup chain.  # noqa: E501

        :param days_to_keep: The days_to_keep of this RetentionSettings.  # noqa: E501
        :type: int
        """

        self._days_to_keep = days_to_keep

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
        if issubclass(RetentionSettings, dict):
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
        if not isinstance(other, RetentionSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
