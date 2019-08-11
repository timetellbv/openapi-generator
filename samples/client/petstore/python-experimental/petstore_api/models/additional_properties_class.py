# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AdditionalPropertiesClass(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'map_string': 'dict(str, str)',
        'map_number': 'dict(str, float)',
        'map_integer': 'dict(str, int)',
        'map_boolean': 'dict(str, bool)',
        'map_array_integer': 'dict(str, list[int])',
        'map_array_anytype': 'dict(str, list[object])',
        'map_map_string': 'dict(str, dict(str, str))',
        'map_map_anytype': 'dict(str, dict(str, object))',
        'anytype_1': 'object',
        'anytype_2': 'object',
        'anytype_3': 'object',
    }

    attribute_map = {
        'map_string': 'map_string',  # noqa: E501
        'map_number': 'map_number',  # noqa: E501
        'map_integer': 'map_integer',  # noqa: E501
        'map_boolean': 'map_boolean',  # noqa: E501
        'map_array_integer': 'map_array_integer',  # noqa: E501
        'map_array_anytype': 'map_array_anytype',  # noqa: E501
        'map_map_string': 'map_map_string',  # noqa: E501
        'map_map_anytype': 'map_map_anytype',  # noqa: E501
        'anytype_1': 'anytype_1',  # noqa: E501
        'anytype_2': 'anytype_2',  # noqa: E501
        'anytype_3': 'anytype_3',  # noqa: E501
    }

    def __init__(self, map_string=None, map_number=None, map_integer=None, map_boolean=None, map_array_integer=None, map_array_anytype=None, map_map_string=None, map_map_anytype=None, anytype_1=None, anytype_2=None, anytype_3=None):  # noqa: E501
        """AdditionalPropertiesClass - a model defined in OpenAPI



        Keyword Args:
            map_string (dict(str, str)): [optional]  # noqa: E501
            map_number (dict(str, float)): [optional]  # noqa: E501
            map_integer (dict(str, int)): [optional]  # noqa: E501
            map_boolean (dict(str, bool)): [optional]  # noqa: E501
            map_array_integer (dict(str, list[int])): [optional]  # noqa: E501
            map_array_anytype (dict(str, list[object])): [optional]  # noqa: E501
            map_map_string (dict(str, dict(str, str))): [optional]  # noqa: E501
            map_map_anytype (dict(str, dict(str, object))): [optional]  # noqa: E501
            anytype_1 (object): [optional]  # noqa: E501
            anytype_2 (object): [optional]  # noqa: E501
            anytype_3 (object): [optional]  # noqa: E501
        """

        self._map_string = None
        self._map_number = None
        self._map_integer = None
        self._map_boolean = None
        self._map_array_integer = None
        self._map_array_anytype = None
        self._map_map_string = None
        self._map_map_anytype = None
        self._anytype_1 = None
        self._anytype_2 = None
        self._anytype_3 = None
        self.discriminator = None

        if map_string is not None:
            self.map_string = map_string  # noqa: E501
        if map_number is not None:
            self.map_number = map_number  # noqa: E501
        if map_integer is not None:
            self.map_integer = map_integer  # noqa: E501
        if map_boolean is not None:
            self.map_boolean = map_boolean  # noqa: E501
        if map_array_integer is not None:
            self.map_array_integer = map_array_integer  # noqa: E501
        if map_array_anytype is not None:
            self.map_array_anytype = map_array_anytype  # noqa: E501
        if map_map_string is not None:
            self.map_map_string = map_map_string  # noqa: E501
        if map_map_anytype is not None:
            self.map_map_anytype = map_map_anytype  # noqa: E501
        if anytype_1 is not None:
            self.anytype_1 = anytype_1  # noqa: E501
        if anytype_2 is not None:
            self.anytype_2 = anytype_2  # noqa: E501
        if anytype_3 is not None:
            self.anytype_3 = anytype_3  # noqa: E501

    @property
    def map_string(self):
        """Gets the map_string of this AdditionalPropertiesClass.  # noqa: E501


        :return: The map_string of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._map_string

    @map_string.setter
    def map_string(
            self,
            map_string):
        """Sets the map_string of this AdditionalPropertiesClass.


        :param map_string: The map_string of this AdditionalPropertiesClass.  # noqa: E501
        :type: dict(str, str)
        """

        self._map_string = (
            map_string)

    @property
    def map_number(self):
        """Gets the map_number of this AdditionalPropertiesClass.  # noqa: E501


        :return: The map_number of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._map_number

    @map_number.setter
    def map_number(
            self,
            map_number):
        """Sets the map_number of this AdditionalPropertiesClass.


        :param map_number: The map_number of this AdditionalPropertiesClass.  # noqa: E501
        :type: dict(str, float)
        """

        self._map_number = (
            map_number)

    @property
    def map_integer(self):
        """Gets the map_integer of this AdditionalPropertiesClass.  # noqa: E501


        :return: The map_integer of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._map_integer

    @map_integer.setter
    def map_integer(
            self,
            map_integer):
        """Sets the map_integer of this AdditionalPropertiesClass.


        :param map_integer: The map_integer of this AdditionalPropertiesClass.  # noqa: E501
        :type: dict(str, int)
        """

        self._map_integer = (
            map_integer)

    @property
    def map_boolean(self):
        """Gets the map_boolean of this AdditionalPropertiesClass.  # noqa: E501


        :return: The map_boolean of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._map_boolean

    @map_boolean.setter
    def map_boolean(
            self,
            map_boolean):
        """Sets the map_boolean of this AdditionalPropertiesClass.


        :param map_boolean: The map_boolean of this AdditionalPropertiesClass.  # noqa: E501
        :type: dict(str, bool)
        """

        self._map_boolean = (
            map_boolean)

    @property
    def map_array_integer(self):
        """Gets the map_array_integer of this AdditionalPropertiesClass.  # noqa: E501


        :return: The map_array_integer of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: dict(str, list[int])
        """
        return self._map_array_integer

    @map_array_integer.setter
    def map_array_integer(
            self,
            map_array_integer):
        """Sets the map_array_integer of this AdditionalPropertiesClass.


        :param map_array_integer: The map_array_integer of this AdditionalPropertiesClass.  # noqa: E501
        :type: dict(str, list[int])
        """

        self._map_array_integer = (
            map_array_integer)

    @property
    def map_array_anytype(self):
        """Gets the map_array_anytype of this AdditionalPropertiesClass.  # noqa: E501


        :return: The map_array_anytype of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: dict(str, list[object])
        """
        return self._map_array_anytype

    @map_array_anytype.setter
    def map_array_anytype(
            self,
            map_array_anytype):
        """Sets the map_array_anytype of this AdditionalPropertiesClass.


        :param map_array_anytype: The map_array_anytype of this AdditionalPropertiesClass.  # noqa: E501
        :type: dict(str, list[object])
        """

        self._map_array_anytype = (
            map_array_anytype)

    @property
    def map_map_string(self):
        """Gets the map_map_string of this AdditionalPropertiesClass.  # noqa: E501


        :return: The map_map_string of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._map_map_string

    @map_map_string.setter
    def map_map_string(
            self,
            map_map_string):
        """Sets the map_map_string of this AdditionalPropertiesClass.


        :param map_map_string: The map_map_string of this AdditionalPropertiesClass.  # noqa: E501
        :type: dict(str, dict(str, str))
        """

        self._map_map_string = (
            map_map_string)

    @property
    def map_map_anytype(self):
        """Gets the map_map_anytype of this AdditionalPropertiesClass.  # noqa: E501


        :return: The map_map_anytype of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: dict(str, dict(str, object))
        """
        return self._map_map_anytype

    @map_map_anytype.setter
    def map_map_anytype(
            self,
            map_map_anytype):
        """Sets the map_map_anytype of this AdditionalPropertiesClass.


        :param map_map_anytype: The map_map_anytype of this AdditionalPropertiesClass.  # noqa: E501
        :type: dict(str, dict(str, object))
        """

        self._map_map_anytype = (
            map_map_anytype)

    @property
    def anytype_1(self):
        """Gets the anytype_1 of this AdditionalPropertiesClass.  # noqa: E501


        :return: The anytype_1 of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: object
        """
        return self._anytype_1

    @anytype_1.setter
    def anytype_1(
            self,
            anytype_1):
        """Sets the anytype_1 of this AdditionalPropertiesClass.


        :param anytype_1: The anytype_1 of this AdditionalPropertiesClass.  # noqa: E501
        :type: object
        """

        self._anytype_1 = (
            anytype_1)

    @property
    def anytype_2(self):
        """Gets the anytype_2 of this AdditionalPropertiesClass.  # noqa: E501


        :return: The anytype_2 of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: object
        """
        return self._anytype_2

    @anytype_2.setter
    def anytype_2(
            self,
            anytype_2):
        """Sets the anytype_2 of this AdditionalPropertiesClass.


        :param anytype_2: The anytype_2 of this AdditionalPropertiesClass.  # noqa: E501
        :type: object
        """

        self._anytype_2 = (
            anytype_2)

    @property
    def anytype_3(self):
        """Gets the anytype_3 of this AdditionalPropertiesClass.  # noqa: E501


        :return: The anytype_3 of this AdditionalPropertiesClass.  # noqa: E501
        :rtype: object
        """
        return self._anytype_3

    @anytype_3.setter
    def anytype_3(
            self,
            anytype_3):
        """Sets the anytype_3 of this AdditionalPropertiesClass.


        :param anytype_3: The anytype_3 of this AdditionalPropertiesClass.  # noqa: E501
        :type: object
        """

        self._anytype_3 = (
            anytype_3)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdditionalPropertiesClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
