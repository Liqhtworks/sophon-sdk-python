# WebhookDeliveryPayload

Payload delivered to registered webhook endpoints on terminal job events. Signed with HMAC-SHA256 over `\"{timestamp}.{raw_body}\"` using the per-webhook secret. Consumers must verify the signature before processing. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Unique delivery event ID for deduplication. | 
**type** | **str** | Event type. | 
**timestamp** | **datetime** | ISO 8601 timestamp of the event. | 
**job_id** | **str** | The job that reached a terminal state. | 
**status** | **str** | Terminal job status. | 
**metadata** | **Dict[str, object]** | Opaque metadata from the original job submission. | 

## Example

```python
from sophon_sdk.models.webhook_delivery_payload import WebhookDeliveryPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryPayload from a JSON string
webhook_delivery_payload_instance = WebhookDeliveryPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryPayload.to_json())

# convert the object into a dict
webhook_delivery_payload_dict = webhook_delivery_payload_instance.to_dict()
# create an instance of WebhookDeliveryPayload from a dict
webhook_delivery_payload_from_dict = WebhookDeliveryPayload.from_dict(webhook_delivery_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


