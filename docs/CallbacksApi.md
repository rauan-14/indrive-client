# indrive_client.CallbacksApi

All URIs are relative to *https://api.masterdelivery.ru/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchant_courier_near_delivery_address_callback_url_order_id_post**](CallbacksApi.md#merchant_courier_near_delivery_address_callback_url_order_id_post) | **POST** /merchant_courier_near_delivery_address_callback_url/{order_id} | The rider is near the delivery address callback
[**merchant_courier_near_place_callback_url_order_id_post**](CallbacksApi.md#merchant_courier_near_place_callback_url_order_id_post) | **POST** /merchant_courier_near_place_callback_url/{order_id} | The rider is near the pickup place callback
[**merchant_order_status_callback_url_order_id_post**](CallbacksApi.md#merchant_order_status_callback_url_order_id_post) | **POST** /merchant_order_status_callback_url/{order_id} | The order changed callback

# **merchant_courier_near_delivery_address_callback_url_order_id_post**
> merchant_courier_near_delivery_address_callback_url_order_id_post(order_id)

The rider is near the delivery address callback

Notifies that the courier is located near the delivery address

### Example

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = indrive_client.CallbacksApi()
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # The rider is near the delivery address callback
    api_instance.merchant_courier_near_delivery_address_callback_url_order_id_post(order_id)
except ApiException as e:
    print(
        "Exception when calling CallbacksApi->merchant_courier_near_delivery_address_callback_url_order_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchant_courier_near_place_callback_url_order_id_post**
> merchant_courier_near_place_callback_url_order_id_post(order_id)

The rider is near the pickup place callback

Notifies that the courier is located near the place

### Example

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = indrive_client.CallbacksApi()
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # The rider is near the pickup place callback
    api_instance.merchant_courier_near_place_callback_url_order_id_post(order_id)
except ApiException as e:
    print("Exception when calling CallbacksApi->merchant_courier_near_place_callback_url_order_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchant_order_status_callback_url_order_id_post**
> merchant_order_status_callback_url_order_id_post(order_id, body=body)

The order changed callback

Notifies about order's status update or about delivery delaying

### Example

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = indrive_client.CallbacksApi()
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 
body = indrive_client.OrderStatusCallback()  # OrderStatusCallback |  (optional)

try:
    # The order changed callback
    api_instance.merchant_order_status_callback_url_order_id_post(order_id, body=body)
except ApiException as e:
    print("Exception when calling CallbacksApi->merchant_order_status_callback_url_order_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**str**](.md)|  | 
 **body** | [**OrderStatusCallback**](OrderStatusCallback.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

