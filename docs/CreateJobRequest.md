# CreateJobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**UploadJobSource**](UploadJobSource.md) |  | 
**profile** | [**JobProfile**](JobProfile.md) |  | 
**output** | [**CreateJobOutputOptions**](CreateJobOutputOptions.md) |  | [optional] 
**webhook_ids** | **List[str]** | IDs of registered webhook endpoints to notify on job state changes. | [optional] [default to []]
**metadata** | **Dict[str, object]** | Arbitrary key-value metadata attached to the job. Max 16 KiB serialized. | [optional] 

## Example

```python
from sophon_sdk.models.create_job_request import CreateJobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobRequest from a JSON string
create_job_request_instance = CreateJobRequest.from_json(json)
# print the JSON string representation of the object
print(CreateJobRequest.to_json())

# convert the object into a dict
create_job_request_dict = create_job_request_instance.to_dict()
# create an instance of CreateJobRequest from a dict
create_job_request_from_dict = CreateJobRequest.from_dict(create_job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


