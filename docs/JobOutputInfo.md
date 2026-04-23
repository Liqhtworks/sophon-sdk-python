# JobOutputInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**container** | **str** | Output container format (\&quot;mp4\&quot; or \&quot;mkv\&quot;). | 
**audio** | **bool** | Whether the output file actually contains audio. Reflects the muxed result, not the request flag — a video-only source with audio requested will report false.  | 
**target_height** | **int** | Customer-requested output height, echoed back. Null when the job ran at source dimensions (passthrough).  | [optional] 
**width** | **int** | Actual encoded output width in pixels (post-ffprobe). Null until the job completes or if the probe failed.  | [optional] 
**height** | **int** | Actual encoded output height in pixels. See &#x60;width&#x60;. | [optional] 
**bytes** | **int** |  | [optional] 
**sha256** | **str** |  | [optional] 
**retention_expires_at** | **datetime** |  | [optional] 

## Example

```python
from sophon_sdk.models.job_output_info import JobOutputInfo

# TODO update the JSON string below
json = "{}"
# create an instance of JobOutputInfo from a JSON string
job_output_info_instance = JobOutputInfo.from_json(json)
# print the JSON string representation of the object
print(JobOutputInfo.to_json())

# convert the object into a dict
job_output_info_dict = job_output_info_instance.to_dict()
# create an instance of JobOutputInfo from a dict
job_output_info_from_dict = JobOutputInfo.from_dict(job_output_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


