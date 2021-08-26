# EmailsPayload

Provide either rule or a list of emails, not both.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | **str** | SQL-like rule. Sending &#39;All&#39; as a value loads all resources of the given type. Help for building a segment rule can be found here: https://help.elasticemail.com/en/articles/5162182-segment-rules | [optional] 
**emails** | **[str]** | Comma delimited list of contact emails | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


