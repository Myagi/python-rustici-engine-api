# rustici_engine.RegistrationApi

All URIs are relative to */api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_registration_launch_link**](RegistrationApi.md#build_registration_launch_link) | **POST** /registrations/{registrationId}/launchLink | Returns the link to use to launch this registration
[**create_new_registration_instance**](RegistrationApi.md#create_new_registration_instance) | **POST** /registrations/{registrationId}/instances | Create a new instance for this registration specified by the registration ID
[**create_registration**](RegistrationApi.md#create_registration) | **POST** /registrations | Create a registration.
[**delete_registration**](RegistrationApi.md#delete_registration) | **DELETE** /registrations/{registrationId} | Delete &#x60;registrationId&#x60;
[**delete_registration_configuration_setting**](RegistrationApi.md#delete_registration_configuration_setting) | **DELETE** /registrations/{registrationId}/configuration/{settingId} | Clears the &#x60;settingId&#x60; value for this registration
[**delete_registration_global_data**](RegistrationApi.md#delete_registration_global_data) | **DELETE** /registrations/{registrationId}/globalData | delete global data associated with &#x60;registrationId&#x60;
[**delete_registration_instance**](RegistrationApi.md#delete_registration_instance) | **DELETE** /registrations/{registrationId}/instances/{instanceId} | Delete instance &#x60;instanceId&#x60; of &#x60;registrationId&#x60;
[**delete_registration_instance_configuration_setting**](RegistrationApi.md#delete_registration_instance_configuration_setting) | **DELETE** /registrations/{registrationId}/instances/{instanceId}/configuration/{settingId} | Clears the &#x60;settingId&#x60; value for this registration instance
[**delete_registration_progress**](RegistrationApi.md#delete_registration_progress) | **DELETE** /registrations/{registrationId}/progress | delete registration progress (clear registration)
[**get_registration**](RegistrationApi.md#get_registration) | **HEAD** /registrations/{registrationId} | Does this registration exist?
[**get_registration_configuration**](RegistrationApi.md#get_registration_configuration) | **GET** /registrations/{registrationId}/configuration | Returns all configuration settings for this registration
[**get_registration_instance_configuration**](RegistrationApi.md#get_registration_instance_configuration) | **GET** /registrations/{registrationId}/instances/{instanceId}/configuration | Returns all configuration settings for this registration instance
[**get_registration_instance_launch_history**](RegistrationApi.md#get_registration_instance_launch_history) | **GET** /registrations/{registrationId}/instances/{instanceId}/launchHistory | Returns history of this registration&#x27;s launches
[**get_registration_instance_progress**](RegistrationApi.md#get_registration_instance_progress) | **GET** /registrations/{registrationId}/instances/{instanceId} | Get registration progress for instance &#x60;instanceId&#x60; of &#x60;registrationId&#x60;
[**get_registration_instance_statements**](RegistrationApi.md#get_registration_instance_statements) | **GET** /registrations/{registrationId}/instances/{instanceId}/xAPIStatements | Get xAPI statements for instance &#x60;instanceId&#x60; of &#x60;registrationId&#x60;
[**get_registration_instances**](RegistrationApi.md#get_registration_instances) | **GET** /registrations/{registrationId}/instances | Get all the instances of this the registration specified by the registration ID
[**get_registration_launch_history**](RegistrationApi.md#get_registration_launch_history) | **GET** /registrations/{registrationId}/launchHistory | Returns history of this registration&#x27;s launches
[**get_registration_progress**](RegistrationApi.md#get_registration_progress) | **GET** /registrations/{registrationId} | Get registration progress for &#x60;registrationId&#x60;
[**get_registration_statements**](RegistrationApi.md#get_registration_statements) | **GET** /registrations/{registrationId}/xAPIStatements | Get xAPI statements for &#x60;registrationId&#x60;
[**get_registrations**](RegistrationApi.md#get_registrations) | **GET** /registrations | Gets a list of registrations including a summary of the status of each registration.
[**set_registration_configuration**](RegistrationApi.md#set_registration_configuration) | **POST** /registrations/{registrationId}/configuration | Set configuration settings for this registration.
[**set_registration_instance_configuration**](RegistrationApi.md#set_registration_instance_configuration) | **POST** /registrations/{registrationId}/instances/{instanceId}/configuration | Set configuration settings for this registration instance.

# **build_registration_launch_link**
> LaunchLinkSchema build_registration_launch_link(body, engine_tenant_name, registration_id)

Returns the link to use to launch this registration

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.LaunchLinkRequestSchema() # LaunchLinkRequestSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration

try:
    # Returns the link to use to launch this registration
    api_response = api_instance.build_registration_launch_link(body, engine_tenant_name, registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->build_registration_launch_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LaunchLinkRequestSchema**](LaunchLinkRequestSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 

### Return type

[**LaunchLinkSchema**](LaunchLinkSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_new_registration_instance**
> create_new_registration_instance(engine_tenant_name, registration_id)

Create a new instance for this registration specified by the registration ID

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration

try:
    # Create a new instance for this registration specified by the registration ID
    api_instance.create_new_registration_instance(engine_tenant_name, registration_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->create_new_registration_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_registration**
> create_registration(body, engine_tenant_name, course_version=course_version)

Create a registration.

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.CreateRegistrationSchema() # CreateRegistrationSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_version = 56 # int | The version of the course you want to create the registration for. Unless you have a reason for using this you probably do not need to. (optional)

try:
    # Create a registration.
    api_instance.create_registration(body, engine_tenant_name, course_version=course_version)
except ApiException as e:
    print("Exception when calling RegistrationApi->create_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRegistrationSchema**](CreateRegistrationSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_version** | **int**| The version of the course you want to create the registration for. Unless you have a reason for using this you probably do not need to. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration**
> delete_registration(engine_tenant_name, registration_id)

Delete `registrationId`

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration

try:
    # Delete `registrationId`
    api_instance.delete_registration(engine_tenant_name, registration_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->delete_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration_configuration_setting**
> delete_registration_configuration_setting(engine_tenant_name, registration_id, setting_id)

Clears the `settingId` value for this registration

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
setting_id = 'setting_id_example' # str | 

try:
    # Clears the `settingId` value for this registration
    api_instance.delete_registration_configuration_setting(engine_tenant_name, registration_id, setting_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->delete_registration_configuration_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **setting_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration_global_data**
> delete_registration_global_data(engine_tenant_name, registration_id)

delete global data associated with `registrationId`

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration

try:
    # delete global data associated with `registrationId`
    api_instance.delete_registration_global_data(engine_tenant_name, registration_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->delete_registration_global_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration_instance**
> delete_registration_instance(engine_tenant_name, registration_id, instance_id)

Delete instance `instanceId` of `registrationId`

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | the instance of this registration

try:
    # Delete instance `instanceId` of `registrationId`
    api_instance.delete_registration_instance(engine_tenant_name, registration_id, instance_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->delete_registration_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| the instance of this registration | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration_instance_configuration_setting**
> delete_registration_instance_configuration_setting(engine_tenant_name, registration_id, instance_id, setting_id)

Clears the `settingId` value for this registration instance

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | the instance of this registration
setting_id = 'setting_id_example' # str | 

try:
    # Clears the `settingId` value for this registration instance
    api_instance.delete_registration_instance_configuration_setting(engine_tenant_name, registration_id, instance_id, setting_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->delete_registration_instance_configuration_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| the instance of this registration | 
 **setting_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration_progress**
> delete_registration_progress(engine_tenant_name, registration_id)

delete registration progress (clear registration)

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration

try:
    # delete registration progress (clear registration)
    api_instance.delete_registration_progress(engine_tenant_name, registration_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->delete_registration_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration**
> get_registration(engine_tenant_name, registration_id)

Does this registration exist?

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration

try:
    # Does this registration exist?
    api_instance.get_registration(engine_tenant_name, registration_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_configuration**
> SettingListSchema get_registration_configuration(engine_tenant_name, registration_id, include_metadata=include_metadata, include_hidden_settings=include_hidden_settings, include_secret_settings=include_secret_settings, process_replacement_tokens=process_replacement_tokens)

Returns all configuration settings for this registration

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
include_metadata = true # bool |  (optional)
include_hidden_settings = true # bool | Should settings that are declared to be hidden be included. Note: such settings generally do not need to be modified, and may be confusing.  (optional)
include_secret_settings = true # bool | Should settings that are stored encrypted (type 'secretString') be included. Note: if included, the decrypted value will be returned.  (optional)
process_replacement_tokens = true # bool | Whether to process replacement tokens (false returns the raw value of each setting, without tokens or environment variable replacements) (optional)

try:
    # Returns all configuration settings for this registration
    api_response = api_instance.get_registration_configuration(engine_tenant_name, registration_id, include_metadata=include_metadata, include_hidden_settings=include_hidden_settings, include_secret_settings=include_secret_settings, process_replacement_tokens=process_replacement_tokens)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **include_metadata** | **bool**|  | [optional] 
 **include_hidden_settings** | **bool**| Should settings that are declared to be hidden be included. Note: such settings generally do not need to be modified, and may be confusing.  | [optional] 
 **include_secret_settings** | **bool**| Should settings that are stored encrypted (type &#x27;secretString&#x27;) be included. Note: if included, the decrypted value will be returned.  | [optional] 
 **process_replacement_tokens** | **bool**| Whether to process replacement tokens (false returns the raw value of each setting, without tokens or environment variable replacements) | [optional] 

### Return type

[**SettingListSchema**](SettingListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_instance_configuration**
> SettingListSchema get_registration_instance_configuration(engine_tenant_name, registration_id, instance_id, include_metadata=include_metadata, include_hidden_settings=include_hidden_settings, include_secret_settings=include_secret_settings, process_replacement_tokens=process_replacement_tokens)

Returns all configuration settings for this registration instance

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | the instance of this registration
include_metadata = true # bool |  (optional)
include_hidden_settings = true # bool | Should settings that are declared to be hidden be included. Note: such settings generally do not need to be modified, and may be confusing.  (optional)
include_secret_settings = true # bool | Should settings that are stored encrypted (type 'secretString') be included. Note: if included, the decrypted value will be returned.  (optional)
process_replacement_tokens = true # bool | Whether to process replacement tokens (false returns the raw value of each setting, without tokens or environment variable replacements) (optional)

try:
    # Returns all configuration settings for this registration instance
    api_response = api_instance.get_registration_instance_configuration(engine_tenant_name, registration_id, instance_id, include_metadata=include_metadata, include_hidden_settings=include_hidden_settings, include_secret_settings=include_secret_settings, process_replacement_tokens=process_replacement_tokens)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration_instance_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| the instance of this registration | 
 **include_metadata** | **bool**|  | [optional] 
 **include_hidden_settings** | **bool**| Should settings that are declared to be hidden be included. Note: such settings generally do not need to be modified, and may be confusing.  | [optional] 
 **include_secret_settings** | **bool**| Should settings that are stored encrypted (type &#x27;secretString&#x27;) be included. Note: if included, the decrypted value will be returned.  | [optional] 
 **process_replacement_tokens** | **bool**| Whether to process replacement tokens (false returns the raw value of each setting, without tokens or environment variable replacements) | [optional] 

### Return type

[**SettingListSchema**](SettingListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_instance_launch_history**
> LaunchHistoryListSchema get_registration_instance_launch_history(engine_tenant_name, registration_id, instance_id, include_history_log=include_history_log)

Returns history of this registration's launches

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | the instance of this registration
include_history_log = true # bool | Whether to include the history log in the launch history (optional)

try:
    # Returns history of this registration's launches
    api_response = api_instance.get_registration_instance_launch_history(engine_tenant_name, registration_id, instance_id, include_history_log=include_history_log)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration_instance_launch_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| the instance of this registration | 
 **include_history_log** | **bool**| Whether to include the history log in the launch history | [optional] 

### Return type

[**LaunchHistoryListSchema**](LaunchHistoryListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_instance_progress**
> RegistrationSchema get_registration_instance_progress(engine_tenant_name, registration_id, instance_id, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime, create_xapi_registration_id_if_absent=create_xapi_registration_id_if_absent)

Get registration progress for instance `instanceId` of `registrationId`

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | the instance of this registration
include_child_results = true # bool | Include information about each learning object, not just the top level in the results (optional)
include_interactions_and_objectives = true # bool | Include interactions and objectives in the results (optional)
include_runtime = true # bool | Include runtime details in the results (optional)
create_xapi_registration_id_if_absent = true # bool | create the xAPI registration ID for this registration if one does not already exist (optional)

try:
    # Get registration progress for instance `instanceId` of `registrationId`
    api_response = api_instance.get_registration_instance_progress(engine_tenant_name, registration_id, instance_id, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime, create_xapi_registration_id_if_absent=create_xapi_registration_id_if_absent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration_instance_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| the instance of this registration | 
 **include_child_results** | **bool**| Include information about each learning object, not just the top level in the results | [optional] 
 **include_interactions_and_objectives** | **bool**| Include interactions and objectives in the results | [optional] 
 **include_runtime** | **bool**| Include runtime details in the results | [optional] 
 **create_xapi_registration_id_if_absent** | **bool**| create the xAPI registration ID for this registration if one does not already exist | [optional] 

### Return type

[**RegistrationSchema**](RegistrationSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_instance_statements**
> XapiStatementResult get_registration_instance_statements(engine_tenant_name, registration_id, instance_id, since=since, until=until, more=more)

Get xAPI statements for instance `instanceId` of `registrationId`

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | the instance of this registration
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)

try:
    # Get xAPI statements for instance `instanceId` of `registrationId`
    api_response = api_instance.get_registration_instance_statements(engine_tenant_name, registration_id, instance_id, since=since, until=until, more=more)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration_instance_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| the instance of this registration | 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **more** | **str**| Value for this parameter will be provided in the &#x27;more&#x27; property of lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 

### Return type

[**XapiStatementResult**](XapiStatementResult.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_instances**
> RegistrationListSchema get_registration_instances(engine_tenant_name, registration_id, since=since, until=until, more=more, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)

Get all the instances of this the registration specified by the registration ID

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)
include_child_results = true # bool | Include information about each learning object, not just the top level in the results (optional)
include_interactions_and_objectives = true # bool | Include interactions and objectives in the results (optional)
include_runtime = true # bool | Include runtime details in the results (optional)

try:
    # Get all the instances of this the registration specified by the registration ID
    api_response = api_instance.get_registration_instances(engine_tenant_name, registration_id, since=since, until=until, more=more, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **more** | **str**| Value for this parameter will be provided in the &#x27;more&#x27; property of lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 
 **include_child_results** | **bool**| Include information about each learning object, not just the top level in the results | [optional] 
 **include_interactions_and_objectives** | **bool**| Include interactions and objectives in the results | [optional] 
 **include_runtime** | **bool**| Include runtime details in the results | [optional] 

### Return type

[**RegistrationListSchema**](RegistrationListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_launch_history**
> LaunchHistoryListSchema get_registration_launch_history(engine_tenant_name, registration_id, include_history_log=include_history_log)

Returns history of this registration's launches

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
include_history_log = true # bool | Whether to include the history log in the launch history (optional)

try:
    # Returns history of this registration's launches
    api_response = api_instance.get_registration_launch_history(engine_tenant_name, registration_id, include_history_log=include_history_log)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration_launch_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **include_history_log** | **bool**| Whether to include the history log in the launch history | [optional] 

### Return type

[**LaunchHistoryListSchema**](LaunchHistoryListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_progress**
> RegistrationSchema get_registration_progress(engine_tenant_name, registration_id, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime, create_xapi_registration_id_if_absent=create_xapi_registration_id_if_absent)

Get registration progress for `registrationId`

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
include_child_results = true # bool | Include information about each learning object, not just the top level in the results (optional)
include_interactions_and_objectives = true # bool | Include interactions and objectives in the results (optional)
include_runtime = true # bool | Include runtime details in the results (optional)
create_xapi_registration_id_if_absent = true # bool | create the xAPI registration ID for this registration if one does not already exist (optional)

try:
    # Get registration progress for `registrationId`
    api_response = api_instance.get_registration_progress(engine_tenant_name, registration_id, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime, create_xapi_registration_id_if_absent=create_xapi_registration_id_if_absent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **include_child_results** | **bool**| Include information about each learning object, not just the top level in the results | [optional] 
 **include_interactions_and_objectives** | **bool**| Include interactions and objectives in the results | [optional] 
 **include_runtime** | **bool**| Include runtime details in the results | [optional] 
 **create_xapi_registration_id_if_absent** | **bool**| create the xAPI registration ID for this registration if one does not already exist | [optional] 

### Return type

[**RegistrationSchema**](RegistrationSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_statements**
> XapiStatementResult get_registration_statements(engine_tenant_name, registration_id, since=since, until=until, more=more)

Get xAPI statements for `registrationId`

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)

try:
    # Get xAPI statements for `registrationId`
    api_response = api_instance.get_registration_statements(engine_tenant_name, registration_id, since=since, until=until, more=more)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registration_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **more** | **str**| Value for this parameter will be provided in the &#x27;more&#x27; property of lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 

### Return type

[**XapiStatementResult**](XapiStatementResult.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registrations**
> RegistrationListSchema get_registrations(engine_tenant_name, course_id=course_id, learner_id=learner_id, since=since, until=until, more=more, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)

Gets a list of registrations including a summary of the status of each registration.

The 'since' parameter exists to allow retrieving only registrations that have changed.

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | Only registrations for the specified course id will be included. (optional)
learner_id = 'learner_id_example' # str | Only entries for the specified learner id will be included. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)
include_child_results = true # bool | Include information about each learning object, not just the top level in the results (optional)
include_interactions_and_objectives = true # bool | Include interactions and objectives in the results (optional)
include_runtime = true # bool | Include runtime details in the results (optional)

try:
    # Gets a list of registrations including a summary of the status of each registration.
    api_response = api_instance.get_registrations(engine_tenant_name, course_id=course_id, learner_id=learner_id, since=since, until=until, more=more, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationApi->get_registrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**| Only registrations for the specified course id will be included. | [optional] 
 **learner_id** | **str**| Only entries for the specified learner id will be included. | [optional] 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **more** | **str**| Value for this parameter will be provided in the &#x27;more&#x27; property of lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 
 **include_child_results** | **bool**| Include information about each learning object, not just the top level in the results | [optional] 
 **include_interactions_and_objectives** | **bool**| Include interactions and objectives in the results | [optional] 
 **include_runtime** | **bool**| Include runtime details in the results | [optional] 

### Return type

[**RegistrationListSchema**](RegistrationListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_registration_configuration**
> set_registration_configuration(body, engine_tenant_name, registration_id)

Set configuration settings for this registration.

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.SettingsPostSchema() # SettingsPostSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration

try:
    # Set configuration settings for this registration.
    api_instance.set_registration_configuration(body, engine_tenant_name, registration_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->set_registration_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsPostSchema**](SettingsPostSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_registration_instance_configuration**
> set_registration_instance_configuration(body, engine_tenant_name, registration_id, instance_id)

Set configuration settings for this registration instance.

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
api_instance = rustici_engine.RegistrationApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.SettingsPostSchema() # SettingsPostSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | the instance of this registration

try:
    # Set configuration settings for this registration instance.
    api_instance.set_registration_instance_configuration(body, engine_tenant_name, registration_id, instance_id)
except ApiException as e:
    print("Exception when calling RegistrationApi->set_registration_instance_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsPostSchema**](SettingsPostSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| the instance of this registration | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

