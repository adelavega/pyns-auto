# coding: utf-8

"""
    neuroscout

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from pyns_auto.models.apianalyses_predictors import ApianalysesPredictors  # noqa: F401,E501
from pyns_auto.models.apidatasets_tasks import ApidatasetsTasks  # noqa: F401,E501


class InlineResponseDefault5(object):
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
        'description': 'object',
        'id': 'int',
        'name': 'str',
        'runs': 'list[ApianalysesPredictors]',
        'tasks': 'list[ApidatasetsTasks]'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'runs': 'runs',
        'tasks': 'tasks'
    }

    def __init__(self, description=None, id=None, name=None, runs=None, tasks=None):  # noqa: E501
        """InlineResponseDefault5 - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self._name = None
        self._runs = None
        self._tasks = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if runs is not None:
            self.runs = runs
        if tasks is not None:
            self.tasks = tasks

    @property
    def description(self):
        """Gets the description of this InlineResponseDefault5.  # noqa: E501


        :return: The description of this InlineResponseDefault5.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponseDefault5.


        :param description: The description of this InlineResponseDefault5.  # noqa: E501
        :type: object
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this InlineResponseDefault5.  # noqa: E501


        :return: The id of this InlineResponseDefault5.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponseDefault5.


        :param id: The id of this InlineResponseDefault5.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponseDefault5.  # noqa: E501

        Dataset name  # noqa: E501

        :return: The name of this InlineResponseDefault5.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponseDefault5.

        Dataset name  # noqa: E501

        :param name: The name of this InlineResponseDefault5.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def runs(self):
        """Gets the runs of this InlineResponseDefault5.  # noqa: E501


        :return: The runs of this InlineResponseDefault5.  # noqa: E501
        :rtype: list[ApianalysesPredictors]
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Sets the runs of this InlineResponseDefault5.


        :param runs: The runs of this InlineResponseDefault5.  # noqa: E501
        :type: list[ApianalysesPredictors]
        """

        self._runs = runs

    @property
    def tasks(self):
        """Gets the tasks of this InlineResponseDefault5.  # noqa: E501


        :return: The tasks of this InlineResponseDefault5.  # noqa: E501
        :rtype: list[ApidatasetsTasks]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this InlineResponseDefault5.


        :param tasks: The tasks of this InlineResponseDefault5.  # noqa: E501
        :type: list[ApidatasetsTasks]
        """

        self._tasks = tasks

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponseDefault5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other