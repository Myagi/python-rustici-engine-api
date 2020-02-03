# rustici_engine.CourseApi

All URIs are relative to */api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_course_preview_launch_link**](CourseApi.md#build_course_preview_launch_link) | **POST** /courses/{courseId}/preview | Returns the link to use to preview this course
[**build_course_preview_launch_link_with_version**](CourseApi.md#build_course_preview_launch_link_with_version) | **POST** /courses/{courseId}/versions/{versionId}/preview | Returns the link to use to preview this course
[**create_fetch_and_import_course_job**](CourseApi.md#create_fetch_and_import_course_job) | **POST** /courses/importJobs | Start a job to fetch and import a course.
[**create_upload_and_import_course_job**](CourseApi.md#create_upload_and_import_course_job) | **POST** /courses/importJobs/upload | Upload a course and start an import job for it.
[**delete_course**](CourseApi.md#delete_course) | **DELETE** /courses/{courseId} | Delete &#x60;courseId&#x60;
[**delete_course_configuration_setting**](CourseApi.md#delete_course_configuration_setting) | **DELETE** /courses/{courseId}/configuration/{settingId} | Clears the &#x60;settingId&#x60; value for this course
[**delete_course_version**](CourseApi.md#delete_course_version) | **DELETE** /courses/{courseId}/versions/{versionId} | Delete version &#x60;versionId&#x60; of &#x60;courseId&#x60;
[**delete_course_version_configuration_setting**](CourseApi.md#delete_course_version_configuration_setting) | **DELETE** /courses/{courseId}/versions/{versionId}/configuration/{settingId} | Clears the &#x60;settingId&#x60; value for this course and version.
[**get_course**](CourseApi.md#get_course) | **GET** /courses/{courseId} | Get information about &#x60;courseId&#x60;
[**get_course_configuration**](CourseApi.md#get_course_configuration) | **GET** /courses/{courseId}/configuration | Returns all configuration settings for this course
[**get_course_statements**](CourseApi.md#get_course_statements) | **GET** /courses/{courseId}/xAPIStatements | Get xAPI statements for &#x60;courseId&#x60;
[**get_course_version_configuration**](CourseApi.md#get_course_version_configuration) | **GET** /courses/{courseId}/versions/{versionId}/configuration | Returns all configuration settings for this course and version.
[**get_course_version_info**](CourseApi.md#get_course_version_info) | **GET** /courses/{courseId}/versions/{versionId} | Get version &#x60;versionId&#x60; of &#x60;courseId&#x60;
[**get_course_version_statements**](CourseApi.md#get_course_version_statements) | **GET** /courses/{courseId}/versions/{versionId}/xAPIStatements | Get xAPI statements for version &#x60;versionId&#x60; of &#x60;courseId&#x60;
[**get_course_versions**](CourseApi.md#get_course_versions) | **GET** /courses/{courseId}/versions | Get all versions of &#x60;courseId&#x60;
[**get_courses**](CourseApi.md#get_courses) | **GET** /courses | Get a list of all courses for the specified tenant
[**get_import_job_status**](CourseApi.md#get_import_job_status) | **GET** /courses/importJobs/{importJobId} | Check the status of an import job.
[**import_course_without_upload**](CourseApi.md#import_course_without_upload) | **POST** /courses | Create a course
[**set_course_configuration**](CourseApi.md#set_course_configuration) | **POST** /courses/{courseId}/configuration | Set configuration settings for this course.
[**set_course_title**](CourseApi.md#set_course_title) | **PUT** /courses/{courseId}/title | Sets the course title for &#x60;courseId&#x60;
[**set_course_version_configuration**](CourseApi.md#set_course_version_configuration) | **POST** /courses/{courseId}/versions/{versionId}/configuration | Set configuration settings for this course and version.
[**upload_and_import_course**](CourseApi.md#upload_and_import_course) | **POST** /courses/upload | Upload a course to import

# **build_course_preview_launch_link**
> LaunchLinkSchema build_course_preview_launch_link(body, engine_tenant_name, course_id)

Returns the link to use to preview this course

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.LaunchLinkRequestSchema() # LaunchLinkRequestSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 

try:
    # Returns the link to use to preview this course
    api_response = api_instance.build_course_preview_launch_link(body, engine_tenant_name, course_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->build_course_preview_launch_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LaunchLinkRequestSchema**](LaunchLinkRequestSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 

### Return type

[**LaunchLinkSchema**](LaunchLinkSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_course_preview_launch_link_with_version**
> LaunchLinkSchema build_course_preview_launch_link_with_version(body, engine_tenant_name, course_id, version_id)

Returns the link to use to preview this course

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.LaunchLinkRequestSchema() # LaunchLinkRequestSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
version_id = 56 # int | the course version

try:
    # Returns the link to use to preview this course
    api_response = api_instance.build_course_preview_launch_link_with_version(body, engine_tenant_name, course_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->build_course_preview_launch_link_with_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LaunchLinkRequestSchema**](LaunchLinkRequestSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **version_id** | **int**| the course version | 

### Return type

[**LaunchLinkSchema**](LaunchLinkSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fetch_and_import_course_job**
> StringResultSchema create_fetch_and_import_course_job(body, engine_tenant_name, course_id, may_create_new_version=may_create_new_version)

Start a job to fetch and import a course.

An import job will be started to fetch and import the referenced file, and the import job ID will be returned. If the import is successful, the imported course will be registered using the courseId provided.

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.ImportFetchRequestSchema() # ImportFetchRequestSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use.
may_create_new_version = true # bool | Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn't already exist. (optional)

try:
    # Start a job to fetch and import a course.
    api_response = api_instance.create_fetch_and_import_course_job(body, engine_tenant_name, course_id, may_create_new_version=may_create_new_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->create_fetch_and_import_course_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportFetchRequestSchema**](ImportFetchRequestSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**| A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use. | 
 **may_create_new_version** | **bool**| Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn&#x27;t already exist. | [optional] 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload_and_import_course_job**
> StringResultSchema create_upload_and_import_course_job(engine_tenant_name, course_id, file=file, uploaded_content_type=uploaded_content_type, may_create_new_version=may_create_new_version)

Upload a course and start an import job for it.

An import job will be started to import the posted file, and the import job ID will be returned. If the import is successful, the imported course will be registered using the courseId provided.

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use.
file = 'file_example' # str |  (optional)
uploaded_content_type = 'uploaded_content_type_example' # str | The MIME type identifier for the content to be uploaded (optional)
may_create_new_version = true # bool | Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn't already exist. (optional)

try:
    # Upload a course and start an import job for it.
    api_response = api_instance.create_upload_and_import_course_job(engine_tenant_name, course_id, file=file, uploaded_content_type=uploaded_content_type, may_create_new_version=may_create_new_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->create_upload_and_import_course_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**| A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use. | 
 **file** | **str**|  | [optional] 
 **uploaded_content_type** | **str**| The MIME type identifier for the content to be uploaded | [optional] 
 **may_create_new_version** | **bool**| Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn&#x27;t already exist. | [optional] 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course**
> delete_course(engine_tenant_name, course_id)

Delete `courseId`

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 

try:
    # Delete `courseId`
    api_instance.delete_course(engine_tenant_name, course_id)
except ApiException as e:
    print("Exception when calling CourseApi->delete_course: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course_configuration_setting**
> delete_course_configuration_setting(engine_tenant_name, course_id, setting_id)

Clears the `settingId` value for this course

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
setting_id = 'setting_id_example' # str | 

try:
    # Clears the `settingId` value for this course
    api_instance.delete_course_configuration_setting(engine_tenant_name, course_id, setting_id)
except ApiException as e:
    print("Exception when calling CourseApi->delete_course_configuration_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **setting_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course_version**
> delete_course_version(engine_tenant_name, course_id, version_id)

Delete version `versionId` of `courseId`

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
version_id = 56 # int | the course version

try:
    # Delete version `versionId` of `courseId`
    api_instance.delete_course_version(engine_tenant_name, course_id, version_id)
except ApiException as e:
    print("Exception when calling CourseApi->delete_course_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **version_id** | **int**| the course version | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course_version_configuration_setting**
> delete_course_version_configuration_setting(engine_tenant_name, course_id, version_id, setting_id)

Clears the `settingId` value for this course and version.

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
version_id = 56 # int | the course version
setting_id = 'setting_id_example' # str | 

try:
    # Clears the `settingId` value for this course and version.
    api_instance.delete_course_version_configuration_setting(engine_tenant_name, course_id, version_id, setting_id)
except ApiException as e:
    print("Exception when calling CourseApi->delete_course_version_configuration_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **version_id** | **int**| the course version | 
 **setting_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course**
> CourseSchema get_course(engine_tenant_name, course_id, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)

Get information about `courseId`

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
include_registration_count = true # bool | Include the registration count in the results (optional)
include_course_metadata = true # bool | Include course metadata in the results (optional)

try:
    # Get information about `courseId`
    api_response = api_instance.get_course(engine_tenant_name, course_id, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->get_course: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **include_registration_count** | **bool**| Include the registration count in the results | [optional] 
 **include_course_metadata** | **bool**| Include course metadata in the results | [optional] 

### Return type

[**CourseSchema**](CourseSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_configuration**
> SettingListSchema get_course_configuration(engine_tenant_name, course_id, include_metadata=include_metadata, include_hidden_settings=include_hidden_settings, include_secret_settings=include_secret_settings, process_replacement_tokens=process_replacement_tokens)

Returns all configuration settings for this course

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
include_metadata = true # bool |  (optional)
include_hidden_settings = true # bool | Should settings that are declared to be hidden be included. Note: such settings generally do not need to be modified, and may be confusing.  (optional)
include_secret_settings = true # bool | Should settings that are stored encrypted (type 'secretString') be included. Note: if included, the decrypted value will be returned.  (optional)
process_replacement_tokens = true # bool | Whether to process replacement tokens (false returns the raw value of each setting, without tokens or environment variable replacements) (optional)

try:
    # Returns all configuration settings for this course
    api_response = api_instance.get_course_configuration(engine_tenant_name, course_id, include_metadata=include_metadata, include_hidden_settings=include_hidden_settings, include_secret_settings=include_secret_settings, process_replacement_tokens=process_replacement_tokens)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->get_course_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
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

# **get_course_statements**
> XapiStatementResult get_course_statements(engine_tenant_name, course_id, learner_id=learner_id, since=since, until=until, more=more)

Get xAPI statements for `courseId`

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
learner_id = 'learner_id_example' # str | Only entries for the specified learner id will be included. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)

try:
    # Get xAPI statements for `courseId`
    api_response = api_instance.get_course_statements(engine_tenant_name, course_id, learner_id=learner_id, since=since, until=until, more=more)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->get_course_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **learner_id** | **str**| Only entries for the specified learner id will be included. | [optional] 
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

# **get_course_version_configuration**
> SettingListSchema get_course_version_configuration(engine_tenant_name, course_id, version_id, include_metadata=include_metadata, include_hidden_settings=include_hidden_settings, include_secret_settings=include_secret_settings, process_replacement_tokens=process_replacement_tokens)

Returns all configuration settings for this course and version.

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
version_id = 56 # int | the course version
include_metadata = true # bool |  (optional)
include_hidden_settings = true # bool | Should settings that are declared to be hidden be included. Note: such settings generally do not need to be modified, and may be confusing.  (optional)
include_secret_settings = true # bool | Should settings that are stored encrypted (type 'secretString') be included. Note: if included, the decrypted value will be returned.  (optional)
process_replacement_tokens = true # bool | Whether to process replacement tokens (false returns the raw value of each setting, without tokens or environment variable replacements) (optional)

try:
    # Returns all configuration settings for this course and version.
    api_response = api_instance.get_course_version_configuration(engine_tenant_name, course_id, version_id, include_metadata=include_metadata, include_hidden_settings=include_hidden_settings, include_secret_settings=include_secret_settings, process_replacement_tokens=process_replacement_tokens)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->get_course_version_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **version_id** | **int**| the course version | 
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

# **get_course_version_info**
> CourseSchema get_course_version_info(engine_tenant_name, course_id, version_id, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)

Get version `versionId` of `courseId`

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
version_id = 56 # int | the course version
include_registration_count = true # bool | Include the registration count in the results (optional)
include_course_metadata = true # bool | Include course metadata in the results (optional)

try:
    # Get version `versionId` of `courseId`
    api_response = api_instance.get_course_version_info(engine_tenant_name, course_id, version_id, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->get_course_version_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **version_id** | **int**| the course version | 
 **include_registration_count** | **bool**| Include the registration count in the results | [optional] 
 **include_course_metadata** | **bool**| Include course metadata in the results | [optional] 

### Return type

[**CourseSchema**](CourseSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_version_statements**
> XapiStatementResult get_course_version_statements(engine_tenant_name, course_id, version_id, learner_id=learner_id, since=since, until=until, more=more)

Get xAPI statements for version `versionId` of `courseId`

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
version_id = 56 # int | the course version
learner_id = 'learner_id_example' # str | Only entries for the specified learner id will be included. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)

try:
    # Get xAPI statements for version `versionId` of `courseId`
    api_response = api_instance.get_course_version_statements(engine_tenant_name, course_id, version_id, learner_id=learner_id, since=since, until=until, more=more)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->get_course_version_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **version_id** | **int**| the course version | 
 **learner_id** | **str**| Only entries for the specified learner id will be included. | [optional] 
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

# **get_course_versions**
> CourseListNonPagedSchema get_course_versions(engine_tenant_name, course_id, since=since, until=until, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)

Get all versions of `courseId`

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
include_registration_count = true # bool | Include the registration count in the results (optional)
include_course_metadata = true # bool | Include course metadata in the results (optional)

try:
    # Get all versions of `courseId`
    api_response = api_instance.get_course_versions(engine_tenant_name, course_id, since=since, until=until, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->get_course_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **include_registration_count** | **bool**| Include the registration count in the results | [optional] 
 **include_course_metadata** | **bool**| Include course metadata in the results | [optional] 

### Return type

[**CourseListNonPagedSchema**](CourseListNonPagedSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_courses**
> CourseListSchema get_courses(engine_tenant_name, more=more, since=since, until=until, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)

Get a list of all courses for the specified tenant

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of lists, where needed. An opaque value, construction and parsing may change without notice. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
include_registration_count = true # bool | Include the registration count in the results (optional)
include_course_metadata = true # bool | Include course metadata in the results (optional)

try:
    # Get a list of all courses for the specified tenant
    api_response = api_instance.get_courses(engine_tenant_name, more=more, since=since, until=until, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->get_courses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **more** | **str**| Value for this parameter will be provided in the &#x27;more&#x27; property of lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated up until the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **include_registration_count** | **bool**| Include the registration count in the results | [optional] 
 **include_course_metadata** | **bool**| Include course metadata in the results | [optional] 

### Return type

[**CourseListSchema**](CourseListSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_job_status**
> ImportJobResultSchema get_import_job_status(engine_tenant_name, import_job_id)

Check the status of an import job.

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
import_job_id = 'import_job_id_example' # str | Id received when the import job was submitted to the importJobs resource.

try:
    # Check the status of an import job.
    api_response = api_instance.get_import_job_status(engine_tenant_name, import_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->get_import_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **import_job_id** | **str**| Id received when the import job was submitted to the importJobs resource. | 

### Return type

[**ImportJobResultSchema**](ImportJobResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_course_without_upload**
> ImportResultSchema import_course_without_upload(body, engine_tenant_name, course_id, may_create_new_version=may_create_new_version, dry_run=dry_run)

Create a course

Import the specified course and return the results of the import. For large imports, it may be necessary to use importJobs instead to avoid timeouts.

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.ImportRequestSchema() # ImportRequestSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use.
may_create_new_version = true # bool | Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn't already exist. (optional)
dry_run = true # bool | Validate the course can be imported (mainly by validating the manifest), but don't actually import it. (optional)

try:
    # Create a course
    api_response = api_instance.import_course_without_upload(body, engine_tenant_name, course_id, may_create_new_version=may_create_new_version, dry_run=dry_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->import_course_without_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportRequestSchema**](ImportRequestSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**| A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use. | 
 **may_create_new_version** | **bool**| Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn&#x27;t already exist. | [optional] 
 **dry_run** | **bool**| Validate the course can be imported (mainly by validating the manifest), but don&#x27;t actually import it. | [optional] 

### Return type

[**ImportResultSchema**](ImportResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_course_configuration**
> set_course_configuration(body, engine_tenant_name, course_id)

Set configuration settings for this course.

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.SettingsPostSchema() # SettingsPostSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 

try:
    # Set configuration settings for this course.
    api_instance.set_course_configuration(body, engine_tenant_name, course_id)
except ApiException as e:
    print("Exception when calling CourseApi->set_course_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsPostSchema**](SettingsPostSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_course_title**
> set_course_title(body, engine_tenant_name, course_id)

Sets the course title for `courseId`

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.TitleSchema() # TitleSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 

try:
    # Sets the course title for `courseId`
    api_instance.set_course_title(body, engine_tenant_name, course_id)
except ApiException as e:
    print("Exception when calling CourseApi->set_course_title: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TitleSchema**](TitleSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_course_version_configuration**
> set_course_version_configuration(body, engine_tenant_name, course_id, version_id)

Set configuration settings for this course and version.

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
body = rustici_engine.SettingsPostSchema() # SettingsPostSchema | 
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | 
version_id = 56 # int | the course version

try:
    # Set configuration settings for this course and version.
    api_instance.set_course_version_configuration(body, engine_tenant_name, course_id, version_id)
except ApiException as e:
    print("Exception when calling CourseApi->set_course_version_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsPostSchema**](SettingsPostSchema.md)|  | 
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**|  | 
 **version_id** | **int**| the course version | 

### Return type

void (empty response body)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_and_import_course**
> ImportResultSchema upload_and_import_course(engine_tenant_name, course_id, file=file, uploaded_content_type=uploaded_content_type, may_create_new_version=may_create_new_version, dry_run=dry_run)

Upload a course to import

Upload and import the specified course and return the results of the import. For large imports, it may be necessary to use importJobs instead to avoid timeouts.

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
api_instance = rustici_engine.CourseApi(rustici_engine.ApiClient(configuration))
engine_tenant_name = 'engine_tenant_name_example' # str | tenant for this request
course_id = 'course_id_example' # str | A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use.
file = 'file_example' # str |  (optional)
uploaded_content_type = 'uploaded_content_type_example' # str | The MIME type identifier for the content to be uploaded (optional)
may_create_new_version = true # bool | Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn't already exist. (optional)
dry_run = true # bool | Validate the course can be imported (mainly by validating the manifest), but don't actually import it. (optional)

try:
    # Upload a course to import
    api_response = api_instance.upload_and_import_course(engine_tenant_name, course_id, file=file, uploaded_content_type=uploaded_content_type, may_create_new_version=may_create_new_version, dry_run=dry_run)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CourseApi->upload_and_import_course: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_tenant_name** | **str**| tenant for this request | 
 **course_id** | **str**| A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use. | 
 **file** | **str**|  | [optional] 
 **uploaded_content_type** | **str**| The MIME type identifier for the content to be uploaded | [optional] 
 **may_create_new_version** | **bool**| Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn&#x27;t already exist. | [optional] 
 **dry_run** | **bool**| Validate the course can be imported (mainly by validating the manifest), but don&#x27;t actually import it. | [optional] 

### Return type

[**ImportResultSchema**](ImportResultSchema.md)

### Authorization

[basic](../README.md#basic), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

