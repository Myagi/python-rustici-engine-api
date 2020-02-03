# RegistrationSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**instance** | **int** |  | [optional] 
**xapi_registration_id** | **str** | xAPI registration id associated with this registration | [optional] 
**dispatch_id** | **str** | Dispatch ID for this registration, if applicable | [optional] 
**updated** | **datetime** |  | [optional] 
**registration_completion** | **str** |  | [optional] [default to 'UNKNOWN']
**registration_success** | **str** |  | [optional] [default to 'UNKNOWN']
**score** | [**ScoreSchema**](ScoreSchema.md) |  | [optional] 
**total_seconds_tracked** | **float** |  | [optional] 
**first_access_date** | **datetime** |  | [optional] 
**last_access_date** | **datetime** |  | [optional] 
**completed_date** | **datetime** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**course** | [**CourseReferenceSchema**](CourseReferenceSchema.md) |  | [optional] 
**learner** | [**LearnerSchema**](LearnerSchema.md) |  | [optional] 
**global_objectives** | [**list[ObjectiveSchema]**](ObjectiveSchema.md) |  | [optional] 
**activity_details** | [**ActivityResultSchema**](ActivityResultSchema.md) |  | [optional] 
**shared_data** | [**list[SharedDataEntrySchema]**](SharedDataEntrySchema.md) |  | [optional] 
**suspended_activity_id** | **str** |  | [optional] 
**registration_completion_amount** | **float** | A decimal value between 0 and 1 representing the percentage of this course that the learner has completed so far, if known. Note: for learning standards other than SCORM 2004 4th Edition, this value is based on the percentage of activities completed/passed. This means that single-activity courses in those standards will always return either 0 or 1.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

