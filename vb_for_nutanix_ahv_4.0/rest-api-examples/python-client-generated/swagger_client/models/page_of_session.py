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

class PageOfSession(object):
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
        'offset': 'int',
        'limit': 'int',
        'total_count': 'int',
        'results': 'list[Session]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total_count': 'totalCount',
        'results': 'results'
    }

    def __init__(self, offset=None, limit=None, total_count=None, results=None):  # noqa: E501
        """PageOfSession - a model defined in Swagger"""  # noqa: E501
        self._offset = None
        self._limit = None
        self._total_count = None
        self._results = None
        self.discriminator = None
        self.offset = offset
        self.limit = limit
        if total_count is not None:
            self.total_count = total_count
        if results is not None:
            self.results = results

    @property
    def offset(self):
        """Gets the offset of this PageOfSession.  # noqa: E501

        First N items excluded from the resource collection.  # noqa: E501

        :return: The offset of this PageOfSession.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfSession.

        First N items excluded from the resource collection.  # noqa: E501

        :param offset: The offset of this PageOfSession.  # noqa: E501
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfSession.  # noqa: E501

        Maximum number of items of the resource collection returned in the response.  # noqa: E501

        :return: The limit of this PageOfSession.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfSession.

        Maximum number of items of the resource collection returned in the response.  # noqa: E501

        :param limit: The limit of this PageOfSession.  # noqa: E501
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def total_count(self):
        """Gets the total_count of this PageOfSession.  # noqa: E501

        Total number of items returned in the resource collection.  # noqa: E501

        :return: The total_count of this PageOfSession.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PageOfSession.

        Total number of items returned in the resource collection.  # noqa: E501

        :param total_count: The total_count of this PageOfSession.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def results(self):
        """Gets the results of this PageOfSession.  # noqa: E501

        List of items returned in the resource collection.  # noqa: E501

        :return: The results of this PageOfSession.  # noqa: E501
        :rtype: list[Session]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PageOfSession.

        List of items returned in the resource collection.  # noqa: E501

        :param results: The results of this PageOfSession.  # noqa: E501
        :type: list[Session]
        """

        self._results = results

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
        if issubclass(PageOfSession, dict):
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
        if not isinstance(other, PageOfSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
