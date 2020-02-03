# CourseSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**xapi_activity_id** | **str** | xAPI activity id associated with this course | [optional] 
**updated** | **datetime** |  | [optional] 
**web_path** | **str** | The web path at which the course&#x27;s contents are hosted. For AICC courses, refer to the href property of the child activities as this value will not be available. | [optional] 
**version** | **int** |  | [optional] 
**registration_count** | **int** |  | [optional] 
**activity_id** | **str** |  | [optional] 
**course_learning_standard** | **str** |  | [optional] 
**connector** | [**CourseConnectorSchema**](CourseConnectorSchema.md) |  | [optional] 
**metadata** | [**MetadataSchema**](MetadataSchema.md) |  | [optional] 
**root_activity** | [**CourseActivitySchema**](CourseActivitySchema.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

