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

class NutanixNetwork(object):
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
        'network_address': 'str',
        'ip_management_on': 'bool',
        'prefix_length': 'int',
        'ip_pool': 'list[str]',
        'gateway_ip': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'network_address': 'networkAddress',
        'ip_management_on': 'ipManagementOn',
        'prefix_length': 'prefixLength',
        'ip_pool': 'ipPool',
        'gateway_ip': 'gatewayIp'
    }

    def __init__(self, id=None, name=None, network_address=None, ip_management_on=None, prefix_length=None, ip_pool=None, gateway_ip=None):  # noqa: E501
        """NutanixNetwork - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._network_address = None
        self._ip_management_on = None
        self._prefix_length = None
        self._ip_pool = None
        self._gateway_ip = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if network_address is not None:
            self.network_address = network_address
        if ip_management_on is not None:
            self.ip_management_on = ip_management_on
        if prefix_length is not None:
            self.prefix_length = prefix_length
        if ip_pool is not None:
            self.ip_pool = ip_pool
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip

    @property
    def id(self):
        """Gets the id of this NutanixNetwork.  # noqa: E501

        ID assigned to the network in the Nutanix AHV environment.  # noqa: E501

        :return: The id of this NutanixNetwork.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NutanixNetwork.

        ID assigned to the network in the Nutanix AHV environment.  # noqa: E501

        :param id: The id of this NutanixNetwork.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NutanixNetwork.  # noqa: E501

        Name of the network in the Nutanix AHV environment.  # noqa: E501

        :return: The name of this NutanixNetwork.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NutanixNetwork.

        Name of the network in the Nutanix AHV environment.  # noqa: E501

        :param name: The name of this NutanixNetwork.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def network_address(self):
        """Gets the network_address of this NutanixNetwork.  # noqa: E501

        Network IP prefix.  # noqa: E501

        :return: The network_address of this NutanixNetwork.  # noqa: E501
        :rtype: str
        """
        return self._network_address

    @network_address.setter
    def network_address(self, network_address):
        """Sets the network_address of this NutanixNetwork.

        Network IP prefix.  # noqa: E501

        :param network_address: The network_address of this NutanixNetwork.  # noqa: E501
        :type: str
        """

        self._network_address = network_address

    @property
    def ip_management_on(self):
        """Gets the ip_management_on of this NutanixNetwork.  # noqa: E501

        Defines whether the IP Address Management feature is enabled on the network. For more information, see [Nutanix documentation](https://portal.nutanix.com/page/documents/details?targetId=AHV-Admin-Guide-v6_5:ahv-acr-host-ipam-r.html).  # noqa: E501

        :return: The ip_management_on of this NutanixNetwork.  # noqa: E501
        :rtype: bool
        """
        return self._ip_management_on

    @ip_management_on.setter
    def ip_management_on(self, ip_management_on):
        """Sets the ip_management_on of this NutanixNetwork.

        Defines whether the IP Address Management feature is enabled on the network. For more information, see [Nutanix documentation](https://portal.nutanix.com/page/documents/details?targetId=AHV-Admin-Guide-v6_5:ahv-acr-host-ipam-r.html).  # noqa: E501

        :param ip_management_on: The ip_management_on of this NutanixNetwork.  # noqa: E501
        :type: bool
        """

        self._ip_management_on = ip_management_on

    @property
    def prefix_length(self):
        """Gets the prefix_length of this NutanixNetwork.  # noqa: E501

        Length of the routing prefix to identify the subnet mask to be used by devices requesting an IP address from the DHCP service.  # noqa: E501

        :return: The prefix_length of this NutanixNetwork.  # noqa: E501
        :rtype: int
        """
        return self._prefix_length

    @prefix_length.setter
    def prefix_length(self, prefix_length):
        """Sets the prefix_length of this NutanixNetwork.

        Length of the routing prefix to identify the subnet mask to be used by devices requesting an IP address from the DHCP service.  # noqa: E501

        :param prefix_length: The prefix_length of this NutanixNetwork.  # noqa: E501
        :type: int
        """

        self._prefix_length = prefix_length

    @property
    def ip_pool(self):
        """Gets the ip_pool of this NutanixNetwork.  # noqa: E501

        Ranges of the IP addresses that can be assigned to devices requesting an IP address from the DHCP service.  # noqa: E501

        :return: The ip_pool of this NutanixNetwork.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_pool

    @ip_pool.setter
    def ip_pool(self, ip_pool):
        """Sets the ip_pool of this NutanixNetwork.

        Ranges of the IP addresses that can be assigned to devices requesting an IP address from the DHCP service.  # noqa: E501

        :param ip_pool: The ip_pool of this NutanixNetwork.  # noqa: E501
        :type: list[str]
        """

        self._ip_pool = ip_pool

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this NutanixNetwork.  # noqa: E501

        IP address of the default gateway to be used by devices requesting an IP address from the DHCP service.  # noqa: E501

        :return: The gateway_ip of this NutanixNetwork.  # noqa: E501
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this NutanixNetwork.

        IP address of the default gateway to be used by devices requesting an IP address from the DHCP service.  # noqa: E501

        :param gateway_ip: The gateway_ip of this NutanixNetwork.  # noqa: E501
        :type: str
        """

        self._gateway_ip = gateway_ip

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
        if issubclass(NutanixNetwork, dict):
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
        if not isinstance(other, NutanixNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
