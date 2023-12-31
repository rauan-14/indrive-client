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

class IngredientForResponse(object):
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
        'price': 'float',
        'group_name': 'str',
        'vat_code': 'str',
        'rkeeper_code': 'str',
        'external_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'price': 'price',
        'group_name': 'group_name',
        'vat_code': 'vat_code',
        'rkeeper_code': 'rkeeper_code',
        'external_id': 'external_id'
    }

    def __init__(self, id=None, name=None, price=None, group_name=None, vat_code=None, rkeeper_code=None, external_id=None):  # noqa: E501
        """IngredientForResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._price = None
        self._group_name = None
        self._vat_code = None
        self._rkeeper_code = None
        self._external_id = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.price = price
        self.group_name = group_name
        if vat_code is not None:
            self.vat_code = vat_code
        if rkeeper_code is not None:
            self.rkeeper_code = rkeeper_code
        if external_id is not None:
            self.external_id = external_id

    @property
    def id(self):
        """Gets the id of this IngredientForResponse.  # noqa: E501


        :return: The id of this IngredientForResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IngredientForResponse.


        :param id: The id of this IngredientForResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this IngredientForResponse.  # noqa: E501


        :return: The name of this IngredientForResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IngredientForResponse.


        :param name: The name of this IngredientForResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def price(self):
        """Gets the price of this IngredientForResponse.  # noqa: E501


        :return: The price of this IngredientForResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this IngredientForResponse.


        :param price: The price of this IngredientForResponse.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def group_name(self):
        """Gets the group_name of this IngredientForResponse.  # noqa: E501


        :return: The group_name of this IngredientForResponse.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this IngredientForResponse.


        :param group_name: The group_name of this IngredientForResponse.  # noqa: E501
        :type: str
        """
        if group_name is None:
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def vat_code(self):
        """Gets the vat_code of this IngredientForResponse.  # noqa: E501


        :return: The vat_code of this IngredientForResponse.  # noqa: E501
        :rtype: str
        """
        return self._vat_code

    @vat_code.setter
    def vat_code(self, vat_code):
        """Sets the vat_code of this IngredientForResponse.


        :param vat_code: The vat_code of this IngredientForResponse.  # noqa: E501
        :type: str
        """

        self._vat_code = vat_code

    @property
    def rkeeper_code(self):
        """Gets the rkeeper_code of this IngredientForResponse.  # noqa: E501


        :return: The rkeeper_code of this IngredientForResponse.  # noqa: E501
        :rtype: str
        """
        return self._rkeeper_code

    @rkeeper_code.setter
    def rkeeper_code(self, rkeeper_code):
        """Sets the rkeeper_code of this IngredientForResponse.


        :param rkeeper_code: The rkeeper_code of this IngredientForResponse.  # noqa: E501
        :type: str
        """

        self._rkeeper_code = rkeeper_code

    @property
    def external_id(self):
        """Gets the external_id of this IngredientForResponse.  # noqa: E501


        :return: The external_id of this IngredientForResponse.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this IngredientForResponse.


        :param external_id: The external_id of this IngredientForResponse.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

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
        if issubclass(IngredientForResponse, dict):
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
        if not isinstance(other, IngredientForResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
