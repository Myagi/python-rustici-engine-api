# swagger_client.DispatchApi

All URIs are relative to */api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_destinations**](DispatchApi.md#create_destinations) | **POST** /dispatch/destinations | Create multiple destinations
[**create_dispatches**](DispatchApi.md#create_dispatches) | **POST** /dispatch/dispatches | Create multiple dispatches
[**delete_destination**](DispatchApi.md#delete_destination) | **DELETE** /dispatch/destinations/{destinationId} | Delete the destination with id &#x60;destinationId&#x60;
[**delete_destination_dispatches**](DispatchApi.md#delete_destination_dispatches) | **DELETE** /dispatch/destinations/{destinationId}/dispatches | Delete all dispatches associated with this destination
[**delete_dispatch**](DispatchApi.md#delete_dispatch) | **DELETE** /dispatch/dispatches/{dispatchId} | Delete the dispatch with id &#x60;dispatchId&#x60;
[**enable_registration_instancing**](DispatchApi.md#enable_registration_instancing) | **POST** /dispatch/destinations/{destinationId}/dispatches/registrationInstancing | Enable or disable registration instancing
[**get_destination**](DispatchApi.md#get_destination) | **GET** /dispatch/destinations/{destinationId} | Get the destination with id &#x60;destinationId&#x60;
[**get_destination_dispatch_registration_count**](DispatchApi.md#get_destination_dispatch_registration_count) | **GET** /dispatch/destinations/{destinationId}/registrationCount | Get the registration count for all related dispatch registrations
[**get_destination_dispatch_zip**](DispatchApi.md#get_destination_dispatch_zip) | **GET** /dispatch/destinations/{destinationId}/dispatches/zip | Get a ZIP file containing all dispatch packages related to a destination.
[**get_destination_dispatches**](DispatchApi.md#get_destination_dispatches) | **GET** /dispatch/destinations/{destinationId}/dispatches | Get a list of related dispatches
[**get_destinations**](DispatchApi.md#get_destinations) | **GET** /dispatch/destinations | Get a list of destinations
[**get_dispatch**](DispatchApi.md#get_dispatch) | **GET** /dispatch/dispatches/{dispatchId} | Get the dispatch with id &#x60;dispatchId&#x60;
[**get_dispatch_enabled**](DispatchApi.md#get_dispatch_enabled) | **GET** /dispatch/dispatches/{dispatchId}/enabled | Returns boolean indicating if dispatch with id &#x60;dispatchId&#x60; is enabled
[**get_dispatch_registration_count**](DispatchApi.md#get_dispatch_registration_count) | **GET** /dispatch/dispatches/{dispatchId}/registrationCount | Get the registration count for this dispatch, and the date and time of the last count reset, if any.
[**get_dispatch_zip**](DispatchApi.md#get_dispatch_zip) | **GET** /dispatch/dispatches/{dispatchId}/zip | Get the ZIP dispatch package.
[**get_dispatches**](DispatchApi.md#get_dispatches) | **GET** /dispatch/dispatches | Get a list of dispatches
[**get_lti_dispatch**](DispatchApi.md#get_lti_dispatch) | **GET** /dispatch/dispatches/{dispatchId}/lti | Get the information necessary to launch this dispatch using the IMS LTI specification.
[**post_dispatch_lti_reporters**](DispatchApi.md#post_dispatch_lti_reporters) | **POST** /dispatch/ltiReporters | Set up a temporary LTI reporter; for use by products that use their own LTI entry points
[**reset_destination_dispatch_registration_count**](DispatchApi.md#reset_destination_dispatch_registration_count) | **DELETE** /dispatch/destinations/{destinationId}/registrationCount | Reset the registration count for related dispatches.
[**reset_dispatch_registration_count**](DispatchApi.md#reset_dispatch_registration_count) | **DELETE** /dispatch/dispatches/{dispatchId}/registrationCount | Reset the registration count for this dispatch.
[**set_destination**](DispatchApi.md#set_destination) | **PUT** /dispatch/destinations/{destinationId} | Create or update the destination with id &#x60;destinationId&#x60;
[**set_destination_dispatch_enabled**](DispatchApi.md#set_destination_dispatch_enabled) | **POST** /dispatch/destinations/{destinationId}/dispatches/enabled | Enable or disable all related dispatches
[**set_dispatch_enabled**](DispatchApi.md#set_dispatch_enabled) | **PUT** /dispatch/dispatches/{dispatchId}/enabled | Enable or disable the dispatch
[**update_dispatch**](DispatchApi.md#update_dispatch) | **PUT** /dispatch/dispatches/{dispatchId} | Update the dispatch with id &#x60;dispatchId&#x60;

# **create_destinations**
> create_destinations(body, engine_tenant_name)

Create multiple destinations

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
body = swagger_client.DestinationListSchema() # DestinationListSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request

try:
    # Create multiple destinations
    api_instance.create_destinations(body, engine_tenant_name)
except ApiException as e:
    print("Exception when calling DispatchApi->create_destinations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DestinationListSchema**](DestinationListSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dispatches**
> create_dispatches(body, engine_tenant_name)

Create multiple dispatches

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateDispatchListSchema() # CreateDispatchListSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request

try:
    # Create multiple dispatches
    api_instance.create_dispatches(body, engine_tenant_name)
except ApiException as e:
    print("Exception when calling DispatchApi->create_dispatches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDispatchListSchema**](CreateDispatchListSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_destination**
> delete_destination(engine_tenant_name, destination_id)

Delete the destination with id `destinationId`

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
destination_id = 'destination_id_example' # str | 

try:
    # Delete the destination with id `destinationId`
    api_instance.delete_destination(engine_tenant_name, destination_id)
except ApiException as e:
    print("Exception when calling DispatchApi->delete_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **destination_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_destination_dispatches**
> delete_destination_dispatches(engine_tenant_name, destination_id)

Delete all dispatches associated with this destination

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
destination_id = 'destination_id_example' # str | 

try:
    # Delete all dispatches associated with this destination
    api_instance.delete_destination_dispatches(engine_tenant_name, destination_id)
except ApiException as e:
    print("Exception when calling DispatchApi->delete_destination_dispatches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **destination_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dispatch**
> delete_dispatch(engine_tenant_name, dispatch_id)

Delete the dispatch with id `dispatchId`

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
dispatch_id = 'dispatch_id_example' # str | 

try:
    # Delete the dispatch with id `dispatchId`
    api_instance.delete_dispatch(engine_tenant_name, dispatch_id)
except ApiException as e:
    print("Exception when calling DispatchApi->delete_dispatch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **dispatch_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_registration_instancing**
> enable_registration_instancing(body, engine_tenant_name, destination_id)

Enable or disable registration instancing

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EnabledSchema() # EnabledSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
destination_id = 'destination_id_example' # str | 

try:
    # Enable or disable registration instancing
    api_instance.enable_registration_instancing(body, engine_tenant_name, destination_id)
except ApiException as e:
    print("Exception when calling DispatchApi->enable_registration_instancing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnabledSchema**](EnabledSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **destination_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination**
> DestinationSchema get_destination(engine_tenant_name, destination_id)

Get the destination with id `destinationId`

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
destination_id = 'destination_id_example' # str | 

try:
    # Get the destination with id `destinationId`
    api_response = api_instance.get_destination(engine_tenant_name, destination_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **destination_id** | **str**|  | 

### Return type

[**DestinationSchema**](DestinationSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination_dispatch_registration_count**
> IntegerResultSchema get_destination_dispatch_registration_count(engine_tenant_name, destination_id)

Get the registration count for all related dispatch registrations

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
destination_id = 'destination_id_example' # str | 

try:
    # Get the registration count for all related dispatch registrations
    api_response = api_instance.get_destination_dispatch_registration_count(engine_tenant_name, destination_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_destination_dispatch_registration_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **destination_id** | **str**|  | 

### Return type

[**IntegerResultSchema**](IntegerResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination_dispatch_zip**
> str get_destination_dispatch_zip(engine_tenant_name, destination_id, type=type)

Get a ZIP file containing all dispatch packages related to a destination.

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
destination_id = 'destination_id_example' # str | 
type = 'type_example' # str | The type of dispatch package to export (SCORM12, SCORM2004-3RD or AICC) (optional)

try:
    # Get a ZIP file containing all dispatch packages related to a destination.
    api_response = api_instance.get_destination_dispatch_zip(engine_tenant_name, destination_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_destination_dispatch_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **destination_id** | **str**|  | 
 **type** | **str**| The type of dispatch package to export (SCORM12, SCORM2004-3RD or AICC) | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination_dispatches**
> DispatchListSchema get_destination_dispatches(engine_tenant_name, destination_id, more=more, since=since, until=until)

Get a list of related dispatches

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
destination_id = 'destination_id_example' # str | 
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)

try:
    # Get a list of related dispatches
    api_response = api_instance.get_destination_dispatches(engine_tenant_name, destination_id, more=more, since=since, until=until)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_destination_dispatches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **destination_id** | **str**|  | 
 **more** | **str**| Value for this parameter will be provided in the &#x27;more&#x27; property of lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 

### Return type

[**DispatchListSchema**](DispatchListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destinations**
> DestinationListSchema get_destinations(engine_tenant_name, more=more, since=since, until=until, course_id=course_id)

Get a list of destinations

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
course_id = 'course_id_example' # str | Limit the results to destinations that have dispatches of the specified course (optional)

try:
    # Get a list of destinations
    api_response = api_instance.get_destinations(engine_tenant_name, more=more, since=since, until=until, course_id=course_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_destinations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **more** | **str**| Value for this parameter will be provided in the &#x27;more&#x27; property of lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **course_id** | **str**| Limit the results to destinations that have dispatches of the specified course | [optional] 

### Return type

[**DestinationListSchema**](DestinationListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dispatch**
> DispatchSchema get_dispatch(engine_tenant_name, dispatch_id)

Get the dispatch with id `dispatchId`

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
dispatch_id = 'dispatch_id_example' # str | 

try:
    # Get the dispatch with id `dispatchId`
    api_response = api_instance.get_dispatch(engine_tenant_name, dispatch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_dispatch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **dispatch_id** | **str**|  | 

### Return type

[**DispatchSchema**](DispatchSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dispatch_enabled**
> EnabledSchema get_dispatch_enabled(engine_tenant_name, dispatch_id)

Returns boolean indicating if dispatch with id `dispatchId` is enabled

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
dispatch_id = 'dispatch_id_example' # str | 

try:
    # Returns boolean indicating if dispatch with id `dispatchId` is enabled
    api_response = api_instance.get_dispatch_enabled(engine_tenant_name, dispatch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_dispatch_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **dispatch_id** | **str**|  | 

### Return type

[**EnabledSchema**](EnabledSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dispatch_registration_count**
> DispatchRegistrationCountSchema get_dispatch_registration_count(engine_tenant_name, dispatch_id)

Get the registration count for this dispatch, and the date and time of the last count reset, if any.

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
dispatch_id = 'dispatch_id_example' # str | 

try:
    # Get the registration count for this dispatch, and the date and time of the last count reset, if any.
    api_response = api_instance.get_dispatch_registration_count(engine_tenant_name, dispatch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_dispatch_registration_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **dispatch_id** | **str**|  | 

### Return type

[**DispatchRegistrationCountSchema**](DispatchRegistrationCountSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dispatch_zip**
> str get_dispatch_zip(engine_tenant_name, dispatch_id, type=type)

Get the ZIP dispatch package.

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
dispatch_id = 'dispatch_id_example' # str | 
type = 'type_example' # str | The type of dispatch package to export (SCORM12, SCORM2004-3RD or AICC) (optional)

try:
    # Get the ZIP dispatch package.
    api_response = api_instance.get_dispatch_zip(engine_tenant_name, dispatch_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_dispatch_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **dispatch_id** | **str**|  | 
 **type** | **str**| The type of dispatch package to export (SCORM12, SCORM2004-3RD or AICC) | [optional] 

### Return type

**str**

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dispatches**
> DispatchListSchema get_dispatches(engine_tenant_name, more=more, since=since, until=until, course_id=course_id)

Get a list of dispatches

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
course_id = 'course_id_example' # str | Limit the results to dispatches of the specified course (optional)

try:
    # Get a list of dispatches
    api_response = api_instance.get_dispatches(engine_tenant_name, more=more, since=since, until=until, course_id=course_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_dispatches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **more** | **str**| Value for this parameter will be provided in the &#x27;more&#x27; property of lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **course_id** | **str**| Limit the results to dispatches of the specified course | [optional] 

### Return type

[**DispatchListSchema**](DispatchListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lti_dispatch**
> DispatchLtiInfoSchema get_lti_dispatch(engine_tenant_name, dispatch_id)

Get the information necessary to launch this dispatch using the IMS LTI specification.

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
dispatch_id = 'dispatch_id_example' # str | 

try:
    # Get the information necessary to launch this dispatch using the IMS LTI specification.
    api_response = api_instance.get_lti_dispatch(engine_tenant_name, dispatch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->get_lti_dispatch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **dispatch_id** | **str**|  | 

### Return type

[**DispatchLtiInfoSchema**](DispatchLtiInfoSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dispatch_lti_reporters**
> LtiReporterIdSchema post_dispatch_lti_reporters(body, engine_tenant_name)

Set up a temporary LTI reporter; for use by products that use their own LTI entry points

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
body = swagger_client.LtiReporterSchema() # LtiReporterSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request

try:
    # Set up a temporary LTI reporter; for use by products that use their own LTI entry points
    api_response = api_instance.post_dispatch_lti_reporters(body, engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DispatchApi->post_dispatch_lti_reporters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LtiReporterSchema**](LtiReporterSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 

### Return type

[**LtiReporterIdSchema**](LtiReporterIdSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_destination_dispatch_registration_count**
> reset_destination_dispatch_registration_count(engine_tenant_name, destination_id)

Reset the registration count for related dispatches.

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
destination_id = 'destination_id_example' # str | 

try:
    # Reset the registration count for related dispatches.
    api_instance.reset_destination_dispatch_registration_count(engine_tenant_name, destination_id)
except ApiException as e:
    print("Exception when calling DispatchApi->reset_destination_dispatch_registration_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **destination_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_dispatch_registration_count**
> reset_dispatch_registration_count(engine_tenant_name, dispatch_id)

Reset the registration count for this dispatch.

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
dispatch_id = 'dispatch_id_example' # str | 

try:
    # Reset the registration count for this dispatch.
    api_instance.reset_dispatch_registration_count(engine_tenant_name, dispatch_id)
except ApiException as e:
    print("Exception when calling DispatchApi->reset_dispatch_registration_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **dispatch_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_destination**
> set_destination(body, engine_tenant_name, destination_id)

Create or update the destination with id `destinationId`

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
body = swagger_client.DestinationSchema() # DestinationSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
destination_id = 'destination_id_example' # str | 

try:
    # Create or update the destination with id `destinationId`
    api_instance.set_destination(body, engine_tenant_name, destination_id)
except ApiException as e:
    print("Exception when calling DispatchApi->set_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DestinationSchema**](DestinationSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **destination_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_destination_dispatch_enabled**
> set_destination_dispatch_enabled(body, engine_tenant_name, destination_id)

Enable or disable all related dispatches

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EnabledSchema() # EnabledSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
destination_id = 'destination_id_example' # str | 

try:
    # Enable or disable all related dispatches
    api_instance.set_destination_dispatch_enabled(body, engine_tenant_name, destination_id)
except ApiException as e:
    print("Exception when calling DispatchApi->set_destination_dispatch_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnabledSchema**](EnabledSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **destination_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_dispatch_enabled**
> set_dispatch_enabled(body, engine_tenant_name, dispatch_id)

Enable or disable the dispatch

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
body = swagger_client.EnabledSchema() # EnabledSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
dispatch_id = 'dispatch_id_example' # str | 

try:
    # Enable or disable the dispatch
    api_instance.set_dispatch_enabled(body, engine_tenant_name, dispatch_id)
except ApiException as e:
    print("Exception when calling DispatchApi->set_dispatch_enabled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnabledSchema**](EnabledSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **dispatch_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dispatch**
> update_dispatch(body, engine_tenant_name, dispatch_id)

Update the dispatch with id `dispatchId`

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
api_instance = swagger_client.DispatchApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateDispatchSchema() # UpdateDispatchSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
dispatch_id = 'dispatch_id_example' # str | 

try:
    # Update the dispatch with id `dispatchId`
    api_instance.update_dispatch(body, engine_tenant_name, dispatch_id)
except ApiException as e:
    print("Exception when calling DispatchApi->update_dispatch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDispatchSchema**](UpdateDispatchSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **dispatch_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

