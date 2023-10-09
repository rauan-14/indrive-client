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

class OrderDryRun(object):
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
        'place_id': 'str',
        'cost': 'OrderCost',
        'person_count': 'int',
        'comment': 'str',
        'products': 'list[CreateProductInRequest]',
        'additional_services': 'list[AdditionalServiceCodeNameOnly]',
        'is_force_start': 'bool',
        'delivery': 'DeliveryDryRunInRequest'
    }

    attribute_map = {
        'place_id': 'place_id',
        'cost': 'cost',
        'person_count': 'person_count',
        'comment': 'comment',
        'products': 'products',
        'additional_services': 'additional_services',
        'is_force_start': 'is_force_start',
        'delivery': 'delivery'
    }

    def __init__(self, place_id=None, cost=None, person_count=None, comment=None, products=None, additional_services=None, is_force_start=False, delivery=None):  # noqa: E501
        """OrderDryRun - a model defined in Swagger"""  # noqa: E501
        self._place_id = None
        self._cost = None
        self._person_count = None
        self._comment = None
        self._products = None
        self._additional_services = None
        self._is_force_start = None
        self._delivery = None
        self.discriminator = None
        self.place_id = place_id
        self.cost = cost
        self.person_count = person_count
        if comment is not None:
            self.comment = comment
        self.products = products
        if additional_services is not None:
            self.additional_services = additional_services
        if is_force_start is not None:
            self.is_force_start = is_force_start
        self.delivery = delivery

    @property
    def place_id(self):
        """Gets the place_id of this OrderDryRun.  # noqa: E501


        :return: The place_id of this OrderDryRun.  # noqa: E501
        :rtype: str
        """
        return self._place_id

    @place_id.setter
    def place_id(self, place_id):
        """Sets the place_id of this OrderDryRun.


        :param place_id: The place_id of this OrderDryRun.  # noqa: E501
        :type: str
        """
        if place_id is None:
            raise ValueError("Invalid value for `place_id`, must not be `None`")  # noqa: E501

        self._place_id = place_id

    @property
    def cost(self):
        """Gets the cost of this OrderDryRun.  # noqa: E501


        :return: The cost of this OrderDryRun.  # noqa: E501
        :rtype: OrderCost
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this OrderDryRun.


        :param cost: The cost of this OrderDryRun.  # noqa: E501
        :type: OrderCost
        """
        if cost is None:
            raise ValueError("Invalid value for `cost`, must not be `None`")  # noqa: E501

        self._cost = cost

    @property
    def person_count(self):
        """Gets the person_count of this OrderDryRun.  # noqa: E501


        :return: The person_count of this OrderDryRun.  # noqa: E501
        :rtype: int
        """
        return self._person_count

    @person_count.setter
    def person_count(self, person_count):
        """Sets the person_count of this OrderDryRun.


        :param person_count: The person_count of this OrderDryRun.  # noqa: E501
        :type: int
        """
        if person_count is None:
            raise ValueError("Invalid value for `person_count`, must not be `None`")  # noqa: E501

        self._person_count = person_count

    @property
    def comment(self):
        """Gets the comment of this OrderDryRun.  # noqa: E501


        :return: The comment of this OrderDryRun.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this OrderDryRun.


        :param comment: The comment of this OrderDryRun.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def products(self):
        """Gets the products of this OrderDryRun.  # noqa: E501


        :return: The products of this OrderDryRun.  # noqa: E501
        :rtype: list[CreateProductInRequest]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this OrderDryRun.


        :param products: The products of this OrderDryRun.  # noqa: E501
        :type: list[CreateProductInRequest]
        """
        if products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

    @property
    def additional_services(self):
        """Gets the additional_services of this OrderDryRun.  # noqa: E501


        :return: The additional_services of this OrderDryRun.  # noqa: E501
        :rtype: list[AdditionalServiceCodeNameOnly]
        """
        return self._additional_services

    @additional_services.setter
    def additional_services(self, additional_services):
        """Sets the additional_services of this OrderDryRun.


        :param additional_services: The additional_services of this OrderDryRun.  # noqa: E501
        :type: list[AdditionalServiceCodeNameOnly]
        """

        self._additional_services = additional_services

    @property
    def is_force_start(self):
        """Gets the is_force_start of this OrderDryRun.  # noqa: E501


        :return: The is_force_start of this OrderDryRun.  # noqa: E501
        :rtype: bool
        """
        return self._is_force_start

    @is_force_start.setter
    def is_force_start(self, is_force_start):
        """Sets the is_force_start of this OrderDryRun.


        :param is_force_start: The is_force_start of this OrderDryRun.  # noqa: E501
        :type: bool
        """

        self._is_force_start = is_force_start

    @property
    def delivery(self):
        """Gets the delivery of this OrderDryRun.  # noqa: E501


        :return: The delivery of this OrderDryRun.  # noqa: E501
        :rtype: DeliveryDryRunInRequest
        """
        return self._delivery

    @delivery.setter
    def delivery(self, delivery):
        """Sets the delivery of this OrderDryRun.


        :param delivery: The delivery of this OrderDryRun.  # noqa: E501
        :type: DeliveryDryRunInRequest
        """
        if delivery is None:
            raise ValueError("Invalid value for `delivery`, must not be `None`")  # noqa: E501

        self._delivery = delivery

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
        if issubclass(OrderDryRun, dict):
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
        if not isinstance(other, OrderDryRun):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
