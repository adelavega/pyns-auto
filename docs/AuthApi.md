# pyns_auto.AuthApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_auth_post**](AuthApi.md#api_auth_post) | **POST** /api/auth | Get JWT authorizaton token.


# **api_auth_post**
> InlineResponseDefault4 api_auth_post(body)

Get JWT authorizaton token.

### Example
```python
from __future__ import print_function
import time
import pyns_auto
from pyns_auto.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyns_auto.AuthApi()
body = pyns_auto.Body2() # Body2 | 

try:
    # Get JWT authorizaton token.
    api_response = api_instance.api_auth_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->api_auth_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)|  | 

### Return type

[**InlineResponseDefault4**](InlineResponseDefault4.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

