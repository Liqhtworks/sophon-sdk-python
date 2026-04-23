# UploadStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | **str** |  | 
**file_name** | **str** |  | 
**total_chunks** | **int** |  | 
**received_chunks** | **List[int]** | Array of 0-indexed part numbers that have been received. | 
**expires_at** | **datetime** |  | 
**source_width** | **int** | Source media width in pixels, populated from ffprobe after upload assembly. Null for uploads in &#x60;initiated&#x60;/&#x60;uploading&#x60; state or when probe failed.  | [optional] 
**source_height** | **int** | Source media height in pixels. See &#x60;source_width&#x60;. | [optional] 
**source_duration_seconds** | **float** | Source media duration in seconds, from ffprobe after upload assembly. Used by the webapp free-tier budget check to compute realistic billable_seconds (5-second ceiling rounding).  | [optional] 

## Example

```python
from sophon_sdk.models.upload_status_response import UploadStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadStatusResponse from a JSON string
upload_status_response_instance = UploadStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UploadStatusResponse.to_json())

# convert the object into a dict
upload_status_response_dict = upload_status_response_instance.to_dict()
# create an instance of UploadStatusResponse from a dict
upload_status_response_from_dict = UploadStatusResponse.from_dict(upload_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


