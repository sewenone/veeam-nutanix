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

class SystemMonitoringInfo(object):
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
        'cpu_usage_info': 'list[CpuUsageInfo]',
        'memory_usage_info': 'list[MemoryUsageInfo]',
        'storage_usage_info': 'list[StorageUsageInfo]'
    }

    attribute_map = {
        'cpu_usage_info': 'cpuUsageInfo',
        'memory_usage_info': 'memoryUsageInfo',
        'storage_usage_info': 'storageUsageInfo'
    }

    def __init__(self, cpu_usage_info=None, memory_usage_info=None, storage_usage_info=None):  # noqa: E501
        """SystemMonitoringInfo - a model defined in Swagger"""  # noqa: E501
        self._cpu_usage_info = None
        self._memory_usage_info = None
        self._storage_usage_info = None
        self.discriminator = None
        if cpu_usage_info is not None:
            self.cpu_usage_info = cpu_usage_info
        if memory_usage_info is not None:
            self.memory_usage_info = memory_usage_info
        if storage_usage_info is not None:
            self.storage_usage_info = storage_usage_info

    @property
    def cpu_usage_info(self):
        """Gets the cpu_usage_info of this SystemMonitoringInfo.  # noqa: E501

        CPU utilization records.  # noqa: E501

        :return: The cpu_usage_info of this SystemMonitoringInfo.  # noqa: E501
        :rtype: list[CpuUsageInfo]
        """
        return self._cpu_usage_info

    @cpu_usage_info.setter
    def cpu_usage_info(self, cpu_usage_info):
        """Sets the cpu_usage_info of this SystemMonitoringInfo.

        CPU utilization records.  # noqa: E501

        :param cpu_usage_info: The cpu_usage_info of this SystemMonitoringInfo.  # noqa: E501
        :type: list[CpuUsageInfo]
        """

        self._cpu_usage_info = cpu_usage_info

    @property
    def memory_usage_info(self):
        """Gets the memory_usage_info of this SystemMonitoringInfo.  # noqa: E501

        RAM consumption records.  # noqa: E501

        :return: The memory_usage_info of this SystemMonitoringInfo.  # noqa: E501
        :rtype: list[MemoryUsageInfo]
        """
        return self._memory_usage_info

    @memory_usage_info.setter
    def memory_usage_info(self, memory_usage_info):
        """Sets the memory_usage_info of this SystemMonitoringInfo.

        RAM consumption records.  # noqa: E501

        :param memory_usage_info: The memory_usage_info of this SystemMonitoringInfo.  # noqa: E501
        :type: list[MemoryUsageInfo]
        """

        self._memory_usage_info = memory_usage_info

    @property
    def storage_usage_info(self):
        """Gets the storage_usage_info of this SystemMonitoringInfo.  # noqa: E501

        Storage usage records.  # noqa: E501

        :return: The storage_usage_info of this SystemMonitoringInfo.  # noqa: E501
        :rtype: list[StorageUsageInfo]
        """
        return self._storage_usage_info

    @storage_usage_info.setter
    def storage_usage_info(self, storage_usage_info):
        """Sets the storage_usage_info of this SystemMonitoringInfo.

        Storage usage records.  # noqa: E501

        :param storage_usage_info: The storage_usage_info of this SystemMonitoringInfo.  # noqa: E501
        :type: list[StorageUsageInfo]
        """

        self._storage_usage_info = storage_usage_info

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
        if issubclass(SystemMonitoringInfo, dict):
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
        if not isinstance(other, SystemMonitoringInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
