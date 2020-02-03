# MediaFileMetadataSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title for the referenced course content | [optional] 
**description** | **str** | Description of the referenced course content | [optional] 
**content_language** | **str** | Language code that specifies the content&#x27;s language. The default value is &#x27;en&#x27;. | [optional] 
**move_on** | **str** | Value of the cmi5 &#x27;moveOn&#x27; property for the referenced course content. The default value is &#x27;Completed&#x27;. | [optional] 
**estimated_duration** | **int** | Estimated number of seconds required to complete the course. | [optional] 
**activity_type** | **str** | The IRI activity type of the media content. If not provided, reasonable default values will be assumed based on the content&#x27;s &#x27;contentType&#x27;. | [optional] 
**cmi5_publisher_id** | **str** | The publisher ID for a cmi5 course. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

