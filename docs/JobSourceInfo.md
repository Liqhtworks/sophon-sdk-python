# JobSourceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Original file name of the source. | [optional] 
**bytes** | **int** |  | [optional] 
**sha256** | **str** | SHA-256 hex digest of the source file. | 
**duration_seconds** | **float** |  | [optional] 
**resolution** | **str** |  | [optional] 
**frame_rate** | **str** |  | [optional] 

## Example

```python
from sophon_sdk.models.job_source_info import JobSourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of JobSourceInfo from a JSON string
job_source_info_instance = JobSourceInfo.from_json(json)
# print the JSON string representation of the object
print(JobSourceInfo.to_json())

# convert the object into a dict
job_source_info_dict = job_source_info_instance.to_dict()
# create an instance of JobSourceInfo from a dict
job_source_info_from_dict = JobSourceInfo.from_dict(job_source_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


