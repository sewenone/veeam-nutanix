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

class Cluster(object):
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
        'address': 'str',
        'port': 'int',
        'state': 'ServerState',
        'version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'address': 'address',
        'port': 'port',
        'state': 'state',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, description=None, address=None, port=None, state=None, version=None):  # noqa: E501
        """Cluster - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._address = None
        self._port = None
        self._state = None
        self._version = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if address is not None:
            self.address = address
        if port is not None:
            self.port = port
        if state is not None:
            self.state = state
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this Cluster.  # noqa: E501

        ID assigned to a cluster in the Nutanix AHV environment.  # noqa: E501

        :return: The id of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Cluster.

        ID assigned to a cluster in the Nutanix AHV environment.  # noqa: E501

        :param id: The id of this Cluster.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Cluster.  # noqa: E501

        Name of the cluster.  # noqa: E501

        :return: The name of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Cluster.

        Name of the cluster.  # noqa: E501

        :param name: The name of this Cluster.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Cluster.  # noqa: E501

        Description of the cluster.  # noqa: E501

        :return: The description of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Cluster.

        Description of the cluster.  # noqa: E501

        :param description: The description of this Cluster.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def address(self):
        """Gets the address of this Cluster.  # noqa: E501

        IP address or hostname of the cluster.  # noqa: E501

        :return: The address of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Cluster.

        IP address or hostname of the cluster.  # noqa: E501

        :param address: The address of this Cluster.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def port(self):
        """Gets the port of this Cluster.  # noqa: E501

        Port used to access the cluster.  # noqa: E501

        :return: The port of this Cluster.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Cluster.

        Port used to access the cluster.  # noqa: E501

        :param port: The port of this Cluster.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def state(self):
        """Gets the state of this Cluster.  # noqa: E501


        :return: The state of this Cluster.  # noqa: E501
        :rtype: ServerState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Cluster.


        :param state: The state of this Cluster.  # noqa: E501
        :type: ServerState
        """

        self._state = state

    @property
    def version(self):
        """Gets the version of this Cluster.  # noqa: E501

        Version of the cluster AOS.  # noqa: E501

        :return: The version of this Cluster.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Cluster.

        Version of the cluster AOS.  # noqa: E501

        :param version: The version of this Cluster.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(Cluster, dict):
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
        if not isinstance(other, Cluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
