# swagger_client.PingApi

All URIs are relative to */api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](PingApi.md#ping) | **GET** /ping | Get back a message indicating that the API is working.

# **ping**
> PingSchema ping(engine_tenant_name=engine_tenant_name)

Get back a message indicating that the API is working.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PingApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)

try:
    # Get back a message indicating that the API is working.
    api_response = api_instance.ping(engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingApi->ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 

### Return type

[**PingSchema**](PingSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

