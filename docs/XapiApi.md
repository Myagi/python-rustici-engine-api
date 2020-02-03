# swagger_client.XapiApi

All URIs are relative to */api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_statement_pipe**](XapiApi.md#create_statement_pipe) | **POST** /xapi/statementPipes | Create an xAPI statement pipe.
[**create_xapi_credential**](XapiApi.md#create_xapi_credential) | **POST** /xapi/credentials | Create an xAPI credential
[**delete_statement_pipe**](XapiApi.md#delete_statement_pipe) | **DELETE** /xapi/statementPipes/{statementPipeId} | Deletes the xAPI statement pipe specified with the id &#x60;statementPipeId&#x60;
[**delete_xapi_credential**](XapiApi.md#delete_xapi_credential) | **DELETE** /xapi/credentials/{xapiCredentialId} | Deletes the xAPI credential specified with the id &#x60;xapiCredentialId&#x60;
[**get_statement_pipe**](XapiApi.md#get_statement_pipe) | **GET** /xapi/statementPipes/{statementPipeId} | Retrieves xAPI statement pipe specified by id &#x60;statementPipeId.&#x60;
[**get_statement_pipes**](XapiApi.md#get_statement_pipes) | **GET** /xapi/statementPipes | Get a list of all xAPI statement pipes
[**get_xapi_credential**](XapiApi.md#get_xapi_credential) | **GET** /xapi/credentials/{xapiCredentialId} | Retrieves the xAPI credential specified by id &#x60;xapiCredentialId&#x60;
[**get_xapi_credentials**](XapiApi.md#get_xapi_credentials) | **GET** /xapi/credentials | Get a list of all xAPI credentials
[**set_statement_pipe**](XapiApi.md#set_statement_pipe) | **PUT** /xapi/statementPipes/{statementPipeId} | Either edits an existing xAPI statement pipe or creates a new one, specified by id &#x60;statementPipeId&#x60;
[**set_xapi_credential**](XapiApi.md#set_xapi_credential) | **PUT** /xapi/credentials/{xapiCredentialId} | Either edits an existing xAPI credential or creates a new one, specified by id &#x60;xapiCredentialId&#x60;

# **create_statement_pipe**
> StringResultSchema create_statement_pipe(body, engine_tenant_name)

Create an xAPI statement pipe.

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
api_instance = swagger_client.XapiApi(swagger_client.ApiClient(configuration))
body = swagger_client.XapiStatementPipePostSchema() # XapiStatementPipePostSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request

try:
    # Create an xAPI statement pipe.
    api_response = api_instance.create_statement_pipe(body, engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XapiApi->create_statement_pipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**XapiStatementPipePostSchema**](XapiStatementPipePostSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_xapi_credential**
> StringResultSchema create_xapi_credential(body, engine_tenant_name)

Create an xAPI credential

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
api_instance = swagger_client.XapiApi(swagger_client.ApiClient(configuration))
body = swagger_client.XapiCredentialPostSchema() # XapiCredentialPostSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request

try:
    # Create an xAPI credential
    api_response = api_instance.create_xapi_credential(body, engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XapiApi->create_xapi_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**XapiCredentialPostSchema**](XapiCredentialPostSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_statement_pipe**
> delete_statement_pipe(engine_tenant_name, statement_pipe_id)

Deletes the xAPI statement pipe specified with the id `statementPipeId`

Caution: avoid re-creating a statement pipe with the same ID quickly after a delete. The old version could still be processing, in which case the new pipe could be updated improperly by the processor.

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
api_instance = swagger_client.XapiApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
statement_pipe_id = 'statement_pipe_id_example' # str | id for this xAPI statement pipe

try:
    # Deletes the xAPI statement pipe specified with the id `statementPipeId`
    api_instance.delete_statement_pipe(engine_tenant_name, statement_pipe_id)
except ApiException as e:
    print("Exception when calling XapiApi->delete_statement_pipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **statement_pipe_id** | **str**| id for this xAPI statement pipe | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_xapi_credential**
> delete_xapi_credential(engine_tenant_name, xapi_credential_id)

Deletes the xAPI credential specified with the id `xapiCredentialId`

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
api_instance = swagger_client.XapiApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
xapi_credential_id = 'xapi_credential_id_example' # str | id for this xAPI credential

try:
    # Deletes the xAPI credential specified with the id `xapiCredentialId`
    api_instance.delete_xapi_credential(engine_tenant_name, xapi_credential_id)
except ApiException as e:
    print("Exception when calling XapiApi->delete_xapi_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **xapi_credential_id** | **str**| id for this xAPI credential | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_pipe**
> XapiStatementPipeSchema get_statement_pipe(engine_tenant_name, statement_pipe_id)

Retrieves xAPI statement pipe specified by id `statementPipeId.`

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
api_instance = swagger_client.XapiApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
statement_pipe_id = 'statement_pipe_id_example' # str | id for this xAPI statement pipe

try:
    # Retrieves xAPI statement pipe specified by id `statementPipeId.`
    api_response = api_instance.get_statement_pipe(engine_tenant_name, statement_pipe_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XapiApi->get_statement_pipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **statement_pipe_id** | **str**| id for this xAPI statement pipe | 

### Return type

[**XapiStatementPipeSchema**](XapiStatementPipeSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_pipes**
> XapiStatementPipeListSchema get_statement_pipes(engine_tenant_name)

Get a list of all xAPI statement pipes

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
api_instance = swagger_client.XapiApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request

try:
    # Get a list of all xAPI statement pipes
    api_response = api_instance.get_statement_pipes(engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XapiApi->get_statement_pipes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 

### Return type

[**XapiStatementPipeListSchema**](XapiStatementPipeListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xapi_credential**
> XapiCredentialSchema get_xapi_credential(engine_tenant_name, xapi_credential_id)

Retrieves the xAPI credential specified by id `xapiCredentialId`

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
api_instance = swagger_client.XapiApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
xapi_credential_id = 'xapi_credential_id_example' # str | id for this xAPI credential

try:
    # Retrieves the xAPI credential specified by id `xapiCredentialId`
    api_response = api_instance.get_xapi_credential(engine_tenant_name, xapi_credential_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XapiApi->get_xapi_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **xapi_credential_id** | **str**| id for this xAPI credential | 

### Return type

[**XapiCredentialSchema**](XapiCredentialSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_xapi_credentials**
> XapiCredentialsListSchema get_xapi_credentials(engine_tenant_name, more=more)

Get a list of all xAPI credentials

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
api_instance = swagger_client.XapiApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)

try:
    # Get a list of all xAPI credentials
    api_response = api_instance.get_xapi_credentials(engine_tenant_name, more=more)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling XapiApi->get_xapi_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **more** | **str**| Value for this parameter will be provided in the &#x27;more&#x27; property of lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 

### Return type

[**XapiCredentialsListSchema**](XapiCredentialsListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_statement_pipe**
> set_statement_pipe(body, engine_tenant_name, statement_pipe_id)

Either edits an existing xAPI statement pipe or creates a new one, specified by id `statementPipeId`

Editing a statement pipe will cause it to start over and forward any statements it finds, even if the prior version of the pipe had already forwarded those statements. If the statement pipe being edited is currently being processed, the this request will fail with a status code of 409.

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
api_instance = swagger_client.XapiApi(swagger_client.ApiClient(configuration))
body = swagger_client.XapiStatementPipePutSchema() # XapiStatementPipePutSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
statement_pipe_id = 'statement_pipe_id_example' # str | id for this xAPI statement pipe

try:
    # Either edits an existing xAPI statement pipe or creates a new one, specified by id `statementPipeId`
    api_instance.set_statement_pipe(body, engine_tenant_name, statement_pipe_id)
except ApiException as e:
    print("Exception when calling XapiApi->set_statement_pipe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**XapiStatementPipePutSchema**](XapiStatementPipePutSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **statement_pipe_id** | **str**| id for this xAPI statement pipe | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_xapi_credential**
> set_xapi_credential(body, engine_tenant_name, xapi_credential_id)

Either edits an existing xAPI credential or creates a new one, specified by id `xapiCredentialId`

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
api_instance = swagger_client.XapiApi(swagger_client.ApiClient(configuration))
body = swagger_client.XapiCredentialPutSchema() # XapiCredentialPutSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
xapi_credential_id = 'xapi_credential_id_example' # str | id for this xAPI credential

try:
    # Either edits an existing xAPI credential or creates a new one, specified by id `xapiCredentialId`
    api_instance.set_xapi_credential(body, engine_tenant_name, xapi_credential_id)
except ApiException as e:
    print("Exception when calling XapiApi->set_xapi_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**XapiCredentialPutSchema**](XapiCredentialPutSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **xapi_credential_id** | **str**| id for this xAPI credential | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

