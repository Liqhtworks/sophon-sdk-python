# JobProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage** | **str** | Current processing stage label (e.g. \&quot;probing\&quot;, \&quot;encoding\&quot;, \&quot;muxing\&quot;). | [optional] 
**phase** | [**JobStatus**](JobStatus.md) | Canonical pipeline phase used for progress semantics. | 
**percent** | **float** |  | 
**phase_percent** | **float** | Progress within the current phase. Null before active processing. | [optional] 
**fps** | **float** |  | [optional] 
**eta_seconds** | **int** |  | [optional] 
**frames_done** | **int** |  | [optional] 
**frames_total** | **int** |  | [optional] 

## Example

```python
from sophon_sdk.models.job_progress import JobProgress

# TODO update the JSON string below
json = "{}"
# create an instance of JobProgress from a JSON string
job_progress_instance = JobProgress.from_json(json)
# print the JSON string representation of the object
print(JobProgress.to_json())

# convert the object into a dict
job_progress_dict = job_progress_instance.to_dict()
# create an instance of JobProgress from a dict
job_progress_from_dict = JobProgress.from_dict(job_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


