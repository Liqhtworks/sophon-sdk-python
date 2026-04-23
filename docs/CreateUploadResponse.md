# CreateUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**chunk_size** | **int** | Size of each chunk in bytes. Tiered by file size: &lt;64 MB &#x3D; whole file, &lt;&#x3D;1 GB &#x3D; 8 MB, &lt;&#x3D;10 GB &#x3D; 16 MB, &gt;10 GB &#x3D; 32 MB.  | 
**total_chunks** | **int** |  | 
**expires_at** | **datetime** | Upload session expiry (24 hours from creation). | 

## Example

```python
from sophon_sdk.models.create_upload_response import CreateUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUploadResponse from a JSON string
create_upload_response_instance = CreateUploadResponse.from_json(json)
# print the JSON string representation of the object
print(CreateUploadResponse.to_json())

# convert the object into a dict
create_upload_response_dict = create_upload_response_instance.to_dict()
# create an instance of CreateUploadResponse from a dict
create_upload_response_from_dict = CreateUploadResponse.from_dict(create_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


