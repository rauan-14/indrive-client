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

class RegularSchedule(object):
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
        'week_day': 'int',
        'time_start': 'str',
        'time_end': 'str',
        'is_work': 'bool'
    }

    attribute_map = {
        'week_day': 'week_day',
        'time_start': 'time_start',
        'time_end': 'time_end',
        'is_work': 'is_work'
    }

    def __init__(self, week_day=None, time_start=None, time_end=None, is_work=None):  # noqa: E501
        """RegularSchedule - a model defined in Swagger"""  # noqa: E501
        self._week_day = None
        self._time_start = None
        self._time_end = None
        self._is_work = None
        self.discriminator = None
        self.week_day = week_day
        self.time_start = time_start
        self.time_end = time_end
        self.is_work = is_work

    @property
    def week_day(self):
        """Gets the week_day of this RegularSchedule.  # noqa: E501


        :return: The week_day of this RegularSchedule.  # noqa: E501
        :rtype: int
        """
        return self._week_day

    @week_day.setter
    def week_day(self, week_day):
        """Sets the week_day of this RegularSchedule.


        :param week_day: The week_day of this RegularSchedule.  # noqa: E501
        :type: int
        """
        if week_day is None:
            raise ValueError("Invalid value for `week_day`, must not be `None`")  # noqa: E501

        self._week_day = week_day

    @property
    def time_start(self):
        """Gets the time_start of this RegularSchedule.  # noqa: E501


        :return: The time_start of this RegularSchedule.  # noqa: E501
        :rtype: str
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """Sets the time_start of this RegularSchedule.


        :param time_start: The time_start of this RegularSchedule.  # noqa: E501
        :type: str
        """
        if time_start is None:
            raise ValueError("Invalid value for `time_start`, must not be `None`")  # noqa: E501

        self._time_start = time_start

    @property
    def time_end(self):
        """Gets the time_end of this RegularSchedule.  # noqa: E501


        :return: The time_end of this RegularSchedule.  # noqa: E501
        :rtype: str
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """Sets the time_end of this RegularSchedule.


        :param time_end: The time_end of this RegularSchedule.  # noqa: E501
        :type: str
        """
        if time_end is None:
            raise ValueError("Invalid value for `time_end`, must not be `None`")  # noqa: E501

        self._time_end = time_end

    @property
    def is_work(self):
        """Gets the is_work of this RegularSchedule.  # noqa: E501


        :return: The is_work of this RegularSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._is_work

    @is_work.setter
    def is_work(self, is_work):
        """Sets the is_work of this RegularSchedule.


        :param is_work: The is_work of this RegularSchedule.  # noqa: E501
        :type: bool
        """
        if is_work is None:
            raise ValueError("Invalid value for `is_work`, must not be `None`")  # noqa: E501

        self._is_work = is_work

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
        if issubclass(RegularSchedule, dict):
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
        if not isinstance(other, RegularSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
