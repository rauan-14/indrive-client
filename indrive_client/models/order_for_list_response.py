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

class OrderForListResponse(object):
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
        'order_id': 'str',
        'merchant': 'OrderMerchant',
        'place': 'OrderPlace',
        'area_id': 'str',
        'status': 'OrderStatusEnum',
        'payment_status': 'PaymentStatusEnum',
        'suggested_time': 'datetime',
        'city_id': 'int',
        'courier': 'OrderCourier',
        'is_normative_exceeded': 'bool',
        'group_id': 'str',
        'group_orders': 'list[OrderForListResponse]'
    }

    attribute_map = {
        'id': 'id',
        'order_id': 'order_id',
        'merchant': 'merchant',
        'place': 'place',
        'area_id': 'area_id',
        'status': 'status',
        'payment_status': 'payment_status',
        'suggested_time': 'suggested_time',
        'city_id': 'city_id',
        'courier': 'courier',
        'is_normative_exceeded': 'is_normative_exceeded',
        'group_id': 'group_id',
        'group_orders': 'group_orders'
    }

    def __init__(self, id=None, order_id=None, merchant=None, place=None, area_id=None, status=None, payment_status=None, suggested_time=None, city_id=None, courier=None, is_normative_exceeded=None, group_id=None, group_orders=None):  # noqa: E501
        """OrderForListResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._order_id = None
        self._merchant = None
        self._place = None
        self._area_id = None
        self._status = None
        self._payment_status = None
        self._suggested_time = None
        self._city_id = None
        self._courier = None
        self._is_normative_exceeded = None
        self._group_id = None
        self._group_orders = None
        self.discriminator = None
        self.id = id
        self.order_id = order_id
        if merchant is not None:
            self.merchant = merchant
        if place is not None:
            self.place = place
        self.area_id = area_id
        self.status = status
        self.payment_status = payment_status
        if suggested_time is not None:
            self.suggested_time = suggested_time
        if city_id is not None:
            self.city_id = city_id
        if courier is not None:
            self.courier = courier
        self.is_normative_exceeded = is_normative_exceeded
        if group_id is not None:
            self.group_id = group_id
        if group_orders is not None:
            self.group_orders = group_orders

    @property
    def id(self):
        """Gets the id of this OrderForListResponse.  # noqa: E501


        :return: The id of this OrderForListResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderForListResponse.


        :param id: The id of this OrderForListResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def order_id(self):
        """Gets the order_id of this OrderForListResponse.  # noqa: E501


        :return: The order_id of this OrderForListResponse.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this OrderForListResponse.


        :param order_id: The order_id of this OrderForListResponse.  # noqa: E501
        :type: str
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def merchant(self):
        """Gets the merchant of this OrderForListResponse.  # noqa: E501


        :return: The merchant of this OrderForListResponse.  # noqa: E501
        :rtype: OrderMerchant
        """
        return self._merchant

    @merchant.setter
    def merchant(self, merchant):
        """Sets the merchant of this OrderForListResponse.


        :param merchant: The merchant of this OrderForListResponse.  # noqa: E501
        :type: OrderMerchant
        """

        self._merchant = merchant

    @property
    def place(self):
        """Gets the place of this OrderForListResponse.  # noqa: E501


        :return: The place of this OrderForListResponse.  # noqa: E501
        :rtype: OrderPlace
        """
        return self._place

    @place.setter
    def place(self, place):
        """Sets the place of this OrderForListResponse.


        :param place: The place of this OrderForListResponse.  # noqa: E501
        :type: OrderPlace
        """

        self._place = place

    @property
    def area_id(self):
        """Gets the area_id of this OrderForListResponse.  # noqa: E501


        :return: The area_id of this OrderForListResponse.  # noqa: E501
        :rtype: str
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this OrderForListResponse.


        :param area_id: The area_id of this OrderForListResponse.  # noqa: E501
        :type: str
        """
        if area_id is None:
            raise ValueError("Invalid value for `area_id`, must not be `None`")  # noqa: E501

        self._area_id = area_id

    @property
    def status(self):
        """Gets the status of this OrderForListResponse.  # noqa: E501


        :return: The status of this OrderForListResponse.  # noqa: E501
        :rtype: OrderStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderForListResponse.


        :param status: The status of this OrderForListResponse.  # noqa: E501
        :type: OrderStatusEnum
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def payment_status(self):
        """Gets the payment_status of this OrderForListResponse.  # noqa: E501


        :return: The payment_status of this OrderForListResponse.  # noqa: E501
        :rtype: PaymentStatusEnum
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """Sets the payment_status of this OrderForListResponse.


        :param payment_status: The payment_status of this OrderForListResponse.  # noqa: E501
        :type: PaymentStatusEnum
        """
        if payment_status is None:
            raise ValueError("Invalid value for `payment_status`, must not be `None`")  # noqa: E501

        self._payment_status = payment_status

    @property
    def suggested_time(self):
        """Gets the suggested_time of this OrderForListResponse.  # noqa: E501


        :return: The suggested_time of this OrderForListResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._suggested_time

    @suggested_time.setter
    def suggested_time(self, suggested_time):
        """Sets the suggested_time of this OrderForListResponse.


        :param suggested_time: The suggested_time of this OrderForListResponse.  # noqa: E501
        :type: datetime
        """

        self._suggested_time = suggested_time

    @property
    def city_id(self):
        """Gets the city_id of this OrderForListResponse.  # noqa: E501


        :return: The city_id of this OrderForListResponse.  # noqa: E501
        :rtype: int
        """
        return self._city_id

    @city_id.setter
    def city_id(self, city_id):
        """Sets the city_id of this OrderForListResponse.


        :param city_id: The city_id of this OrderForListResponse.  # noqa: E501
        :type: int
        """

        self._city_id = city_id

    @property
    def courier(self):
        """Gets the courier of this OrderForListResponse.  # noqa: E501


        :return: The courier of this OrderForListResponse.  # noqa: E501
        :rtype: OrderCourier
        """
        return self._courier

    @courier.setter
    def courier(self, courier):
        """Sets the courier of this OrderForListResponse.


        :param courier: The courier of this OrderForListResponse.  # noqa: E501
        :type: OrderCourier
        """

        self._courier = courier

    @property
    def is_normative_exceeded(self):
        """Gets the is_normative_exceeded of this OrderForListResponse.  # noqa: E501


        :return: The is_normative_exceeded of this OrderForListResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_normative_exceeded

    @is_normative_exceeded.setter
    def is_normative_exceeded(self, is_normative_exceeded):
        """Sets the is_normative_exceeded of this OrderForListResponse.


        :param is_normative_exceeded: The is_normative_exceeded of this OrderForListResponse.  # noqa: E501
        :type: bool
        """
        if is_normative_exceeded is None:
            raise ValueError("Invalid value for `is_normative_exceeded`, must not be `None`")  # noqa: E501

        self._is_normative_exceeded = is_normative_exceeded

    @property
    def group_id(self):
        """Gets the group_id of this OrderForListResponse.  # noqa: E501


        :return: The group_id of this OrderForListResponse.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this OrderForListResponse.


        :param group_id: The group_id of this OrderForListResponse.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def group_orders(self):
        """Gets the group_orders of this OrderForListResponse.  # noqa: E501


        :return: The group_orders of this OrderForListResponse.  # noqa: E501
        :rtype: list[OrderForListResponse]
        """
        return self._group_orders

    @group_orders.setter
    def group_orders(self, group_orders):
        """Sets the group_orders of this OrderForListResponse.


        :param group_orders: The group_orders of this OrderForListResponse.  # noqa: E501
        :type: list[OrderForListResponse]
        """

        self._group_orders = group_orders

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
        if issubclass(OrderForListResponse, dict):
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
        if not isinstance(other, OrderForListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
