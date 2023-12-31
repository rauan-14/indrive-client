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

class PlaceAccessForResponse(object):
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
        'merchant_place_id': 'str',
        'pickup_time': 'datetime',
        'interval_start': 'datetime',
        'interval_end': 'datetime',
        'status': 'object',
        'delivery_fee': 'float'
    }

    attribute_map = {
        'id': 'id',
        'merchant_place_id': 'merchant_place_id',
        'pickup_time': 'pickup_time',
        'interval_start': 'interval_start',
        'interval_end': 'interval_end',
        'status': 'status',
        'delivery_fee': 'delivery_fee'
    }

    def __init__(self, id=None, merchant_place_id=None, pickup_time=None, interval_start=None, interval_end=None, status=None, delivery_fee=None):  # noqa: E501
        """PlaceAccessForResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._merchant_place_id = None
        self._pickup_time = None
        self._interval_start = None
        self._interval_end = None
        self._status = None
        self._delivery_fee = None
        self.discriminator = None
        self.id = id
        self.merchant_place_id = merchant_place_id
        if pickup_time is not None:
            self.pickup_time = pickup_time
        if interval_start is not None:
            self.interval_start = interval_start
        if interval_end is not None:
            self.interval_end = interval_end
        self.status = status
        if delivery_fee is not None:
            self.delivery_fee = delivery_fee

    @property
    def id(self):
        """Gets the id of this PlaceAccessForResponse.  # noqa: E501


        :return: The id of this PlaceAccessForResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlaceAccessForResponse.


        :param id: The id of this PlaceAccessForResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def merchant_place_id(self):
        """Gets the merchant_place_id of this PlaceAccessForResponse.  # noqa: E501


        :return: The merchant_place_id of this PlaceAccessForResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_place_id

    @merchant_place_id.setter
    def merchant_place_id(self, merchant_place_id):
        """Sets the merchant_place_id of this PlaceAccessForResponse.


        :param merchant_place_id: The merchant_place_id of this PlaceAccessForResponse.  # noqa: E501
        :type: str
        """
        if merchant_place_id is None:
            raise ValueError("Invalid value for `merchant_place_id`, must not be `None`")  # noqa: E501

        self._merchant_place_id = merchant_place_id

    @property
    def pickup_time(self):
        """Gets the pickup_time of this PlaceAccessForResponse.  # noqa: E501


        :return: The pickup_time of this PlaceAccessForResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pickup_time

    @pickup_time.setter
    def pickup_time(self, pickup_time):
        """Sets the pickup_time of this PlaceAccessForResponse.


        :param pickup_time: The pickup_time of this PlaceAccessForResponse.  # noqa: E501
        :type: datetime
        """

        self._pickup_time = pickup_time

    @property
    def interval_start(self):
        """Gets the interval_start of this PlaceAccessForResponse.  # noqa: E501


        :return: The interval_start of this PlaceAccessForResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._interval_start

    @interval_start.setter
    def interval_start(self, interval_start):
        """Sets the interval_start of this PlaceAccessForResponse.


        :param interval_start: The interval_start of this PlaceAccessForResponse.  # noqa: E501
        :type: datetime
        """

        self._interval_start = interval_start

    @property
    def interval_end(self):
        """Gets the interval_end of this PlaceAccessForResponse.  # noqa: E501


        :return: The interval_end of this PlaceAccessForResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._interval_end

    @interval_end.setter
    def interval_end(self, interval_end):
        """Sets the interval_end of this PlaceAccessForResponse.


        :param interval_end: The interval_end of this PlaceAccessForResponse.  # noqa: E501
        :type: datetime
        """

        self._interval_end = interval_end

    @property
    def status(self):
        """Gets the status of this PlaceAccessForResponse.  # noqa: E501


        :return: The status of this PlaceAccessForResponse.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PlaceAccessForResponse.


        :param status: The status of this PlaceAccessForResponse.  # noqa: E501
        :type: object
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def delivery_fee(self):
        """Gets the delivery_fee of this PlaceAccessForResponse.  # noqa: E501


        :return: The delivery_fee of this PlaceAccessForResponse.  # noqa: E501
        :rtype: float
        """
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, delivery_fee):
        """Sets the delivery_fee of this PlaceAccessForResponse.


        :param delivery_fee: The delivery_fee of this PlaceAccessForResponse.  # noqa: E501
        :type: float
        """

        self._delivery_fee = delivery_fee

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
        if issubclass(PlaceAccessForResponse, dict):
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
        if not isinstance(other, PlaceAccessForResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
