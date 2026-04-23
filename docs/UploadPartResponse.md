# UploadPartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_number** | **int** |  | 
**received** | **bool** |  | 

## Example

```python
from sophon_sdk.models.upload_part_response import UploadPartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPartResponse from a JSON string
upload_part_response_instance = UploadPartResponse.from_json(json)
# print the JSON string representation of the object
print(UploadPartResponse.to_json())

# convert the object into a dict
upload_part_response_dict = upload_part_response_instance.to_dict()
# create an instance of UploadPartResponse from a dict
upload_part_response_from_dict = UploadPartResponse.from_dict(upload_part_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


