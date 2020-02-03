# swagger_client.AppManagementApi

All URIs are relative to */api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credential**](AppManagementApi.md#create_credential) | **POST** /appManagement/credentials | Create credential
[**create_or_update_tenant**](AppManagementApi.md#create_or_update_tenant) | **PUT** /appManagement/tenants/{tenantName} | Create or update tenant
[**create_token**](AppManagementApi.md#create_token) | **POST** /appManagement/token | Create token
[**delete_application_configuration_setting**](AppManagementApi.md#delete_application_configuration_setting) | **DELETE** /appManagement/configuration/{settingId} | Clears the &#x60;settingId&#x60; value for this level
[**delete_credential**](AppManagementApi.md#delete_credential) | **DELETE** /appManagement/credentials/{credentialId} | Removes &#x60;credentialId&#x60; credentials
[**delete_tenant**](AppManagementApi.md#delete_tenant) | **DELETE** /appManagement/tenants/{tenantName} | Delete a tenant. Warning: If tenant data is not deleted first, this will leave orphaned rows that can only be deleted manually. Does not remove any data, but does remove mapping between name and key used to store data. Consider deactivating instead.
[**delete_tenant_data**](AppManagementApi.md#delete_tenant_data) | **DELETE** /appManagement/tenants/{tenantName}/data | Delete all of a tenant&#x27;s data.
[**get_application_configuration**](AppManagementApi.md#get_application_configuration) | **GET** /appManagement/configuration | Returns all configuration settings for this level
[**get_authenticated_credential**](AppManagementApi.md#get_authenticated_credential) | **GET** /appManagement/authenticatedCredential | Get information about the credential used to authenticate this request.
[**get_credential**](AppManagementApi.md#get_credential) | **GET** /appManagement/credentials/{credentialId} | Get information on &#x60;credentialId&#x60; credential
[**get_credentials**](AppManagementApi.md#get_credentials) | **GET** /appManagement/credentials | List of credentials
[**get_pii_deletion_job**](AppManagementApi.md#get_pii_deletion_job) | **GET** /appManagement/PII/deletionJob/{jobId} | Check the status of a PII deletion job with the provided job id.
[**get_tenant_list**](AppManagementApi.md#get_tenant_list) | **GET** /appManagement/tenants | Get list of all tenants
[**inspect_token**](AppManagementApi.md#inspect_token) | **GET** /appManagement/token | Inspect token
[**post_pii_deletion_job**](AppManagementApi.md#post_pii_deletion_job) | **POST** /appManagement/PII/deletionJob | Initiate a job to delete a user&#x27;s Personal Identifying Information from the system.
[**post_update_encrypted_setting**](AppManagementApi.md#post_update_encrypted_setting) | **POST** /appManagement/configuration/updateEncryptedSettings | Re-write settings, and statement pipe passwords using the current encryption settings. For password rotation.
[**reset_credential_secret**](AppManagementApi.md#reset_credential_secret) | **POST** /appManagement/credentials/{credentialId}/resetSecret | Reset credential secret
[**set_application_configuration**](AppManagementApi.md#set_application_configuration) | **POST** /appManagement/configuration | Set configuration settings for this level.
[**update_credential**](AppManagementApi.md#update_credential) | **PUT** /appManagement/credentials/{credentialId} | Update &#x60;credentialId&#x60; credentials

# **create_credential**
> CredentialCreatedSchema create_credential(body, engine_tenant_name=engine_tenant_name)

Create credential

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.CredentialRequestSchema() # CredentialRequestSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains 'tenantName' which should be used for any permissions that need to be scoped to a particular tenant.  (optional)

try:
    # Create credential
    api_response = api_instance.create_credential(body, engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->create_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CredentialRequestSchema**](CredentialRequestSchema.md)|  | 
 **engine_tenant_name** | **str**| If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains &#x27;tenantName&#x27; which should be used for any permissions that need to be scoped to a particular tenant.  | [optional] 

### Return type

[**CredentialCreatedSchema**](CredentialCreatedSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_or_update_tenant**
> create_or_update_tenant(body, tenant_name)

Create or update tenant

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
body = NULL # object | 
tenant_name = 'tenant_name_example' # str | 

try:
    # Create or update tenant
    api_instance.create_or_update_tenant(body, tenant_name)
except ApiException as e:
    print("Exception when calling AppManagementApi->create_or_update_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **tenant_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token**
> StringResultSchema create_token(body, engine_tenant_name=engine_tenant_name)

Create token

Creates, signs and returns a token based on the provided permissions, if the credentials used to request the token have the permissions being requested. Note: the token is not stored and therefore can not be modified or deleted. The requested permissions are encoded in the token which is then signed. As long as the secret used to create it is not changed the token will be valid until it expires. 

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.TokenRequestSchema() # TokenRequestSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains 'tenantName' which should be used for any permissions that need to be scoped to a particular tenant.  (optional)

try:
    # Create token
    api_response = api_instance.create_token(body, engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenRequestSchema**](TokenRequestSchema.md)|  | 
 **engine_tenant_name** | **str**| If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains &#x27;tenantName&#x27; which should be used for any permissions that need to be scoped to a particular tenant.  | [optional] 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_configuration_setting**
> delete_application_configuration_setting(setting_id, engine_tenant_name=engine_tenant_name, learning_standard=learning_standard, single_sco=single_sco)

Clears the `settingId` value for this level

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
setting_id = 'setting_id_example' # str | 
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)
learning_standard = 'learning_standard_example' # str | Required if singleSco is specified. Scopes the request to the provided learning standard. (optional)
single_sco = true # bool | Required if learningStandard is specified. Scopes settings to whether a package has only one SCO or assignable unit within it or not. To apply a configuration setting to a learning standard for single and multi-SCO content, it must be set for both scopes.  (optional)

try:
    # Clears the `settingId` value for this level
    api_instance.delete_application_configuration_setting(setting_id, engine_tenant_name=engine_tenant_name, learning_standard=learning_standard, single_sco=single_sco)
except ApiException as e:
    print("Exception when calling AppManagementApi->delete_application_configuration_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_id** | **str**|  | 
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 
 **learning_standard** | **str**| Required if singleSco is specified. Scopes the request to the provided learning standard. | [optional] 
 **single_sco** | **bool**| Required if learningStandard is specified. Scopes settings to whether a package has only one SCO or assignable unit within it or not. To apply a configuration setting to a learning standard for single and multi-SCO content, it must be set for both scopes.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credential**
> delete_credential(credential_id, engine_tenant_name=engine_tenant_name)

Removes `credentialId` credentials

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
credential_id = 'credential_id_example' # str | 
engine_tenant_name = 'engine_tenant_name_example' # str | If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains 'tenantName' which should be used for any permissions that need to be scoped to a particular tenant.  (optional)

try:
    # Removes `credentialId` credentials
    api_instance.delete_credential(credential_id, engine_tenant_name=engine_tenant_name)
except ApiException as e:
    print("Exception when calling AppManagementApi->delete_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 
 **engine_tenant_name** | **str**| If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains &#x27;tenantName&#x27; which should be used for any permissions that need to be scoped to a particular tenant.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant**
> delete_tenant(tenant_name)

Delete a tenant. Warning: If tenant data is not deleted first, this will leave orphaned rows that can only be deleted manually. Does not remove any data, but does remove mapping between name and key used to store data. Consider deactivating instead.

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | 

try:
    # Delete a tenant. Warning: If tenant data is not deleted first, this will leave orphaned rows that can only be deleted manually. Does not remove any data, but does remove mapping between name and key used to store data. Consider deactivating instead.
    api_instance.delete_tenant(tenant_name)
except ApiException as e:
    print("Exception when calling AppManagementApi->delete_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant_data**
> delete_tenant_data(tenant_name)

Delete all of a tenant's data.

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | 

try:
    # Delete all of a tenant's data.
    api_instance.delete_tenant_data(tenant_name)
except ApiException as e:
    print("Exception when calling AppManagementApi->delete_tenant_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_configuration**
> SettingListSchema get_application_configuration(engine_tenant_name=engine_tenant_name, learning_standard=learning_standard, single_sco=single_sco, include_metadata=include_metadata, include_hidden_settings=include_hidden_settings, include_secret_settings=include_secret_settings, process_replacement_tokens=process_replacement_tokens)

Returns all configuration settings for this level

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)
learning_standard = 'learning_standard_example' # str | Required if singleSco is specified. Scopes the request to the provided learning standard. (optional)
single_sco = true # bool | Required if learningStandard is specified. Scopes settings to whether a package has only one SCO or assignable unit within it or not. To apply a configuration setting to a learning standard for single and multi-SCO content, it must be set for both scopes.  (optional)
include_metadata = true # bool |  (optional)
include_hidden_settings = true # bool | Should settings that are declared to be hidden be included. Note: such settings generally do not need to be modified, and may be confusing.  (optional)
include_secret_settings = true # bool | Should settings that are stored encrypted (type 'secretString') be included. Note: if included, the decrypted value will be returned.  (optional)
process_replacement_tokens = true # bool | Whether to process replacement tokens (false returns the raw value of each setting, without tokens or environment variable replacements) (optional)

try:
    # Returns all configuration settings for this level
    api_response = api_instance.get_application_configuration(engine_tenant_name=engine_tenant_name, learning_standard=learning_standard, single_sco=single_sco, include_metadata=include_metadata, include_hidden_settings=include_hidden_settings, include_secret_settings=include_secret_settings, process_replacement_tokens=process_replacement_tokens)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->get_application_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 
 **learning_standard** | **str**| Required if singleSco is specified. Scopes the request to the provided learning standard. | [optional] 
 **single_sco** | **bool**| Required if learningStandard is specified. Scopes settings to whether a package has only one SCO or assignable unit within it or not. To apply a configuration setting to a learning standard for single and multi-SCO content, it must be set for both scopes.  | [optional] 
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

# **get_authenticated_credential**
> CredentialSchema get_authenticated_credential(engine_tenant_name=engine_tenant_name)

Get information about the credential used to authenticate this request.

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains 'tenantName' which should be used for any permissions that need to be scoped to a particular tenant.  (optional)

try:
    # Get information about the credential used to authenticate this request.
    api_response = api_instance.get_authenticated_credential(engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->get_authenticated_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains &#x27;tenantName&#x27; which should be used for any permissions that need to be scoped to a particular tenant.  | [optional] 

### Return type

[**CredentialSchema**](CredentialSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credential**
> CredentialSchema get_credential(credential_id, engine_tenant_name=engine_tenant_name)

Get information on `credentialId` credential

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
credential_id = 'credential_id_example' # str | 
engine_tenant_name = 'engine_tenant_name_example' # str | If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains 'tenantName' which should be used for any permissions that need to be scoped to a particular tenant.  (optional)

try:
    # Get information on `credentialId` credential
    api_response = api_instance.get_credential(credential_id, engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->get_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 
 **engine_tenant_name** | **str**| If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains &#x27;tenantName&#x27; which should be used for any permissions that need to be scoped to a particular tenant.  | [optional] 

### Return type

[**CredentialSchema**](CredentialSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credentials**
> CredentialListSchema get_credentials(engine_tenant_name=engine_tenant_name)

List of credentials

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains 'tenantName' which should be used for any permissions that need to be scoped to a particular tenant.  (optional)

try:
    # List of credentials
    api_response = api_instance.get_credentials(engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->get_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains &#x27;tenantName&#x27; which should be used for any permissions that need to be scoped to a particular tenant.  | [optional] 

### Return type

[**CredentialListSchema**](CredentialListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pii_deletion_job**
> PIIDeletionResultSchema get_pii_deletion_job(engine_tenant_name, job_id)

Check the status of a PII deletion job with the provided job id.

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
job_id = 'job_id_example' # str | 

try:
    # Check the status of a PII deletion job with the provided job id.
    api_response = api_instance.get_pii_deletion_job(engine_tenant_name, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->get_pii_deletion_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **job_id** | **str**|  | 

### Return type

[**PIIDeletionResultSchema**](PIIDeletionResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_list**
> TenantListSchema get_tenant_list(include_deactivated=include_deactivated)

Get list of all tenants

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
include_deactivated = true # bool |  (optional)

try:
    # Get list of all tenants
    api_response = api_instance.get_tenant_list(include_deactivated=include_deactivated)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->get_tenant_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deactivated** | **bool**|  | [optional] 

### Return type

[**TenantListSchema**](TenantListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inspect_token**
> TokenInfoSchema inspect_token(token, engine_tenant_name=engine_tenant_name)

Inspect token

Verifies the signature of the provided token, and if valid returns information about the token 

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
token = 'token_example' # str | 
engine_tenant_name = 'engine_tenant_name_example' # str | If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains 'tenantName' which should be used for any permissions that need to be scoped to a particular tenant.  (optional)

try:
    # Inspect token
    api_response = api_instance.inspect_token(token, engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->inspect_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **engine_tenant_name** | **str**| If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains &#x27;tenantName&#x27; which should be used for any permissions that need to be scoped to a particular tenant.  | [optional] 

### Return type

[**TokenInfoSchema**](TokenInfoSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pii_deletion_job**
> PIIDeletionRequestResultSchema post_pii_deletion_job(body, engine_tenant_name)

Initiate a job to delete a user's Personal Identifying Information from the system.

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.PIIDeletionRequestSchema() # PIIDeletionRequestSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request

try:
    # Initiate a job to delete a user's Personal Identifying Information from the system.
    api_response = api_instance.post_pii_deletion_job(body, engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->post_pii_deletion_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PIIDeletionRequestSchema**](PIIDeletionRequestSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 

### Return type

[**PIIDeletionRequestResultSchema**](PIIDeletionRequestResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_update_encrypted_setting**
> post_update_encrypted_setting(engine_tenant_name)

Re-write settings, and statement pipe passwords using the current encryption settings. For password rotation.

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request

try:
    # Re-write settings, and statement pipe passwords using the current encryption settings. For password rotation.
    api_instance.post_update_encrypted_setting(engine_tenant_name)
except ApiException as e:
    print("Exception when calling AppManagementApi->post_update_encrypted_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_credential_secret**
> StringResultSchema reset_credential_secret(credential_id, engine_tenant_name=engine_tenant_name)

Reset credential secret

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
credential_id = 'credential_id_example' # str | 
engine_tenant_name = 'engine_tenant_name_example' # str | If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains 'tenantName' which should be used for any permissions that need to be scoped to a particular tenant.  (optional)

try:
    # Reset credential secret
    api_response = api_instance.reset_credential_secret(credential_id, engine_tenant_name=engine_tenant_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppManagementApi->reset_credential_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 
 **engine_tenant_name** | **str**| If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains &#x27;tenantName&#x27; which should be used for any permissions that need to be scoped to a particular tenant.  | [optional] 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_application_configuration**
> set_application_configuration(body, engine_tenant_name=engine_tenant_name, learning_standard=learning_standard, single_sco=single_sco)

Set configuration settings for this level.

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.SettingsPostSchema() # SettingsPostSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | optional tenant for this request (optional)
learning_standard = 'learning_standard_example' # str | Required if singleSco is specified. Scopes the request to the provided learning standard. (optional)
single_sco = true # bool | Required if learningStandard is specified. Scopes settings to whether a package has only one SCO or assignable unit within it or not. To apply a configuration setting to a learning standard for single and multi-SCO content, it must be set for both scopes.  (optional)

try:
    # Set configuration settings for this level.
    api_instance.set_application_configuration(body, engine_tenant_name=engine_tenant_name, learning_standard=learning_standard, single_sco=single_sco)
except ApiException as e:
    print("Exception when calling AppManagementApi->set_application_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsPostSchema**](SettingsPostSchema.md)|  | 
 **engine_tenant_name** | **str**| optional tenant for this request | [optional] 
 **learning_standard** | **str**| Required if singleSco is specified. Scopes the request to the provided learning standard. | [optional] 
 **single_sco** | **bool**| Required if learningStandard is specified. Scopes settings to whether a package has only one SCO or assignable unit within it or not. To apply a configuration setting to a learning standard for single and multi-SCO content, it must be set for both scopes.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credential**
> update_credential(body, credential_id, engine_tenant_name=engine_tenant_name)

Update `credentialId` credentials

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
api_instance = swagger_client.AppManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.CredentialRequestSchema() # CredentialRequestSchema | 
credential_id = 'credential_id_example' # str | 
engine_tenant_name = 'engine_tenant_name_example' # str | If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains 'tenantName' which should be used for any permissions that need to be scoped to a particular tenant.  (optional)

try:
    # Update `credentialId` credentials
    api_instance.update_credential(body, credential_id, engine_tenant_name=engine_tenant_name)
except ApiException as e:
    print("Exception when calling AppManagementApi->update_credential: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CredentialRequestSchema**](CredentialRequestSchema.md)|  | 
 **credential_id** | **str**|  | 
 **engine_tenant_name** | **str**| If specified, the tenant that will be used to store or validate the credentials or token. If not specified, the system data store / settings will be used. Note that PermissionsSchema contains &#x27;tenantName&#x27; which should be used for any permissions that need to be scoped to a particular tenant.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

