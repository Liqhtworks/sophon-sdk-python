# sophon_sdk.WebhooksApi

All URIs are relative to *https://api.liqhtworks.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /v1/webhooks | Register a webhook endpoint
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /v1/webhooks/{id} | Soft-delete a webhook endpoint
[**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /v1/webhooks | List active webhook endpoints


# **create_webhook**
> WebhookResponse create_webhook(idempotency_key, create_webhook_request)

Register a webhook endpoint

Registers an HTTPS endpoint for terminal job events and returns the
HMAC signing secret once at creation time.


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.models.create_webhook_request import CreateWebhookRequest
from sophon_sdk.models.webhook_response import WebhookResponse
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
    api_instance = sophon_sdk.WebhooksApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Client-generated UUID or string for exactly-once semantics. Required on all POST endpoints. Replaying the same key with the same request body returns the original response without side effects. 
    create_webhook_request = sophon_sdk.CreateWebhookRequest() # CreateWebhookRequest | 

    try:
        # Register a webhook endpoint
        api_response = api_instance.create_webhook(idempotency_key, create_webhook_request)
        print("The response of WebhooksApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Client-generated UUID or string for exactly-once semantics. Required on all POST endpoints. Replaying the same key with the same request body returns the original response without side effects.  | 
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webhook registered. The response includes the HMAC secret (shown only once). |  * X-Request-Id -  <br>  |
**400** | Invalid URL (non-HTTPS, private IP, userinfo, etc.). |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires webhooks:manage). |  * X-Request-Id -  <br>  |
**409** | Idempotency conflict. |  * X-Request-Id -  <br>  |
**429** | Rate limited. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(id)

Soft-delete a webhook endpoint

Sets the webhook to inactive. It will no longer receive deliveries.

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
    api_instance = sophon_sdk.WebhooksApi(api_client)
    id = 'id_example' # str | 

    try:
        # Soft-delete a webhook endpoint
        api_instance.delete_webhook(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Webhook deactivated. No content returned. |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires webhooks:manage). |  * X-Request-Id -  <br>  |
**404** | Webhook not found or already inactive. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> WebhookListResponse list_webhooks()

List active webhook endpoints

Lists active webhook endpoints for the authenticated organization.


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.models.webhook_list_response import WebhookListResponse
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
    api_instance = sophon_sdk.WebhooksApi(api_client)

    try:
        # List active webhook endpoints
        api_response = api_instance.list_webhooks()
        print("The response of WebhooksApi->list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhookListResponse**](WebhookListResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of active webhooks for the authenticated organization. |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires webhooks:manage). |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

