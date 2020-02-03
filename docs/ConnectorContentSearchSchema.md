# ConnectorContentSearchSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** | only search using the specified connector | [optional] 
**search** | **str** |  | [optional] 
**since** | **datetime** | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
**context** | [**ConnectorContentSearchContextSchema**](ConnectorContentSearchContextSchema.md) |  | [optional] 
**more** | **str** | Token for getting the next set of results, from the prior set of results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

