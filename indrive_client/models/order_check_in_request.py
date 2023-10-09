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

class OrderCheckInRequest(object):
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
        'longitude': 'float',
        'latitude': 'float',
        'region': 'str',
        'city_id': 'int',
        'street': 'str',
        'house_number': 'str',
        'flat_number': 'str',
        'entrance': 'str',
        'intercom': 'str',
        'floor': 'str',
        'pickup_time': 'datetime',
        'channel': 'str'
    }

    attribute_map = {
        'longitude': 'longitude',
        'latitude': 'latitude',
        'region': 'region',
        'city_id': 'city_id',
        'street': 'street',
        'house_number': 'house_number',
        'flat_number': 'flat_number',
        'entrance': 'entrance',
        'intercom': 'intercom',
        'floor': 'floor',
        'pickup_time': 'pickup_time',
        'channel': 'channel'
    }

    def __init__(self, longitude=None, latitude=None, region=None, city_id=None, street=None, house_number=None, flat_number=None, entrance=None, intercom=None, floor=None, pickup_time=None, channel=None):  # noqa: E501
        """OrderCheckInRequest - a model defined in Swagger"""  # noqa: E501
        self._longitude = None
        self._latitude = None
        self._region = None
        self._city_id = None
        self._street = None
        self._house_number = None
        self._flat_number = None
        self._entrance = None
        self._intercom = None
        self._floor = None
        self._pickup_time = None
        self._channel = None
        self.discriminator = None
        self.longitude = longitude
        self.latitude = latitude
        if region is not None:
            self.region = region
        if city_id is not None:
            self.city_id = city_id
        if street is not None:
            self.street = street
        if house_number is not None:
            self.house_number = house_number
        if flat_number is not None:
            self.flat_number = flat_number
        if entrance is not None:
            self.entrance = entrance
        if intercom is not None:
            self.intercom = intercom
        if floor is not None:
            self.floor = floor
        if pickup_time is not None:
            self.pickup_time = pickup_time
        if channel is not None:
            self.channel = channel

    @property
    def longitude(self):
        """Gets the longitude of this OrderCheckInRequest.  # noqa: E501


        :return: The longitude of this OrderCheckInRequest.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this OrderCheckInRequest.


        :param longitude: The longitude of this OrderCheckInRequest.  # noqa: E501
        :type: float
        """
        if longitude is None:
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

    @property
    def latitude(self):
        """Gets the latitude of this OrderCheckInRequest.  # noqa: E501


        :return: The latitude of this OrderCheckInRequest.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this OrderCheckInRequest.


        :param latitude: The latitude of this OrderCheckInRequest.  # noqa: E501
        :type: float
        """
        if latitude is None:
            raise ValueError("Invalid value for `latitude`, must not be `None`")  # noqa: E501

        self._latitude = latitude

    @property
    def region(self):
        """Gets the region of this OrderCheckInRequest.  # noqa: E501


        :return: The region of this OrderCheckInRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this OrderCheckInRequest.


        :param region: The region of this OrderCheckInRequest.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def city_id(self):
        """Gets the city_id of this OrderCheckInRequest.  # noqa: E501


        :return: The city_id of this OrderCheckInRequest.  # noqa: E501
        :rtype: int
        """
        return self._city_id

    @city_id.setter
    def city_id(self, city_id):
        """Sets the city_id of this OrderCheckInRequest.


        :param city_id: The city_id of this OrderCheckInRequest.  # noqa: E501
        :type: int
        """

        self._city_id = city_id

    @property
    def street(self):
        """Gets the street of this OrderCheckInRequest.  # noqa: E501


        :return: The street of this OrderCheckInRequest.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this OrderCheckInRequest.


        :param street: The street of this OrderCheckInRequest.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def house_number(self):
        """Gets the house_number of this OrderCheckInRequest.  # noqa: E501


        :return: The house_number of this OrderCheckInRequest.  # noqa: E501
        :rtype: str
        """
        return self._house_number

    @house_number.setter
    def house_number(self, house_number):
        """Sets the house_number of this OrderCheckInRequest.


        :param house_number: The house_number of this OrderCheckInRequest.  # noqa: E501
        :type: str
        """

        self._house_number = house_number

    @property
    def flat_number(self):
        """Gets the flat_number of this OrderCheckInRequest.  # noqa: E501


        :return: The flat_number of this OrderCheckInRequest.  # noqa: E501
        :rtype: str
        """
        return self._flat_number

    @flat_number.setter
    def flat_number(self, flat_number):
        """Sets the flat_number of this OrderCheckInRequest.


        :param flat_number: The flat_number of this OrderCheckInRequest.  # noqa: E501
        :type: str
        """

        self._flat_number = flat_number

    @property
    def entrance(self):
        """Gets the entrance of this OrderCheckInRequest.  # noqa: E501


        :return: The entrance of this OrderCheckInRequest.  # noqa: E501
        :rtype: str
        """
        return self._entrance

    @entrance.setter
    def entrance(self, entrance):
        """Sets the entrance of this OrderCheckInRequest.


        :param entrance: The entrance of this OrderCheckInRequest.  # noqa: E501
        :type: str
        """

        self._entrance = entrance

    @property
    def intercom(self):
        """Gets the intercom of this OrderCheckInRequest.  # noqa: E501


        :return: The intercom of this OrderCheckInRequest.  # noqa: E501
        :rtype: str
        """
        return self._intercom

    @intercom.setter
    def intercom(self, intercom):
        """Sets the intercom of this OrderCheckInRequest.


        :param intercom: The intercom of this OrderCheckInRequest.  # noqa: E501
        :type: str
        """

        self._intercom = intercom

    @property
    def floor(self):
        """Gets the floor of this OrderCheckInRequest.  # noqa: E501


        :return: The floor of this OrderCheckInRequest.  # noqa: E501
        :rtype: str
        """
        return self._floor

    @floor.setter
    def floor(self, floor):
        """Sets the floor of this OrderCheckInRequest.


        :param floor: The floor of this OrderCheckInRequest.  # noqa: E501
        :type: str
        """

        self._floor = floor

    @property
    def pickup_time(self):
        """Gets the pickup_time of this OrderCheckInRequest.  # noqa: E501


        :return: The pickup_time of this OrderCheckInRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._pickup_time

    @pickup_time.setter
    def pickup_time(self, pickup_time):
        """Sets the pickup_time of this OrderCheckInRequest.


        :param pickup_time: The pickup_time of this OrderCheckInRequest.  # noqa: E501
        :type: datetime
        """

        self._pickup_time = pickup_time

    @property
    def channel(self):
        """Gets the channel of this OrderCheckInRequest.  # noqa: E501


        :return: The channel of this OrderCheckInRequest.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this OrderCheckInRequest.


        :param channel: The channel of this OrderCheckInRequest.  # noqa: E501
        :type: str
        """

        self._channel = channel

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
        if issubclass(OrderCheckInRequest, dict):
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
        if not isinstance(other, OrderCheckInRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other