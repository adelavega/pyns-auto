# pyns-auto
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import pyns_auto 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pyns_auto
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import pyns_auto
from pyns_auto.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = pyns_auto.AnalysisApi()
analysis_id = 'analysis_id_example' # str | 

try:
    # Get analysis tarball bundle.
    api_instance.api_analyses_analysis_id_bundle_get(analysis_id)
except ApiException as e:
    print("Exception when calling AnalysisApi->api_analyses_analysis_id_bundle_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalysisApi* | [**api_analyses_analysis_id_bundle_get**](docs/AnalysisApi.md#api_analyses_analysis_id_bundle_get) | **GET** /api/analyses/{analysis_id}/bundle | Get analysis tarball bundle.
*AnalysisApi* | [**api_analyses_analysis_id_clone_post**](docs/AnalysisApi.md#api_analyses_analysis_id_clone_post) | **POST** /api/analyses/{analysis_id}/clone | Clone analysis.
*AnalysisApi* | [**api_analyses_analysis_id_compile_post**](docs/AnalysisApi.md#api_analyses_analysis_id_compile_post) | **POST** /api/analyses/{analysis_id}/compile | Compile and lock analysis.
*AnalysisApi* | [**api_analyses_analysis_id_delete**](docs/AnalysisApi.md#api_analyses_analysis_id_delete) | **DELETE** /api/analyses/{analysis_id} | Delete analysis.
*AnalysisApi* | [**api_analyses_analysis_id_full_get**](docs/AnalysisApi.md#api_analyses_analysis_id_full_get) | **GET** /api/analyses/{analysis_id}/full | Get analysis (including nested fields).
*AnalysisApi* | [**api_analyses_analysis_id_get**](docs/AnalysisApi.md#api_analyses_analysis_id_get) | **GET** /api/analyses/{analysis_id} | Get analysis by id.
*AnalysisApi* | [**api_analyses_analysis_id_put**](docs/AnalysisApi.md#api_analyses_analysis_id_put) | **PUT** /api/analyses/{analysis_id} | Edit analysis.
*AnalysisApi* | [**api_analyses_analysis_id_resources_get**](docs/AnalysisApi.md#api_analyses_analysis_id_resources_get) | **GET** /api/analyses/{analysis_id}/resources | Get analysis resources.
*AnalysisApi* | [**api_analyses_analysis_id_status_get**](docs/AnalysisApi.md#api_analyses_analysis_id_status_get) | **GET** /api/analyses/{analysis_id}/status | Check if analysis has compiled.
*AnalysisApi* | [**api_analyses_get**](docs/AnalysisApi.md#api_analyses_get) | **GET** /api/analyses | Returns list of public analyses.
*AnalysisApi* | [**api_analyses_post**](docs/AnalysisApi.md#api_analyses_post) | **POST** /api/analyses | Add new analysis!
*AuthApi* | [**api_auth_post**](docs/AuthApi.md#api_auth_post) | **POST** /api/auth | Get JWT authorizaton token.
*DatasetApi* | [**api_datasets_dataset_id_get**](docs/DatasetApi.md#api_datasets_dataset_id_get) | **GET** /api/datasets/{dataset_id} | Get dataset by id.
*DatasetApi* | [**api_datasets_get**](docs/DatasetApi.md#api_datasets_get) | **GET** /api/datasets | Returns list of datasets.
*DefaultApi* | [**api_user_get**](docs/DefaultApi.md#api_user_get) | **GET** /api/user | Get current user information.
*DefaultApi* | [**api_user_post**](docs/DefaultApi.md#api_user_post) | **POST** /api/user | Add a new user.
*DefaultApi* | [**api_user_put**](docs/DefaultApi.md#api_user_put) | **PUT** /api/user | Edit user information.
*DefaultApi* | [**api_user_resend_confirmation_post**](docs/DefaultApi.md#api_user_resend_confirmation_post) | **POST** /api/user/resend_confirmation | Resend confirmation email.
*DefaultApi* | [**api_user_reset_password_post**](docs/DefaultApi.md#api_user_reset_password_post) | **POST** /api/user/reset_password | 
*DefaultApi* | [**api_user_submit_token_post**](docs/DefaultApi.md#api_user_submit_token_post) | **POST** /api/user/submit_token | 
*PredictorsApi* | [**api_predictor_events_get**](docs/PredictorsApi.md#api_predictor_events_get) | **GET** /api/predictor-events | Get events for predictor(s)
*PredictorsApi* | [**api_predictors_get**](docs/PredictorsApi.md#api_predictors_get) | **GET** /api/predictors | Get list of predictors.
*PredictorsApi* | [**api_predictors_predictor_id_get**](docs/PredictorsApi.md#api_predictors_predictor_id_get) | **GET** /api/predictors/{predictor_id} | Get predictor by id.
*RunApi* | [**api_runs_get**](docs/RunApi.md#api_runs_get) | **GET** /api/runs | Returns list of runs.
*RunApi* | [**api_runs_run_id_get**](docs/RunApi.md#api_runs_run_id_get) | **GET** /api/runs/{run_id} | Get run by id.
*RunApi* | [**api_tasks_get**](docs/RunApi.md#api_tasks_get) | **GET** /api/tasks | Returns list of tasks.
*RunApi* | [**api_tasks_task_id_get**](docs/RunApi.md#api_tasks_task_id_get) | **GET** /api/tasks/{task_id} | Get task by id.


## Documentation For Models

 - [ApianalysesPredictors](docs/ApianalysesPredictors.md)
 - [ApidatasetsTasks](docs/ApidatasetsTasks.md)
 - [ApipredictorsExtractedFeature](docs/ApipredictorsExtractedFeature.md)
 - [ApirunsTask](docs/ApirunsTask.md)
 - [Body](docs/Body.md)
 - [Body1](docs/Body1.md)
 - [Body2](docs/Body2.md)
 - [Body3](docs/Body3.md)
 - [Body4](docs/Body4.md)
 - [Body5](docs/Body5.md)
 - [Body6](docs/Body6.md)
 - [InlineResponseDefault](docs/InlineResponseDefault.md)
 - [InlineResponseDefault1](docs/InlineResponseDefault1.md)
 - [InlineResponseDefault10](docs/InlineResponseDefault10.md)
 - [InlineResponseDefault11](docs/InlineResponseDefault11.md)
 - [InlineResponseDefault12](docs/InlineResponseDefault12.md)
 - [InlineResponseDefault12Analyses](docs/InlineResponseDefault12Analyses.md)
 - [InlineResponseDefault1Predictors](docs/InlineResponseDefault1Predictors.md)
 - [InlineResponseDefault1Runs](docs/InlineResponseDefault1Runs.md)
 - [InlineResponseDefault2](docs/InlineResponseDefault2.md)
 - [InlineResponseDefault2DatasetAddress](docs/InlineResponseDefault2DatasetAddress.md)
 - [InlineResponseDefault2DatasetName](docs/InlineResponseDefault2DatasetName.md)
 - [InlineResponseDefault2FuncPaths](docs/InlineResponseDefault2FuncPaths.md)
 - [InlineResponseDefault2MaskPaths](docs/InlineResponseDefault2MaskPaths.md)
 - [InlineResponseDefault2PreprocAddress](docs/InlineResponseDefault2PreprocAddress.md)
 - [InlineResponseDefault3](docs/InlineResponseDefault3.md)
 - [InlineResponseDefault4](docs/InlineResponseDefault4.md)
 - [InlineResponseDefault5](docs/InlineResponseDefault5.md)
 - [InlineResponseDefault6](docs/InlineResponseDefault6.md)
 - [InlineResponseDefault7](docs/InlineResponseDefault7.md)
 - [InlineResponseDefault8](docs/InlineResponseDefault8.md)
 - [InlineResponseDefault9](docs/InlineResponseDefault9.md)
 - [InlineResponseDefault9RunStatistics](docs/InlineResponseDefault9RunStatistics.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author


