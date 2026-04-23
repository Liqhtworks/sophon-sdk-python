# WebhookListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url** | **str** |  | 
**active** | **bool** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from sophon_sdk.models.webhook_list_item import WebhookListItem

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookListItem from a JSON string
webhook_list_item_instance = WebhookListItem.from_json(json)
# print the JSON string representation of the object
print(WebhookListItem.to_json())

# convert the object into a dict
webhook_list_item_dict = webhook_list_item_instance.to_dict()
# create an instance of WebhookListItem from a dict
webhook_list_item_from_dict = WebhookListItem.from_dict(webhook_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


