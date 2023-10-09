# indrive_client.OrdersApi

All URIs are relative to *https://api.masterdelivery.ru/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_cancel_order_public_v1_orders_order_id_delete**](OrdersApi.md#public_cancel_order_public_v1_orders_order_id_delete) | **DELETE** /orders/{order_id}/ | Public:Cancel Order
[**public_create_order_public_v1_orders_post**](OrdersApi.md#public_create_order_public_v1_orders_post) | **POST** /orders/ | Public:Create Order
[**public_dry_run_public_v1_orders_dry_run_post**](OrdersApi.md#public_dry_run_public_v1_orders_dry_run_post) | **POST** /orders/dry_run/ | Public:Dry Run
[**public_get_courier_position_public_v1_orders_order_id_tracking_get**](OrdersApi.md#public_get_courier_position_public_v1_orders_order_id_tracking_get) | **GET** /orders/{order_id}/tracking/ | Public:Get Courier Position
[**public_get_order_photos_public_v1_orders_order_id_photos_get**](OrdersApi.md#public_get_order_photos_public_v1_orders_order_id_photos_get) | **GET** /orders/{order_id}/photos/ | Public:Get Order Photos
[**public_get_order_public_v1_orders_order_id_get**](OrdersApi.md#public_get_order_public_v1_orders_order_id_get) | **GET** /orders/{order_id}/ | Public:Get Order
[**public_return_order_public_v1_orders_order_id_return_patch**](OrdersApi.md#public_return_order_public_v1_orders_order_id_return_patch) | **PATCH** /orders/{order_id}/return/ | Public:Return Order
[**public_return_order_public_v2_orders_order_id_return_patch**](OrdersApi.md#public_return_order_public_v2_orders_order_id_return_patch) | **PATCH** /v2/orders/{order_id}/return/ | Public:Return Order
[**public_update_order_public_v1_orders_order_id_patch**](OrdersApi.md#public_update_order_public_v1_orders_order_id_patch) | **PATCH** /orders/{order_id}/ | Public:Update Order

# **public_cancel_order_public_v1_orders_order_id_delete**
> public_cancel_order_public_v1_orders_order_id_delete(body, order_id)

Public:Cancel Order

Cancel order.

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
api_instance = indrive_client.OrdersApi(indrive_client.ApiClient(configuration))
body = indrive_client.CancelOrderInRequest()  # CancelOrderInRequest | 
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Public:Cancel Order
    api_instance.public_cancel_order_public_v1_orders_order_id_delete(body, order_id)
except ApiException as e:
    print("Exception when calling OrdersApi->public_cancel_order_public_v1_orders_order_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CancelOrderInRequest**](CancelOrderInRequest.md)|  | 
 **order_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_create_order_public_v1_orders_post**
> PublicOrderDetailForResponse public_create_order_public_v1_orders_post(body)

Public:Create Order

Create order to delivery

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
api_instance = indrive_client.OrdersApi(indrive_client.ApiClient(configuration))
body = indrive_client.CreateOrderInRequest()  # CreateOrderInRequest | 

try:
    # Public:Create Order
    api_response = api_instance.public_create_order_public_v1_orders_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->public_create_order_public_v1_orders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrderInRequest**](CreateOrderInRequest.md)|  | 

### Return type

[**PublicOrderDetailForResponse**](PublicOrderDetailForResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_dry_run_public_v1_orders_dry_run_post**
> BaseSchemaResponse public_dry_run_public_v1_orders_dry_run_post(body)

Public:Dry Run

Check whether order can be created

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
api_instance = indrive_client.OrdersApi(indrive_client.ApiClient(configuration))
body = indrive_client.OrderDryRun()  # OrderDryRun | 

try:
    # Public:Dry Run
    api_response = api_instance.public_dry_run_public_v1_orders_dry_run_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->public_dry_run_public_v1_orders_dry_run_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderDryRun**](OrderDryRun.md)|  | 

### Return type

[**BaseSchemaResponse**](BaseSchemaResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_courier_position_public_v1_orders_order_id_tracking_get**
> PublicCourierPositionForResponse public_get_courier_position_public_v1_orders_order_id_tracking_get(order_id)

Public:Get Courier Position

### Example

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = indrive_client.OrdersApi()
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Public:Get Courier Position
    api_response = api_instance.public_get_courier_position_public_v1_orders_order_id_tracking_get(order_id)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling OrdersApi->public_get_courier_position_public_v1_orders_order_id_tracking_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**str**](.md)|  | 

### Return type

[**PublicCourierPositionForResponse**](PublicCourierPositionForResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_order_photos_public_v1_orders_order_id_photos_get**
> list[OrderPhotoForResponse] public_get_order_photos_public_v1_orders_order_id_photos_get(order_id, authorization, photo_type=photo_type)

Public:Get Order Photos

Getting photos of the order

### Example

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = indrive_client.OrdersApi()
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 
authorization = 'authorization_example'  # str | 
photo_type = [indrive_client.OrderPhotoType()]  # list[OrderPhotoType] |  (optional)

try:
    # Public:Get Order Photos
    api_response = api_instance.public_get_order_photos_public_v1_orders_order_id_photos_get(order_id, authorization,
                                                                                             photo_type=photo_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->public_get_order_photos_public_v1_orders_order_id_photos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**str**](.md)|  | 
 **authorization** | **str**|  | 
 **photo_type** | [**list[OrderPhotoType]**](OrderPhotoType.md)|  | [optional] 

### Return type

[**list[OrderPhotoForResponse]**](OrderPhotoForResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_get_order_public_v1_orders_order_id_get**
> PublicOrderDetailForResponse public_get_order_public_v1_orders_order_id_get(order_id)

Public:Get Order

Get order info

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
api_instance = indrive_client.OrdersApi(indrive_client.ApiClient(configuration))
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Public:Get Order
    api_response = api_instance.public_get_order_public_v1_orders_order_id_get(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->public_get_order_public_v1_orders_order_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | [**str**](.md)|  | 

### Return type

[**PublicOrderDetailForResponse**](PublicOrderDetailForResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_return_order_public_v1_orders_order_id_return_patch**
> object public_return_order_public_v1_orders_order_id_return_patch(body, order_id)

Public:Return Order

Return products of order (deprecated)

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
api_instance = indrive_client.OrdersApi(indrive_client.ApiClient(configuration))
body = indrive_client.ReturnProductsInRequest()  # ReturnProductsInRequest | 
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Public:Return Order
    api_response = api_instance.public_return_order_public_v1_orders_order_id_return_patch(body, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->public_return_order_public_v1_orders_order_id_return_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReturnProductsInRequest**](ReturnProductsInRequest.md)|  | 
 **order_id** | [**str**](.md)|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_return_order_public_v2_orders_order_id_return_patch**
> object public_return_order_public_v2_orders_order_id_return_patch(body, order_id)

Public:Return Order

Return products of order

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
api_instance = indrive_client.OrdersApi(indrive_client.ApiClient(configuration))
body = indrive_client.ReturnProductsInRequestV2()  # ReturnProductsInRequestV2 | 
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Public:Return Order
    api_response = api_instance.public_return_order_public_v2_orders_order_id_return_patch(body, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->public_return_order_public_v2_orders_order_id_return_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReturnProductsInRequestV2**](ReturnProductsInRequestV2.md)|  | 
 **order_id** | [**str**](.md)|  | 

### Return type

**object**

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_update_order_public_v1_orders_order_id_patch**
> PublicOrderDetailForResponse public_update_order_public_v1_orders_order_id_patch(body, order_id)

Public:Update Order

Update order. Undesirable to use to cancel an order

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
api_instance = indrive_client.OrdersApi(indrive_client.ApiClient(configuration))
body = indrive_client.UpdateOrderInRequest()  # UpdateOrderInRequest | 
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Public:Update Order
    api_response = api_instance.public_update_order_public_v1_orders_order_id_patch(body, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->public_update_order_public_v1_orders_order_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateOrderInRequest**](UpdateOrderInRequest.md)|  | 
 **order_id** | [**str**](.md)|  | 

### Return type

[**PublicOrderDetailForResponse**](PublicOrderDetailForResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

