# CreateJobOutputOptions

Optional output shaping knobs for a new job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | [**OutputContainer**](OutputContainer.md) |  | [optional] [default to OutputContainer.MP4]
**audio** | **bool** | When true, audio is included in the output. MKV preserves source audio streams unchanged. MP4 preserves broadly compatible source audio codecs when possible, and may normalize incompatible codecs to AAC for playback compatibility. When false, the output is video only.  | [optional] [default to False]
**target_height** | **int** | Target output height in pixels. When set, output is scaled down (aspect ratio preserved, width derived from source, both dims rounded to even). If absent or larger than source height, output uses source dimensions. Billing tier is determined by the actual encoded output, not by this requested value.  | [optional] 

## Example

```python
from sophon_sdk.models.create_job_output_options import CreateJobOutputOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobOutputOptions from a JSON string
create_job_output_options_instance = CreateJobOutputOptions.from_json(json)
# print the JSON string representation of the object
print(CreateJobOutputOptions.to_json())

# convert the object into a dict
create_job_output_options_dict = create_job_output_options_instance.to_dict()
# create an instance of CreateJobOutputOptions from a dict
create_job_output_options_from_dict = CreateJobOutputOptions.from_dict(create_job_output_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


