# ErrorBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 
**retryable** | **bool** | True for rate_limited, capacity_exceeded, and internal_error. Clients should retry with exponential backoff when true.  | 
**request_id** | **str** | Server-assigned request ID for correlation with logs. | [optional] 

## Example

```python
from sophon_sdk.models.error_body import ErrorBody

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorBody from a JSON string
error_body_instance = ErrorBody.from_json(json)
# print the JSON string representation of the object
print(ErrorBody.to_json())

# convert the object into a dict
error_body_dict = error_body_instance.to_dict()
# create an instance of ErrorBody from a dict
error_body_from_dict = ErrorBody.from_dict(error_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


