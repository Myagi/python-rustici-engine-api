# TokenRequestSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**PermissionsSchema**](PermissionsSchema.md) |  | 
**expiry** | **datetime** | Expiration of the token. This should not be set far in the future, as there is no way to invalidate an individual token. | 
**additional_values** | [**list[ItemValuePairSchema]**](ItemValuePairSchema.md) | Additional values to be included in the token | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

