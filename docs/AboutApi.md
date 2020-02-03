# rustici_engine.AboutApi

All URIs are relative to */api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_about**](AboutApi.md#get_about) | **GET** /about | Get back the version and platform of the running instance of Engine
[**get_user_count**](AboutApi.md#get_user_count) | **GET** /about/userCount | Gets the number of users for the specified tenant or across all tenants when none is specified

# **get_about**
> AboutSchema get_about(engine_tenant_name=engine_tenant_name)

Get back the version and platform of the running instance of Engine

### Example
```python
from __future__ import print_function
import time
import rustici_engine
from rustici_engine.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = rustici_engine.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: oauth
configuration = rustici_engine.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_engine.AboutApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)

try:
    # Get back the version and platform of the running instance of Engine
    api_response = api_instance.get_about(engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->get_about: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 

### Return type

[**AboutSchema**](AboutSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_count**
> UserCountSummarySchema get_user_count(engine_tenant_name=engine_tenant_name, since=since, until=until)

Gets the number of users for the specified tenant or across all tenants when none is specified

### Example
```python
from __future__ import print_function
import time
import rustici_engine
from rustici_engine.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic
configuration = rustici_engine.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: oauth
configuration = rustici_engine.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_engine.AboutApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)

try:
    # Gets the number of users for the specified tenant or across all tenants when none is specified
    api_response = api_instance.get_user_count(engine_tenant_name=engine_tenant_name, since=since, until=until)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AboutApi->get_user_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 

### Return type

[**UserCountSummarySchema**](UserCountSummarySchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

