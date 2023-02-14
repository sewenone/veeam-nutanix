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

class ProtectionDomainSnapshotData(object):
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
        'snapshot_id': 'str',
        'pd_name': 'str',
        'vm_ids': 'list[str]'
    }

    attribute_map = {
        'snapshot_id': 'snapshotId',
        'pd_name': 'pdName',
        'vm_ids': 'vmIds'
    }

    def __init__(self, snapshot_id=None, pd_name=None, vm_ids=None):  # noqa: E501
        """ProtectionDomainSnapshotData - a model defined in Swagger"""  # noqa: E501
        self._snapshot_id = None
        self._pd_name = None
        self._vm_ids = None
        self.discriminator = None
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if pd_name is not None:
            self.pd_name = pd_name
        if vm_ids is not None:
            self.vm_ids = vm_ids

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this ProtectionDomainSnapshotData.  # noqa: E501

        ID assigned to a protection domain snapshot in the Nutanix AHV environment.  # noqa: E501

        :return: The snapshot_id of this ProtectionDomainSnapshotData.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this ProtectionDomainSnapshotData.

        ID assigned to a protection domain snapshot in the Nutanix AHV environment.  # noqa: E501

        :param snapshot_id: The snapshot_id of this ProtectionDomainSnapshotData.  # noqa: E501
        :type: str
        """

        self._snapshot_id = snapshot_id

    @property
    def pd_name(self):
        """Gets the pd_name of this ProtectionDomainSnapshotData.  # noqa: E501

        Name of the protection domain.  # noqa: E501

        :return: The pd_name of this ProtectionDomainSnapshotData.  # noqa: E501
        :rtype: str
        """
        return self._pd_name

    @pd_name.setter
    def pd_name(self, pd_name):
        """Sets the pd_name of this ProtectionDomainSnapshotData.

        Name of the protection domain.  # noqa: E501

        :param pd_name: The pd_name of this ProtectionDomainSnapshotData.  # noqa: E501
        :type: str
        """

        self._pd_name = pd_name

    @property
    def vm_ids(self):
        """Gets the vm_ids of this ProtectionDomainSnapshotData.  # noqa: E501

        IDs of VMs that are protected with the protection domain.  # noqa: E501

        :return: The vm_ids of this ProtectionDomainSnapshotData.  # noqa: E501
        :rtype: list[str]
        """
        return self._vm_ids

    @vm_ids.setter
    def vm_ids(self, vm_ids):
        """Sets the vm_ids of this ProtectionDomainSnapshotData.

        IDs of VMs that are protected with the protection domain.  # noqa: E501

        :param vm_ids: The vm_ids of this ProtectionDomainSnapshotData.  # noqa: E501
        :type: list[str]
        """

        self._vm_ids = vm_ids

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
        if issubclass(ProtectionDomainSnapshotData, dict):
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
        if not isinstance(other, ProtectionDomainSnapshotData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
