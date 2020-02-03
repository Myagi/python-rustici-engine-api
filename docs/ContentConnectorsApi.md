# swagger_client.ContentConnectorsApi

All URIs are relative to */api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connector**](ContentConnectorsApi.md#create_connector) | **POST** /contentConnectors | Create a connector
[**get_connector_content_list**](ContentConnectorsApi.md#get_connector_content_list) | **GET** /contentConnectors/availableContent | Get list of available content
[**get_connectors_list**](ContentConnectorsApi.md#get_connectors_list) | **GET** /contentConnectors | Get content connectors
[**get_refresh_job_status**](ContentConnectorsApi.md#get_refresh_job_status) | **GET** /contentConnectors/availableContent/refreshJobs/{refreshJobId} | Check the status of a refresh job.
[**refresh_connector_content_list_job**](ContentConnectorsApi.md#refresh_connector_content_list_job) | **POST** /contentConnectors/availableContent/refreshJobs | Start a job to refresh the list of available content
[**search_remote_connector_content**](ContentConnectorsApi.md#search_remote_connector_content) | **POST** /contentConnectors/remoteSearch | search remote content
[**update_connector**](ContentConnectorsApi.md#update_connector) | **PUT** /contentConnectors/{connectorId} | Update a connector

# **create_connector**
> StringResultSchema create_connector(body, engine_tenant_name=engine_tenant_name)

Create a connector

Creates a connector for the specified tenant, or a system-wide connector if tenant is not specified.

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
api_instance = swagger_client.ContentConnectorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateConnectorSchema() # CreateConnectorSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)

try:
    # Create a connector
    api_response = api_instance.create_connector(body, engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentConnectorsApi->create_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateConnectorSchema**](CreateConnectorSchema.md)|  | 
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connector_content_list**
> ConnectorContentListSchema get_connector_content_list(engine_tenant_name=engine_tenant_name, connector_id=connector_id, since=since, more=more, not_imported=not_imported, search=search, include_all_metadata=include_all_metadata)

Get list of available content

Gets the list of content available, either for all connectors, or for only a specific connector if specified. If tenant is specified, this is the list of content for that tenant, if not, it is only content available through connectors configured for the whole system (not connectors configured for other tenants) 

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
api_instance = swagger_client.ContentConnectorsApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)
connector_id = 'connector_id_example' # str | the connector id (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)
not_imported = true # bool |  (optional)
search = 'search_example' # str |  (optional)
include_all_metadata = true # bool |  (optional)

try:
    # Get list of available content
    api_response = api_instance.get_connector_content_list(engine_tenant_name=engine_tenant_name, connector_id=connector_id, since=since, more=more, not_imported=not_imported, search=search, include_all_metadata=include_all_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentConnectorsApi->get_connector_content_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 
 **connector_id** | **str**| the connector id | [optional] 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **more** | **str**| Value for this parameter will be provided in the &#x27;more&#x27; property of lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 
 **not_imported** | **bool**|  | [optional] 
 **search** | **str**|  | [optional] 
 **include_all_metadata** | **bool**|  | [optional] 

### Return type

[**ConnectorContentListSchema**](ConnectorContentListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectors_list**
> ConnectorListSchema get_connectors_list(engine_tenant_name=engine_tenant_name)

Get content connectors

Gets list of connectors, for the specified tenant, or connectors that apply to all tenants if tenant is not specified.

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
api_instance = swagger_client.ContentConnectorsApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)

try:
    # Get content connectors
    api_response = api_instance.get_connectors_list(engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentConnectorsApi->get_connectors_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 

### Return type

[**ConnectorListSchema**](ConnectorListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refresh_job_status**
> RefreshConnectorResultListSchema get_refresh_job_status(refresh_job_id, engine_tenant_name=engine_tenant_name)

Check the status of a refresh job.

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
api_instance = swagger_client.ContentConnectorsApi(swagger_client.ApiClient(configuration))
refresh_job_id = 'refresh_job_id_example' # str | The Id received when the refresh job was submitted to the refreshJobs resource.
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)

try:
    # Check the status of a refresh job.
    api_response = api_instance.get_refresh_job_status(refresh_job_id, engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentConnectorsApi->get_refresh_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_job_id** | **str**| The Id received when the refresh job was submitted to the refreshJobs resource. | 
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 

### Return type

[**RefreshConnectorResultListSchema**](RefreshConnectorResultListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_connector_content_list_job**
> StringResultSchema refresh_connector_content_list_job(engine_tenant_name=engine_tenant_name, connector_id=connector_id)

Start a job to refresh the list of available content

Starts a job to refresh the list of content available, either for all connectors, or for only a specific connector if specified. If a tenant is specified, then this is this list of content for that tenant. If a tenant is not specified, then the list will only contain content available through connectors configured for the whole system (not connectors configured for other tenants) 

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
api_instance = swagger_client.ContentConnectorsApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)
connector_id = 'connector_id_example' # str | the connector id (optional)

try:
    # Start a job to refresh the list of available content
    api_response = api_instance.refresh_connector_content_list_job(engine_tenant_name=engine_tenant_name, connector_id=connector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentConnectorsApi->refresh_connector_content_list_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 
 **connector_id** | **str**| the connector id | [optional] 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_remote_connector_content**
> ConnectorContentListSchema search_remote_connector_content(body, engine_tenant_name=engine_tenant_name)

search remote content

Searches the remote content available, either for all connectors, or for only a specific connector if specified. If tenant is specified, this is the list of content for that tenant, if not, it is only content available through connectors configured for the whole system (not connectors configured for other tenants) 

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
api_instance = swagger_client.ContentConnectorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConnectorContentSearchSchema() # ConnectorContentSearchSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)

try:
    # search remote content
    api_response = api_instance.search_remote_connector_content(body, engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentConnectorsApi->search_remote_connector_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectorContentSearchSchema**](ConnectorContentSearchSchema.md)|  | 
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 

### Return type

[**ConnectorContentListSchema**](ConnectorContentListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connector**
> update_connector(body, connector_id, engine_tenant_name=engine_tenant_name)

Update a connector

Update the specified connector.

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
api_instance = swagger_client.ContentConnectorsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateConnectorSchema() # UpdateConnectorSchema | 
connector_id = 'connector_id_example' # str | the connector id
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)

try:
    # Update a connector
    api_instance.update_connector(body, connector_id, engine_tenant_name=engine_tenant_name)
except ApiException as e:
    print("Exception when calling ContentConnectorsApi->update_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateConnectorSchema**](UpdateConnectorSchema.md)|  | 
 **connector_id** | **str**| the connector id | 
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

