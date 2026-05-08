# JobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**JobStatus**](JobStatus.md) |  | 
**status_reason** | **str** |  | [optional] 
**attempt** | **int** |  | 
**retryable** | **bool** | Whether the job can still be retried (attempt &lt; max_attempts and not terminal). | 
**profile** | [**JobProfile**](JobProfile.md) | Public profile ID submitted by the customer. For adaptive jobs this stays &#x60;sophon-auto&#x60;; see &#x60;effective_profile_id&#x60; for the worker&#39;s resolved concrete profile.  | 
**effective_profile_id** | **str** | Concrete profile resolved by the worker. Omitted until dispatch resolves. On explicit-profile jobs this equals &#x60;profile&#x60;. On &#x60;sophon-auto&#x60; jobs this is a variant identifier recording which path the API routed the source through; exact encoder settings for a given variant may be updated between releases as the adaptive logic is tuned.  | [optional] 
**source** | [**JobSourceInfo**](JobSourceInfo.md) |  | 
**progress** | [**JobProgress**](JobProgress.md) |  | 
**output** | [**JobOutputInfo**](JobOutputInfo.md) |  | 
**metadata** | **Dict[str, object]** | Arbitrary JSON object attached to a job. Keys and values are passed through unchanged to webhook deliveries and echoed on job reads. The serialized representation must not exceed 16 KiB. Free-form; SDKs surface this as a &#x60;Record&lt;string, unknown&gt;&#x60; / &#x60;dict[str, Any]&#x60; / &#x60;map[string]interface{}&#x60; depending on language.  | 
**created_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from sophon_sdk.models.job_response import JobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobResponse from a JSON string
job_response_instance = JobResponse.from_json(json)
# print the JSON string representation of the object
print(JobResponse.to_json())

# convert the object into a dict
job_response_dict = job_response_instance.to_dict()
# create an instance of JobResponse from a dict
job_response_from_dict = JobResponse.from_dict(job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


