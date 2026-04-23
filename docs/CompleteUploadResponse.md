# CompleteUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**sha256** | **str** | SHA-256 hex digest of the assembled file. | 
**bytes** | **int** |  | 

## Example

```python
from sophon_sdk.models.complete_upload_response import CompleteUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteUploadResponse from a JSON string
complete_upload_response_instance = CompleteUploadResponse.from_json(json)
# print the JSON string representation of the object
print(CompleteUploadResponse.to_json())

# convert the object into a dict
complete_upload_response_dict = complete_upload_response_instance.to_dict()
# create an instance of CompleteUploadResponse from a dict
complete_upload_response_from_dict = CompleteUploadResponse.from_dict(complete_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


