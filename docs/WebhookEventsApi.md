# sophon_sdk.WebhookEventsApi

All URIs are relative to *https://api.liqhtworks.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receive_job_terminal_webhook**](WebhookEventsApi.md#receive_job_terminal_webhook) | **POST** /jobTerminalEvent | Receive a terminal job webhook


# **receive_job_terminal_webhook**
> receive_job_terminal_webhook(x_turbo_signature_256, x_turbo_event_id, x_turbo_timestamp, webhook_delivery_payload)

Receive a terminal job webhook

Outbound webhook delivery sent to registered webhook endpoints when a
job reaches `completed`, `failed`, or `canceled`. Consumers should
verify `X-Turbo-Signature-256` before processing.


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.liqhtworks.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = sophon_sdk.Configuration(
    host = "https://api.liqhtworks.xyz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionCookie
configuration.api_key['sessionCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionCookie'] = 'Bearer'

# Configure Bearer authorization: bearerApiKey
configuration = sophon_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with sophon_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sophon_sdk.WebhookEventsApi(api_client)
    x_turbo_signature_256 = 'sha256=abc123def456...' # str | `sha256={hex}` — HMAC-SHA256 of `\"{X-Turbo-Timestamp}.{raw_body}\"` using the webhook's secret key. 
    x_turbo_event_id = 'evt_01JQabc123' # str | Unique event ID for consumer deduplication.
    x_turbo_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp used in signature computation. Check for replay.
    webhook_delivery_payload = sophon_sdk.WebhookDeliveryPayload() # WebhookDeliveryPayload | 

    try:
        # Receive a terminal job webhook
        api_instance.receive_job_terminal_webhook(x_turbo_signature_256, x_turbo_event_id, x_turbo_timestamp, webhook_delivery_payload)
    except Exception as e:
        print("Exception when calling WebhookEventsApi->receive_job_terminal_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_turbo_signature_256** | **str**| &#x60;sha256&#x3D;{hex}&#x60; — HMAC-SHA256 of &#x60;\&quot;{X-Turbo-Timestamp}.{raw_body}\&quot;&#x60; using the webhook&#39;s secret key.  | 
 **x_turbo_event_id** | **str**| Unique event ID for consumer deduplication. | 
 **x_turbo_timestamp** | **datetime**| Timestamp used in signature computation. Check for replay. | 
 **webhook_delivery_payload** | [**WebhookDeliveryPayload**](WebhookDeliveryPayload.md)|  | 

### Return type

void (empty response body)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook accepted by the consumer. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

