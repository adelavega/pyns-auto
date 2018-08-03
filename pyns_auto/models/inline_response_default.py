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


class InlineResponseDefault(object):
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
        'tr': 'float',
        'compile_traceback': 'str',
        'compiled_at': 'str',
        'created_at': 'str',
        'data': 'object',
        'dataset_id': 'int',
        'description': 'str',
        'hash_id': 'str',
        'model': 'object',
        'modified_at': 'str',
        'name': 'str',
        'parent_id': 'str',
        'predictions': 'str',
        'predictors': 'list[ApianalysesPredictors]',
        'private': 'bool',
        'runs': 'list[ApianalysesPredictors]',
        'status': 'str',
        'task_name': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'tr': 'TR',
        'compile_traceback': 'compile_traceback',
        'compiled_at': 'compiled_at',
        'created_at': 'created_at',
        'data': 'data',
        'dataset_id': 'dataset_id',
        'description': 'description',
        'hash_id': 'hash_id',
        'model': 'model',
        'modified_at': 'modified_at',
        'name': 'name',
        'parent_id': 'parent_id',
        'predictions': 'predictions',
        'predictors': 'predictors',
        'private': 'private',
        'runs': 'runs',
        'status': 'status',
        'task_name': 'task_name',
        'user_id': 'user_id'
    }

    def __init__(self, tr=None, compile_traceback=None, compiled_at=None, created_at=None, data=None, dataset_id=None, description=None, hash_id=None, model=None, modified_at=None, name=None, parent_id=None, predictions=None, predictors=None, private=None, runs=None, status=None, task_name=None, user_id=None):  # noqa: E501
        """InlineResponseDefault - a model defined in Swagger"""  # noqa: E501

        self._tr = None
        self._compile_traceback = None
        self._compiled_at = None
        self._created_at = None
        self._data = None
        self._dataset_id = None
        self._description = None
        self._hash_id = None
        self._model = None
        self._modified_at = None
        self._name = None
        self._parent_id = None
        self._predictions = None
        self._predictors = None
        self._private = None
        self._runs = None
        self._status = None
        self._task_name = None
        self._user_id = None
        self.discriminator = None

        if tr is not None:
            self.tr = tr
        if compile_traceback is not None:
            self.compile_traceback = compile_traceback
        if compiled_at is not None:
            self.compiled_at = compiled_at
        if created_at is not None:
            self.created_at = created_at
        if data is not None:
            self.data = data
        self.dataset_id = dataset_id
        if description is not None:
            self.description = description
        if hash_id is not None:
            self.hash_id = hash_id
        if model is not None:
            self.model = model
        if modified_at is not None:
            self.modified_at = modified_at
        self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if predictions is not None:
            self.predictions = predictions
        if predictors is not None:
            self.predictors = predictors
        if private is not None:
            self.private = private
        if runs is not None:
            self.runs = runs
        if status is not None:
            self.status = status
        if task_name is not None:
            self.task_name = task_name
        if user_id is not None:
            self.user_id = user_id

    @property
    def tr(self):
        """Gets the tr of this InlineResponseDefault.  # noqa: E501

        Time repetition (s)  # noqa: E501

        :return: The tr of this InlineResponseDefault.  # noqa: E501
        :rtype: float
        """
        return self._tr

    @tr.setter
    def tr(self, tr):
        """Sets the tr of this InlineResponseDefault.

        Time repetition (s)  # noqa: E501

        :param tr: The tr of this InlineResponseDefault.  # noqa: E501
        :type: float
        """

        self._tr = tr

    @property
    def compile_traceback(self):
        """Gets the compile_traceback of this InlineResponseDefault.  # noqa: E501

        Traceback of compilation error.  # noqa: E501

        :return: The compile_traceback of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._compile_traceback

    @compile_traceback.setter
    def compile_traceback(self, compile_traceback):
        """Sets the compile_traceback of this InlineResponseDefault.

        Traceback of compilation error.  # noqa: E501

        :param compile_traceback: The compile_traceback of this InlineResponseDefault.  # noqa: E501
        :type: str
        """

        self._compile_traceback = compile_traceback

    @property
    def compiled_at(self):
        """Gets the compiled_at of this InlineResponseDefault.  # noqa: E501

        Timestamp of when analysis was compiled  # noqa: E501

        :return: The compiled_at of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._compiled_at

    @compiled_at.setter
    def compiled_at(self, compiled_at):
        """Sets the compiled_at of this InlineResponseDefault.

        Timestamp of when analysis was compiled  # noqa: E501

        :param compiled_at: The compiled_at of this InlineResponseDefault.  # noqa: E501
        :type: str
        """

        self._compiled_at = compiled_at

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponseDefault.  # noqa: E501


        :return: The created_at of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponseDefault.


        :param created_at: The created_at of this InlineResponseDefault.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def data(self):
        """Gets the data of this InlineResponseDefault.  # noqa: E501


        :return: The data of this InlineResponseDefault.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponseDefault.


        :param data: The data of this InlineResponseDefault.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def dataset_id(self):
        """Gets the dataset_id of this InlineResponseDefault.  # noqa: E501


        :return: The dataset_id of this InlineResponseDefault.  # noqa: E501
        :rtype: int
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this InlineResponseDefault.


        :param dataset_id: The dataset_id of this InlineResponseDefault.  # noqa: E501
        :type: int
        """
        if dataset_id is None:
            raise ValueError("Invalid value for `dataset_id`, must not be `None`")  # noqa: E501

        self._dataset_id = dataset_id

    @property
    def description(self):
        """Gets the description of this InlineResponseDefault.  # noqa: E501


        :return: The description of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InlineResponseDefault.


        :param description: The description of this InlineResponseDefault.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hash_id(self):
        """Gets the hash_id of this InlineResponseDefault.  # noqa: E501

        Hashed analysis id.  # noqa: E501

        :return: The hash_id of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._hash_id

    @hash_id.setter
    def hash_id(self, hash_id):
        """Sets the hash_id of this InlineResponseDefault.

        Hashed analysis id.  # noqa: E501

        :param hash_id: The hash_id of this InlineResponseDefault.  # noqa: E501
        :type: str
        """

        self._hash_id = hash_id

    @property
    def model(self):
        """Gets the model of this InlineResponseDefault.  # noqa: E501

        BIDS model.  # noqa: E501

        :return: The model of this InlineResponseDefault.  # noqa: E501
        :rtype: object
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this InlineResponseDefault.

        BIDS model.  # noqa: E501

        :param model: The model of this InlineResponseDefault.  # noqa: E501
        :type: object
        """

        self._model = model

    @property
    def modified_at(self):
        """Gets the modified_at of this InlineResponseDefault.  # noqa: E501


        :return: The modified_at of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this InlineResponseDefault.


        :param modified_at: The modified_at of this InlineResponseDefault.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

    @property
    def name(self):
        """Gets the name of this InlineResponseDefault.  # noqa: E501

        Analysis name.  # noqa: E501

        :return: The name of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponseDefault.

        Analysis name.  # noqa: E501

        :param name: The name of this InlineResponseDefault.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this InlineResponseDefault.  # noqa: E501

        Parent analysis, if cloned.  # noqa: E501

        :return: The parent_id of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this InlineResponseDefault.

        Parent analysis, if cloned.  # noqa: E501

        :param parent_id: The parent_id of this InlineResponseDefault.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def predictions(self):
        """Gets the predictions of this InlineResponseDefault.  # noqa: E501

        User apriori predictions.  # noqa: E501

        :return: The predictions of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._predictions

    @predictions.setter
    def predictions(self, predictions):
        """Sets the predictions of this InlineResponseDefault.

        User apriori predictions.  # noqa: E501

        :param predictions: The predictions of this InlineResponseDefault.  # noqa: E501
        :type: str
        """

        self._predictions = predictions

    @property
    def predictors(self):
        """Gets the predictors of this InlineResponseDefault.  # noqa: E501

        Predictor id(s) associated with analysis  # noqa: E501

        :return: The predictors of this InlineResponseDefault.  # noqa: E501
        :rtype: list[ApianalysesPredictors]
        """
        return self._predictors

    @predictors.setter
    def predictors(self, predictors):
        """Sets the predictors of this InlineResponseDefault.

        Predictor id(s) associated with analysis  # noqa: E501

        :param predictors: The predictors of this InlineResponseDefault.  # noqa: E501
        :type: list[ApianalysesPredictors]
        """

        self._predictors = predictors

    @property
    def private(self):
        """Gets the private of this InlineResponseDefault.  # noqa: E501

        Analysis private or discoverable?  # noqa: E501

        :return: The private of this InlineResponseDefault.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this InlineResponseDefault.

        Analysis private or discoverable?  # noqa: E501

        :param private: The private of this InlineResponseDefault.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def runs(self):
        """Gets the runs of this InlineResponseDefault.  # noqa: E501

        Runs associated with analysis  # noqa: E501

        :return: The runs of this InlineResponseDefault.  # noqa: E501
        :rtype: list[ApianalysesPredictors]
        """
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Sets the runs of this InlineResponseDefault.

        Runs associated with analysis  # noqa: E501

        :param runs: The runs of this InlineResponseDefault.  # noqa: E501
        :type: list[ApianalysesPredictors]
        """

        self._runs = runs

    @property
    def status(self):
        """Gets the status of this InlineResponseDefault.  # noqa: E501

        PASSED, FAILED, PENDING, or DRAFT.  # noqa: E501

        :return: The status of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponseDefault.

        PASSED, FAILED, PENDING, or DRAFT.  # noqa: E501

        :param status: The status of this InlineResponseDefault.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def task_name(self):
        """Gets the task_name of this InlineResponseDefault.  # noqa: E501

        Task name  # noqa: E501

        :return: The task_name of this InlineResponseDefault.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this InlineResponseDefault.

        Task name  # noqa: E501

        :param task_name: The task_name of this InlineResponseDefault.  # noqa: E501
        :type: str
        """

        self._task_name = task_name

    @property
    def user_id(self):
        """Gets the user_id of this InlineResponseDefault.  # noqa: E501


        :return: The user_id of this InlineResponseDefault.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InlineResponseDefault.


        :param user_id: The user_id of this InlineResponseDefault.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if not isinstance(other, InlineResponseDefault):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
