# CreateDispatchSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_id** | **str** | Destination Id | 
**course_id** | **str** | Serialized external package ID. | 
**allow_new_registrations** | **bool** | If true, then new registrations can be created for this dispatch. | [optional] [default to True]
**instanced** | **bool** | If true, then a new registration instance will be created if the client LMS doesn&#x27;t provide launch data for an existing one. Otherwise, the same instance will always be used for the given cmi.learner_id. | [optional] [default to True]
**registration_cap** | **int** | The maximum number of registrations that can be created for this dispatch, where &#x27;0&#x27; means &#x27;unlimited registrations&#x27;. | [optional] [default to 0]
**expiration_date** | **datetime** | The date after which this dispatch will be disabled as an ISO 8601 string, or not present for no expiration date. | [optional] 
**enabled** | **bool** | If true, then this dispatch can be launched. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

