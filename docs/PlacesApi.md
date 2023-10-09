# indrive_client.PlacesApi

All URIs are relative to *https://api.masterdelivery.ru/public/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**place_schedule_get_public_v1_merchant_places_place_id_schedule_get**](PlacesApi.md#place_schedule_get_public_v1_merchant_places_place_id_schedule_get) | **GET** /merchant/places/{place_id}/schedule | Place Schedule:Get
[**place_schedule_update_public_v1_merchant_places_place_id_schedule_put**](PlacesApi.md#place_schedule_update_public_v1_merchant_places_place_id_schedule_put) | **PUT** /merchant/places/{place_id}/schedule | Place Schedule:Update
[**places_block_public_v1_merchant_places_block_post**](PlacesApi.md#places_block_public_v1_merchant_places_block_post) | **POST** /merchant/places/block/ | Places:Block
[**places_blocks_public_v1_merchant_places_blocks_get**](PlacesApi.md#places_blocks_public_v1_merchant_places_blocks_get) | **GET** /merchant/places/blocks/ | Places:Blocks
[**places_create_public_v1_merchant_places_post**](PlacesApi.md#places_create_public_v1_merchant_places_post) | **POST** /merchant/places | Places:Create
[**places_list_public_v1_merchant_places_get**](PlacesApi.md#places_list_public_v1_merchant_places_get) | **GET** /merchant/places | Places:List
[**places_order_check_public_v1_merchant_places_order_check_post**](PlacesApi.md#places_order_check_public_v1_merchant_places_order_check_post) | **POST** /merchant/places/order-check | Places:Order Check
[**places_unblock_public_v1_merchant_places_unblock_post**](PlacesApi.md#places_unblock_public_v1_merchant_places_unblock_post) | **POST** /merchant/places/unblock/ | Places:Unblock
[**places_update_public_v1_merchant_places_place_id_put**](PlacesApi.md#places_update_public_v1_merchant_places_place_id_put) | **PUT** /merchant/places/{place_id} | Places:Update

# **place_schedule_get_public_v1_merchant_places_place_id_schedule_get**
> WorkTimes place_schedule_get_public_v1_merchant_places_place_id_schedule_get(place_id)

Place Schedule:Get

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
api_instance = indrive_client.PlacesApi(indrive_client.ApiClient(configuration))
place_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Place Schedule:Get
    api_response = api_instance.place_schedule_get_public_v1_merchant_places_place_id_schedule_get(place_id)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling PlacesApi->place_schedule_get_public_v1_merchant_places_place_id_schedule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_id** | [**str**](.md)|  | 

### Return type

[**WorkTimes**](WorkTimes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_schedule_update_public_v1_merchant_places_place_id_schedule_put**
> WorkTimes place_schedule_update_public_v1_merchant_places_place_id_schedule_put(body, place_id)

Place Schedule:Update

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
api_instance = indrive_client.PlacesApi(indrive_client.ApiClient(configuration))
body = indrive_client.WorkTimesUpdate()  # WorkTimesUpdate | 
place_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Place Schedule:Update
    api_response = api_instance.place_schedule_update_public_v1_merchant_places_place_id_schedule_put(body, place_id)
    pprint(api_response)
except ApiException as e:
    print(
        "Exception when calling PlacesApi->place_schedule_update_public_v1_merchant_places_place_id_schedule_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkTimesUpdate**](WorkTimesUpdate.md)|  | 
 **place_id** | [**str**](.md)|  | 

### Return type

[**WorkTimes**](WorkTimes.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **places_block_public_v1_merchant_places_block_post**
> list[PlaceBlockInResponse] places_block_public_v1_merchant_places_block_post(body, authorization)

Places:Block

Blocks places for the specified period or endless. Use if you want to temporally stop orders creating for one or list of places

### Example

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = indrive_client.PlacesApi()
body = indrive_client.PlaceBlockInRequest()  # PlaceBlockInRequest | 
authorization = 'authorization_example'  # str | 

try:
    # Places:Block
    api_response = api_instance.places_block_public_v1_merchant_places_block_post(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacesApi->places_block_public_v1_merchant_places_block_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaceBlockInRequest**](PlaceBlockInRequest.md)|  | 
 **authorization** | **str**|  | 

### Return type

[**list[PlaceBlockInResponse]**](PlaceBlockInResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **places_blocks_public_v1_merchant_places_blocks_get**
> list[PlaceBlockInResponse] places_blocks_public_v1_merchant_places_blocks_get(authorization, place_ids=place_ids, limit=limit, offset=offset)

Places:Blocks

Returns list of active places blocks

### Example

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = indrive_client.PlacesApi()
authorization = 'authorization_example'  # str | 
place_ids = ['place_ids_example']  # list[str] |  (optional)
limit = 500  # int |  (optional) (default to 500)
offset = 0  # int |  (optional) (default to 0)

try:
    # Places:Blocks
    api_response = api_instance.places_blocks_public_v1_merchant_places_blocks_get(authorization, place_ids=place_ids,
                                                                                   limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacesApi->places_blocks_public_v1_merchant_places_blocks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | 
 **place_ids** | [**list[str]**](str.md)|  | [optional] 
 **limit** | **int**|  | [optional] [default to 500]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**list[PlaceBlockInResponse]**](PlaceBlockInResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **places_create_public_v1_merchant_places_post**
> PlaceInDB places_create_public_v1_merchant_places_post(body)

Places:Create

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
api_instance = indrive_client.PlacesApi(indrive_client.ApiClient(configuration))
body = indrive_client.PlaceWithArea()  # PlaceWithArea | 

try:
    # Places:Create
    api_response = api_instance.places_create_public_v1_merchant_places_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacesApi->places_create_public_v1_merchant_places_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaceWithArea**](PlaceWithArea.md)|  | 

### Return type

[**PlaceInDB**](PlaceInDB.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **places_list_public_v1_merchant_places_get**
> list[PlaceInDB] places_list_public_v1_merchant_places_get()

Places:List

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
api_instance = indrive_client.PlacesApi(indrive_client.ApiClient(configuration))

try:
    # Places:List
    api_response = api_instance.places_list_public_v1_merchant_places_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacesApi->places_list_public_v1_merchant_places_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PlaceInDB]**](PlaceInDB.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **places_order_check_public_v1_merchant_places_order_check_post**
> PlaceAccessList places_order_check_public_v1_merchant_places_order_check_post(body)

Places:Order Check

Check whether delivery from place is possible to adress

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
api_instance = indrive_client.PlacesApi(indrive_client.ApiClient(configuration))
body = indrive_client.OrderCheckInRequest()  # OrderCheckInRequest | 

try:
    # Places:Order Check
    api_response = api_instance.places_order_check_public_v1_merchant_places_order_check_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacesApi->places_order_check_public_v1_merchant_places_order_check_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCheckInRequest**](OrderCheckInRequest.md)|  | 

### Return type

[**PlaceAccessList**](PlaceAccessList.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **places_unblock_public_v1_merchant_places_unblock_post**
> list[PlaceBlockInResponse] places_unblock_public_v1_merchant_places_unblock_post(body, authorization)

Places:Unblock

Unblocks places

### Example

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = indrive_client.PlacesApi()
body = indrive_client.PlaceUnBlockInRequest()  # PlaceUnBlockInRequest | 
authorization = 'authorization_example'  # str | 

try:
    # Places:Unblock
    api_response = api_instance.places_unblock_public_v1_merchant_places_unblock_post(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacesApi->places_unblock_public_v1_merchant_places_unblock_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaceUnBlockInRequest**](PlaceUnBlockInRequest.md)|  | 
 **authorization** | **str**|  | 

### Return type

[**list[PlaceBlockInResponse]**](PlaceBlockInResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **places_update_public_v1_merchant_places_place_id_put**
> PlaceInDB places_update_public_v1_merchant_places_place_id_put(body, place_id)

Places:Update

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
api_instance = indrive_client.PlacesApi(indrive_client.ApiClient(configuration))
body = indrive_client.PlaceUpdate()  # PlaceUpdate | 
place_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d'  # str | 

try:
    # Places:Update
    api_response = api_instance.places_update_public_v1_merchant_places_place_id_put(body, place_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlacesApi->places_update_public_v1_merchant_places_place_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlaceUpdate**](PlaceUpdate.md)|  | 
 **place_id** | [**str**](.md)|  | 

### Return type

[**PlaceInDB**](PlaceInDB.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

