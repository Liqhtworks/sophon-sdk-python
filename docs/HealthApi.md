# sophon_sdk.HealthApi

All URIs are relative to *https://api.liqhtworks.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthz**](HealthApi.md#healthz) | **GET** /healthz | Liveness probe
[**readyz**](HealthApi.md#readyz) | **GET** /readyz | Readiness probe


# **healthz**
> healthz()

Liveness probe

Always returns 200. Used by load balancers and orchestrators.

### Example


```python
import sophon_sdk
from sophon_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.liqhtworks.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = sophon_sdk.Configuration(
    host = "https://api.liqhtworks.xyz"
)


# Enter a context with an instance of the API client
with sophon_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sophon_sdk.HealthApi(api_client)

    try:
        # Liveness probe
        api_instance.healthz()
    except Exception as e:
        print("Exception when calling HealthApi->healthz: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Service is alive. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **readyz**
> ReadyResponse readyz()

Readiness probe

Returns 200 when the service is ready to accept traffic. Checks database
connectivity, disk headroom (warning and critical thresholds), worker liveness,
and drain state.


### Example


```python
import sophon_sdk
from sophon_sdk.models.ready_response import ReadyResponse
from sophon_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.liqhtworks.xyz
# See configuration.py for a list of all supported configuration parameters.
configuration = sophon_sdk.Configuration(
    host = "https://api.liqhtworks.xyz"
)


# Enter a context with an instance of the API client
with sophon_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sophon_sdk.HealthApi(api_client)

    try:
        # Readiness probe
        api_response = api_instance.readyz()
        print("The response of HealthApi->readyz:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HealthApi->readyz: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReadyResponse**](ReadyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All readiness checks passed. |  * X-Request-Id -  <br>  |
**503** | One or more readiness checks failed. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

