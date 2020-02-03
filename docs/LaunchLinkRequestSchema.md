# LaunchLinkRequestSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **int** | The number of seconds from now that this link will expire in. This parameter should only be specified if the setting &#x27;ApiUseSignedLaunchLinks&#x27; is configured with a value of &#x27;true&#x27;. | [optional] [default to 120]
**redirect_on_exit_url** | **str** | The URL the application should redirect to when the learner exits a course. If not specified, configured value will be used. | [optional] 
**tracking** | **bool** | Should this launch be tracked? If false, Engine will avoid tracking to the extent possible for the standard being used. | [optional] [default to True]
**start_sco** | **str** | For SCORM, SCO identifier to override launch, overriding the normal sequencing. | [optional] 
**additional_values** | [**list[ItemValuePairSchema]**](ItemValuePairSchema.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

