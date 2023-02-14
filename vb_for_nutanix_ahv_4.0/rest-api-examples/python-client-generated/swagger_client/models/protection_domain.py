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

class ProtectionDomain(object):
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
        'name': 'str',
        'virtual_machines_size': 'int',
        'virtual_machines_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'virtual_machines_size': 'virtualMachinesSize',
        'virtual_machines_count': 'virtualMachinesCount'
    }

    def __init__(self, name=None, virtual_machines_size=None, virtual_machines_count=None):  # noqa: E501
        """ProtectionDomain - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._virtual_machines_size = None
        self._virtual_machines_count = None
        self.discriminator = None
        self.name = name
        if virtual_machines_size is not None:
            self.virtual_machines_size = virtual_machines_size
        if virtual_machines_count is not None:
            self.virtual_machines_count = virtual_machines_count

    @property
    def name(self):
        """Gets the name of this ProtectionDomain.  # noqa: E501

        Name of the protection domain.  # noqa: E501

        :return: The name of this ProtectionDomain.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProtectionDomain.

        Name of the protection domain.  # noqa: E501

        :param name: The name of this ProtectionDomain.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def virtual_machines_size(self):
        """Gets the virtual_machines_size of this ProtectionDomain.  # noqa: E501

        Size of all VMs added to the protection domain (in bytes).  # noqa: E501

        :return: The virtual_machines_size of this ProtectionDomain.  # noqa: E501
        :rtype: int
        """
        return self._virtual_machines_size

    @virtual_machines_size.setter
    def virtual_machines_size(self, virtual_machines_size):
        """Sets the virtual_machines_size of this ProtectionDomain.

        Size of all VMs added to the protection domain (in bytes).  # noqa: E501

        :param virtual_machines_size: The virtual_machines_size of this ProtectionDomain.  # noqa: E501
        :type: int
        """

        self._virtual_machines_size = virtual_machines_size

    @property
    def virtual_machines_count(self):
        """Gets the virtual_machines_count of this ProtectionDomain.  # noqa: E501

        Number of VMs added to the protection domain.  # noqa: E501

        :return: The virtual_machines_count of this ProtectionDomain.  # noqa: E501
        :rtype: int
        """
        return self._virtual_machines_count

    @virtual_machines_count.setter
    def virtual_machines_count(self, virtual_machines_count):
        """Sets the virtual_machines_count of this ProtectionDomain.

        Number of VMs added to the protection domain.  # noqa: E501

        :param virtual_machines_count: The virtual_machines_count of this ProtectionDomain.  # noqa: E501
        :type: int
        """

        self._virtual_machines_count = virtual_machines_count

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
        if issubclass(ProtectionDomain, dict):
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
        if not isinstance(other, ProtectionDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
