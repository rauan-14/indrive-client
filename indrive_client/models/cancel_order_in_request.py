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

class CancelOrderInRequest(object):
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
        'cancel_code': 'OrderCancelCodeEnum',
        'cancel_reason': 'str'
    }

    attribute_map = {
        'cancel_code': 'cancel_code',
        'cancel_reason': 'cancel_reason'
    }

    def __init__(self, cancel_code=None, cancel_reason=None):  # noqa: E501
        """CancelOrderInRequest - a model defined in Swagger"""  # noqa: E501
        self._cancel_code = None
        self._cancel_reason = None
        self.discriminator = None
        self.cancel_code = cancel_code
        if cancel_reason is not None:
            self.cancel_reason = cancel_reason

    @property
    def cancel_code(self):
        """Gets the cancel_code of this CancelOrderInRequest.  # noqa: E501


        :return: The cancel_code of this CancelOrderInRequest.  # noqa: E501
        :rtype: OrderCancelCodeEnum
        """
        return self._cancel_code

    @cancel_code.setter
    def cancel_code(self, cancel_code):
        """Sets the cancel_code of this CancelOrderInRequest.


        :param cancel_code: The cancel_code of this CancelOrderInRequest.  # noqa: E501
        :type: OrderCancelCodeEnum
        """
        if cancel_code is None:
            raise ValueError("Invalid value for `cancel_code`, must not be `None`")  # noqa: E501

        self._cancel_code = cancel_code

    @property
    def cancel_reason(self):
        """Gets the cancel_reason of this CancelOrderInRequest.  # noqa: E501


        :return: The cancel_reason of this CancelOrderInRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancel_reason

    @cancel_reason.setter
    def cancel_reason(self, cancel_reason):
        """Sets the cancel_reason of this CancelOrderInRequest.


        :param cancel_reason: The cancel_reason of this CancelOrderInRequest.  # noqa: E501
        :type: str
        """

        self._cancel_reason = cancel_reason

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
        if issubclass(CancelOrderInRequest, dict):
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
        if not isinstance(other, CancelOrderInRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other