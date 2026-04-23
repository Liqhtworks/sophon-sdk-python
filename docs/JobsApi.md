# sophon_sdk.JobsApi

All URIs are relative to *https://api.liqhtworks.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](JobsApi.md#cancel_job) | **DELETE** /v1/jobs/{id} | Cancel a job
[**create_job**](JobsApi.md#create_job) | **POST** /v1/jobs | Submit an encoding job
[**get_job**](JobsApi.md#get_job) | **GET** /v1/jobs/{id} | Get a single job by ID
[**get_job_output**](JobsApi.md#get_job_output) | **GET** /v1/jobs/{id}/output | Get the encoded output file
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /v1/jobs | List jobs with cursor pagination


# **cancel_job**
> JobResponse cancel_job(id)

Cancel a job

Cancels a job in a non-terminal state (queued, probing, encoding, muxing,
uploading_output). Returns 409 if the job is already completed, failed, or canceled.


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.models.job_response import JobResponse
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
    api_instance = sophon_sdk.JobsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Cancel a job
        api_response = api_instance.cancel_job(id)
        print("The response of JobsApi->cancel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->cancel_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job canceled. Returns the updated job. |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires jobs:cancel). |  * X-Request-Id -  <br>  |
**404** | Job not found. |  * X-Request-Id -  <br>  |
**409** | Job is in a terminal state and cannot be canceled (job_not_cancelable). |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> JobResponse create_job(idempotency_key, create_job_request)

Submit an encoding job

Creates a queued encoding job from a completed upload source. The
`profile` field accepts explicit coffee profiles or `sophon-auto`,
and `output.target_height` can request aspect-preserving downscale.


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.models.create_job_request import CreateJobRequest
from sophon_sdk.models.job_response import JobResponse
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
    api_instance = sophon_sdk.JobsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Client-generated UUID or string for exactly-once semantics. Required on all POST endpoints. Replaying the same key with the same request body returns the original response without side effects. 
    create_job_request = sophon_sdk.CreateJobRequest() # CreateJobRequest | 

    try:
        # Submit an encoding job
        api_response = api_instance.create_job(idempotency_key, create_job_request)
        print("The response of JobsApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Client-generated UUID or string for exactly-once semantics. Required on all POST endpoints. Replaying the same key with the same request body returns the original response without side effects.  | 
 **create_job_request** | [**CreateJobRequest**](CreateJobRequest.md)|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Job created. |  * X-Request-Id -  <br>  |
**400** | Validation error (bad profile, source, container, metadata, or webhook_ids). |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires jobs:create). |  * X-Request-Id -  <br>  |
**409** | Idempotency conflict (same key, different request body). |  * X-Request-Id -  <br>  |
**422** | Source is invalid or unsupported. |  * X-Request-Id -  <br>  |
**429** | Rate limited or quota exceeded. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> JobResponse get_job(id)

Get a single job by ID

Returns current job state, progress, source metadata, resolved adaptive
profile information, and output availability for one job.


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.models.job_response import JobResponse
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
    api_instance = sophon_sdk.JobsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a single job by ID
        api_response = api_instance.get_job(id)
        print("The response of JobsApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job details. |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires jobs:read). |  * X-Request-Id -  <br>  |
**404** | Job not found. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_output**
> get_job_output(id)

Get the encoded output file

Returns a 302 redirect to a signed download URL for the job's output file.
The signed URL is valid for 24 hours.


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
    api_instance = sophon_sdk.JobsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get the encoded output file
        api_instance.get_job_output(id)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_output: %s\n" % e)
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
**302** | Redirect to signed download URL. The resolved resource is a video/mp4 file.  |  * Location - Signed download URL (24-hour TTL). Resolves to video/mp4. <br>  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires outputs:read). |  * X-Request-Id -  <br>  |
**404** | Job not found. |  * X-Request-Id -  <br>  |
**409** | Output not ready (job not in completed state). |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_jobs**
> ListJobsResponse list_jobs(status=status, limit=limit, cursor=cursor)

List jobs with cursor pagination

Returns jobs for the authenticated organization ordered by creation
time, with optional status filtering and opaque cursor pagination.


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.models.job_status import JobStatus
from sophon_sdk.models.list_jobs_response import ListJobsResponse
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
    api_instance = sophon_sdk.JobsApi(api_client)
    status = sophon_sdk.JobStatus() # JobStatus | Filter by job status. (optional)
    limit = 20 # int | Maximum number of items to return per page. (optional) (default to 20)
    cursor = 'cursor_example' # str | Opaque pagination cursor returned in a previous response's `next_cursor` field. (optional)

    try:
        # List jobs with cursor pagination
        api_response = api_instance.list_jobs(status=status, limit=limit, cursor=cursor)
        print("The response of JobsApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**JobStatus**](.md)| Filter by job status. | [optional] 
 **limit** | **int**| Maximum number of items to return per page. | [optional] [default to 20]
 **cursor** | **str**| Opaque pagination cursor returned in a previous response&#39;s &#x60;next_cursor&#x60; field. | [optional] 

### Return type

[**ListJobsResponse**](ListJobsResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of jobs, ordered by created_at descending. |  * X-Request-Id -  <br>  |
**400** | Invalid status filter or cursor. |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires jobs:read). |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

