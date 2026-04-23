# UploadJobSource

Source backed by a completed chunked upload session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**JobSourceType**](JobSourceType.md) |  | 
**upload_id** | **str** | ID of a completed upload session. | 

## Example

```python
from sophon_sdk.models.upload_job_source import UploadJobSource

# TODO update the JSON string below
json = "{}"
# create an instance of UploadJobSource from a JSON string
upload_job_source_instance = UploadJobSource.from_json(json)
# print the JSON string representation of the object
print(UploadJobSource.to_json())

# convert the object into a dict
upload_job_source_dict = upload_job_source_instance.to_dict()
# create an instance of UploadJobSource from a dict
upload_job_source_from_dict = UploadJobSource.from_dict(upload_job_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


