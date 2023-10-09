# indrive_client.MerchantApi

All URIs are relative to *https://api.masterdelivery.ru/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchant_schedule_get_public_v1_merchant_merchant_id_schedule_get**](MerchantApi.md#merchant_schedule_get_public_v1_merchant_merchant_id_schedule_get) | **GET** /merchant/{merchant_id}/schedule | Merchant Schedule:Get
[**merchant_schedule_update_public_v1_merchant_merchant_id_schedule_put**](MerchantApi.md#merchant_schedule_update_public_v1_merchant_merchant_id_schedule_put) | **PUT** /merchant/{merchant_id}/schedule | Merchant Schedule:Update

# **merchant_schedule_get_public_v1_merchant_merchant_id_schedule_get**
> WorkTimes merchant_schedule_get_public_v1_merchant_merchant_id_schedule_get(merchant_id)

Merchant Schedule:Get

### Example

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = indrive_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = indrive_client.MerchantApi(indrive_client.ApiClient(configuration))
merchant_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Merchant Schedule:Get
    api_response = api_instance.merchant_schedule_get_public_v1_merchant_merchant_id_schedule_get(merchant_id)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling MerchantApi->merchant_schedule_get_public_v1_merchant_merchant_id_schedule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | [**str**](.md)|  | 

### Return type

[**WorkTimes**](WorkTimes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchant_schedule_update_public_v1_merchant_merchant_id_schedule_put**
> WorkTimes merchant_schedule_update_public_v1_merchant_merchant_id_schedule_put(body, merchant_id)

Merchant Schedule:Update

### Example

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = indrive_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = indrive_client.MerchantApi(indrive_client.ApiClient(configuration))
body = indrive_client.WorkTimesUpdate()  # WorkTimesUpdate | 
merchant_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Merchant Schedule:Update
    api_response = api_instance.merchant_schedule_update_public_v1_merchant_merchant_id_schedule_put(body, merchant_id)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling MerchantApi->merchant_schedule_update_public_v1_merchant_merchant_id_schedule_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkTimesUpdate**](WorkTimesUpdate.md)|  | 
 **merchant_id** | [**str**](.md)|  | 

### Return type

[**WorkTimes**](WorkTimes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

