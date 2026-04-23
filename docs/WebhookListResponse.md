# WebhookListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhooks** | [**List[WebhookListItem]**](WebhookListItem.md) |  | 

## Example

```python
from sophon_sdk.models.webhook_list_response import WebhookListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookListResponse from a JSON string
webhook_list_response_instance = WebhookListResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookListResponse.to_json())

# convert the object into a dict
webhook_list_response_dict = webhook_list_response_instance.to_dict()
# create an instance of WebhookListResponse from a dict
webhook_list_response_from_dict = WebhookListResponse.from_dict(webhook_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


