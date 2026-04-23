# sophon_sdk.UploadsApi

All URIs are relative to *https://api.liqhtworks.xyz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_upload**](UploadsApi.md#cancel_upload) | **DELETE** /v1/uploads/{id} | Cancel an upload session
[**complete_upload**](UploadsApi.md#complete_upload) | **POST** /v1/uploads/{id}/complete | Finalize a chunked upload
[**create_upload**](UploadsApi.md#create_upload) | **POST** /v1/uploads | Initialize a chunked upload session
[**get_upload**](UploadsApi.md#get_upload) | **GET** /v1/uploads/{id} | Get upload session status
[**upload_part**](UploadsApi.md#upload_part) | **PUT** /v1/uploads/{id}/parts/{part_number} | Upload a single chunk


# **cancel_upload**
> cancel_upload(id)

Cancel an upload session

Sets the upload session to canceled and deletes staged chunks from disk.


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
    api_instance = sophon_sdk.UploadsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Cancel an upload session
        api_instance.cancel_upload(id)
    except Exception as e:
        print("Exception when calling UploadsApi->cancel_upload: %s\n" % e)
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
**204** | Upload canceled. No content returned. |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires uploads:write). |  * X-Request-Id -  <br>  |
**404** | Upload session not found. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_upload**
> CompleteUploadResponse complete_upload(id, idempotency_key)

Finalize a chunked upload

Assembles all received chunks into a single file, validates size matches
the declared file_size, probes with ffprobe, and transitions the session to completed.


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.models.complete_upload_response import CompleteUploadResponse
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
    api_instance = sophon_sdk.UploadsApi(api_client)
    id = 'id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | Client-generated UUID or string for exactly-once semantics. Required on all POST endpoints. Replaying the same key with the same request body returns the original response without side effects. 

    try:
        # Finalize a chunked upload
        api_response = api_instance.complete_upload(id, idempotency_key)
        print("The response of UploadsApi->complete_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->complete_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **idempotency_key** | **str**| Client-generated UUID or string for exactly-once semantics. Required on all POST endpoints. Replaying the same key with the same request body returns the original response without side effects.  | 

### Return type

[**CompleteUploadResponse**](CompleteUploadResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload assembled and validated. |  * X-Request-Id -  <br>  |
**400** | Not all chunks received. |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires uploads:write). |  * X-Request-Id -  <br>  |
**404** | Upload session not found. |  * X-Request-Id -  <br>  |
**409** | Upload session is not in \&quot;uploading\&quot; state. |  * X-Request-Id -  <br>  |
**422** | Assembled file size mismatch or not a valid video file (source_invalid). |  * X-Request-Id -  <br>  |
**503** | Disk capacity exceeded; cannot assemble. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload**
> CreateUploadResponse create_upload(idempotency_key, create_upload_request)

Initialize a chunked upload session

Starts a resumable source upload and returns the chunk size, chunk
count, session ID, and expiration timestamp.


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.models.create_upload_request import CreateUploadRequest
from sophon_sdk.models.create_upload_response import CreateUploadResponse
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
    api_instance = sophon_sdk.UploadsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Client-generated UUID or string for exactly-once semantics. Required on all POST endpoints. Replaying the same key with the same request body returns the original response without side effects. 
    create_upload_request = sophon_sdk.CreateUploadRequest() # CreateUploadRequest | 

    try:
        # Initialize a chunked upload session
        api_response = api_instance.create_upload(idempotency_key, create_upload_request)
        print("The response of UploadsApi->create_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->create_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Client-generated UUID or string for exactly-once semantics. Required on all POST endpoints. Replaying the same key with the same request body returns the original response without side effects.  | 
 **create_upload_request** | [**CreateUploadRequest**](CreateUploadRequest.md)|  | 

### Return type

[**CreateUploadResponse**](CreateUploadResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Upload session created. |  * X-Request-Id -  <br>  |
**400** | Validation error (empty file_name, zero file_size, exceeds max). |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires uploads:create). |  * X-Request-Id -  <br>  |
**409** | Idempotency conflict. |  * X-Request-Id -  <br>  |
**429** | Rate limited or quota exceeded. |  * X-Request-Id -  <br>  |
**503** | Disk capacity exceeded; uploads paused. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload**
> UploadStatusResponse get_upload(id)

Get upload session status

Returns received chunks and, after assembly/probe, source dimensions
and duration used by downstream budget and encoding decisions.


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.models.upload_status_response import UploadStatusResponse
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
    api_instance = sophon_sdk.UploadsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get upload session status
        api_response = api_instance.get_upload(id)
        print("The response of UploadsApi->get_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->get_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**UploadStatusResponse**](UploadStatusResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload session status. |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires uploads:read). |  * X-Request-Id -  <br>  |
**404** | Upload session not found. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_part**
> UploadPartResponse upload_part(id, part_number, body)

Upload a single chunk

Streams the chunk body to disk. Part numbers are 0-indexed.
Uploading the same part number again is idempotent (returns success without re-writing).


### Example

* Api Key Authentication (sessionCookie):
* Bearer Authentication (bearerApiKey):

```python
import sophon_sdk
from sophon_sdk.models.upload_part_response import UploadPartResponse
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
    api_instance = sophon_sdk.UploadsApi(api_client)
    id = 'id_example' # str | 
    part_number = 56 # int | 
    body = None # bytes | 

    try:
        # Upload a single chunk
        api_response = api_instance.upload_part(id, part_number, body)
        print("The response of UploadsApi->upload_part:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->upload_part: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **part_number** | **int**|  | 
 **body** | **bytes**|  | 

### Return type

[**UploadPartResponse**](UploadPartResponse.md)

### Authorization

[sessionCookie](../README.md#sessionCookie), [bearerApiKey](../README.md#bearerApiKey)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chunk received. |  * X-Request-Id -  <br>  |
**400** | Part number out of range. |  * X-Request-Id -  <br>  |
**401** | Missing or invalid credentials. |  * X-Request-Id -  <br>  |
**403** | Insufficient scope (requires uploads:write). |  * X-Request-Id -  <br>  |
**404** | Upload session not found. |  * X-Request-Id -  <br>  |
**409** | Upload session is not in \&quot;uploading\&quot; state. |  * X-Request-Id -  <br>  |
**503** | Disk capacity exceeded. |  * X-Request-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

