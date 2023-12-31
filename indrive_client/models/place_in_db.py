# coding: utf-8

"""
    Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PlaceInDB(object):
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
        'location': 'DbModelsBasePoint',
        'merchant_id': 'str',
        'merchant_place_id': 'str',
        'address': 'str',
        'name': 'str',
        'city_id': 'int',
        'email': 'str',
        'id': 'str',
        'work_times': 'WorkTimes',
        'is_blocked': 'bool'
    }

    attribute_map = {
        'location': 'location',
        'merchant_id': 'merchant_id',
        'merchant_place_id': 'merchant_place_id',
        'address': 'address',
        'name': 'name',
        'city_id': 'city_id',
        'email': 'email',
        'id': 'id',
        'work_times': 'work_times',
        'is_blocked': 'is_blocked'
    }

    def __init__(self, location=None, merchant_id=None, merchant_place_id=None, address=None, name=None, city_id=None, email=None, id=None, work_times=None, is_blocked=False):  # noqa: E501
        """PlaceInDB - a model defined in Swagger"""  # noqa: E501
        self._location = None
        self._merchant_id = None
        self._merchant_place_id = None
        self._address = None
        self._name = None
        self._city_id = None
        self._email = None
        self._id = None
        self._work_times = None
        self._is_blocked = None
        self.discriminator = None
        self.location = location
        self.merchant_id = merchant_id
        if merchant_place_id is not None:
            self.merchant_place_id = merchant_place_id
        self.address = address
        self.name = name
        self.city_id = city_id
        if email is not None:
            self.email = email
        self.id = id
        if work_times is not None:
            self.work_times = work_times
        if is_blocked is not None:
            self.is_blocked = is_blocked

    @property
    def location(self):
        """Gets the location of this PlaceInDB.  # noqa: E501


        :return: The location of this PlaceInDB.  # noqa: E501
        :rtype: DbModelsBasePoint
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PlaceInDB.


        :param location: The location of this PlaceInDB.  # noqa: E501
        :type: DbModelsBasePoint
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def merchant_id(self):
        """Gets the merchant_id of this PlaceInDB.  # noqa: E501


        :return: The merchant_id of this PlaceInDB.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this PlaceInDB.


        :param merchant_id: The merchant_id of this PlaceInDB.  # noqa: E501
        :type: str
        """
        if merchant_id is None:
            raise ValueError("Invalid value for `merchant_id`, must not be `None`")  # noqa: E501

        self._merchant_id = merchant_id

    @property
    def merchant_place_id(self):
        """Gets the merchant_place_id of this PlaceInDB.  # noqa: E501


        :return: The merchant_place_id of this PlaceInDB.  # noqa: E501
        :rtype: str
        """
        return self._merchant_place_id

    @merchant_place_id.setter
    def merchant_place_id(self, merchant_place_id):
        """Sets the merchant_place_id of this PlaceInDB.


        :param merchant_place_id: The merchant_place_id of this PlaceInDB.  # noqa: E501
        :type: str
        """

        self._merchant_place_id = merchant_place_id

    @property
    def address(self):
        """Gets the address of this PlaceInDB.  # noqa: E501


        :return: The address of this PlaceInDB.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PlaceInDB.


        :param address: The address of this PlaceInDB.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def name(self):
        """Gets the name of this PlaceInDB.  # noqa: E501


        :return: The name of this PlaceInDB.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlaceInDB.


        :param name: The name of this PlaceInDB.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def city_id(self):
        """Gets the city_id of this PlaceInDB.  # noqa: E501


        :return: The city_id of this PlaceInDB.  # noqa: E501
        :rtype: int
        """
        return self._city_id

    @city_id.setter
    def city_id(self, city_id):
        """Sets the city_id of this PlaceInDB.


        :param city_id: The city_id of this PlaceInDB.  # noqa: E501
        :type: int
        """
        if city_id is None:
            raise ValueError("Invalid value for `city_id`, must not be `None`")  # noqa: E501

        self._city_id = city_id

    @property
    def email(self):
        """Gets the email of this PlaceInDB.  # noqa: E501


        :return: The email of this PlaceInDB.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PlaceInDB.


        :param email: The email of this PlaceInDB.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this PlaceInDB.  # noqa: E501


        :return: The id of this PlaceInDB.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlaceInDB.


        :param id: The id of this PlaceInDB.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def work_times(self):
        """Gets the work_times of this PlaceInDB.  # noqa: E501


        :return: The work_times of this PlaceInDB.  # noqa: E501
        :rtype: WorkTimes
        """
        return self._work_times

    @work_times.setter
    def work_times(self, work_times):
        """Sets the work_times of this PlaceInDB.


        :param work_times: The work_times of this PlaceInDB.  # noqa: E501
        :type: WorkTimes
        """

        self._work_times = work_times

    @property
    def is_blocked(self):
        """Gets the is_blocked of this PlaceInDB.  # noqa: E501


        :return: The is_blocked of this PlaceInDB.  # noqa: E501
        :rtype: bool
        """
        return self._is_blocked

    @is_blocked.setter
    def is_blocked(self, is_blocked):
        """Sets the is_blocked of this PlaceInDB.


        :param is_blocked: The is_blocked of this PlaceInDB.  # noqa: E501
        :type: bool
        """

        self._is_blocked = is_blocked

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
        if issubclass(PlaceInDB, dict):
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
        if not isinstance(other, PlaceInDB):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
