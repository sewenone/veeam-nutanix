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

class VolumeGroup(object):
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
        'protection_domain': 'str',
        'consistency_group': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'protection_domain': 'protectionDomain',
        'consistency_group': 'consistencyGroup'
    }

    def __init__(self, id=None, name=None, protection_domain=None, consistency_group=None):  # noqa: E501
        """VolumeGroup - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._protection_domain = None
        self._consistency_group = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if protection_domain is not None:
            self.protection_domain = protection_domain
        if consistency_group is not None:
            self.consistency_group = consistency_group

    @property
    def id(self):
        """Gets the id of this VolumeGroup.  # noqa: E501

        ID assigned to a cluster in the Nutanix AHV environment.  # noqa: E501

        :return: The id of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumeGroup.

        ID assigned to a cluster in the Nutanix AHV environment.  # noqa: E501

        :param id: The id of this VolumeGroup.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this VolumeGroup.  # noqa: E501

        Name of the volume group.  # noqa: E501

        :return: The name of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VolumeGroup.

        Name of the volume group.  # noqa: E501

        :param name: The name of this VolumeGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def protection_domain(self):
        """Gets the protection_domain of this VolumeGroup.  # noqa: E501

        Protection domain that includes the volume group.  # noqa: E501

        :return: The protection_domain of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._protection_domain

    @protection_domain.setter
    def protection_domain(self, protection_domain):
        """Sets the protection_domain of this VolumeGroup.

        Protection domain that includes the volume group.  # noqa: E501

        :param protection_domain: The protection_domain of this VolumeGroup.  # noqa: E501
        :type: str
        """

        self._protection_domain = protection_domain

    @property
    def consistency_group(self):
        """Gets the consistency_group of this VolumeGroup.  # noqa: E501

        Consistency group that contains the volume group.  # noqa: E501

        :return: The consistency_group of this VolumeGroup.  # noqa: E501
        :rtype: str
        """
        return self._consistency_group

    @consistency_group.setter
    def consistency_group(self, consistency_group):
        """Sets the consistency_group of this VolumeGroup.

        Consistency group that contains the volume group.  # noqa: E501

        :param consistency_group: The consistency_group of this VolumeGroup.  # noqa: E501
        :type: str
        """

        self._consistency_group = consistency_group

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
        if issubclass(VolumeGroup, dict):
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
        if not isinstance(other, VolumeGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
