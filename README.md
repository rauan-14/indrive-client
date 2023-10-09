# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.7.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/rauan-14/indrive-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/rauan-14/indrive-client.git`)

Then import the package:

```python
import indrive_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import indrive_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import indrive_client
from indrive_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = indrive_client.CallbacksApi(indrive_client.ApiClient(configuration))
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # The rider is near the delivery address callback
    api_instance.merchant_courier_near_delivery_address_callback_url_order_id_post(order_id)
except ApiException as e:
    print("Exception when calling CallbacksApi->merchant_courier_near_delivery_address_callback_url_order_id_post: %s\n" % e)

# create an instance of the API class
api_instance = indrive_client.CallbacksApi(indrive_client.ApiClient(configuration))
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # The rider is near the pickup place callback
    api_instance.merchant_courier_near_place_callback_url_order_id_post(order_id)
except ApiException as e:
    print("Exception when calling CallbacksApi->merchant_courier_near_place_callback_url_order_id_post: %s\n" % e)

# create an instance of the API class
api_instance = indrive_client.CallbacksApi(indrive_client.ApiClient(configuration))
order_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = indrive_client.OrderStatusCallback() # OrderStatusCallback |  (optional)

try:
    # The order changed callback
    api_instance.merchant_order_status_callback_url_order_id_post(order_id, body=body)
except ApiException as e:
    print("Exception when calling CallbacksApi->merchant_order_status_callback_url_order_id_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.masterdelivery.ru/public/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CallbacksApi* | [**merchant_courier_near_delivery_address_callback_url_order_id_post**](docs/CallbacksApi.md#merchant_courier_near_delivery_address_callback_url_order_id_post) | **POST** /merchant_courier_near_delivery_address_callback_url/{order_id} | The rider is near the delivery address callback
*CallbacksApi* | [**merchant_courier_near_place_callback_url_order_id_post**](docs/CallbacksApi.md#merchant_courier_near_place_callback_url_order_id_post) | **POST** /merchant_courier_near_place_callback_url/{order_id} | The rider is near the pickup place callback
*CallbacksApi* | [**merchant_order_status_callback_url_order_id_post**](docs/CallbacksApi.md#merchant_order_status_callback_url_order_id_post) | **POST** /merchant_order_status_callback_url/{order_id} | The order changed callback
*MerchantApi* | [**merchant_schedule_get_public_v1_merchant_merchant_id_schedule_get**](docs/MerchantApi.md#merchant_schedule_get_public_v1_merchant_merchant_id_schedule_get) | **GET** /merchant/{merchant_id}/schedule | Merchant Schedule:Get
*MerchantApi* | [**merchant_schedule_update_public_v1_merchant_merchant_id_schedule_put**](docs/MerchantApi.md#merchant_schedule_update_public_v1_merchant_merchant_id_schedule_put) | **PUT** /merchant/{merchant_id}/schedule | Merchant Schedule:Update
*OrdersApi* | [**public_cancel_order_public_v1_orders_order_id_delete**](docs/OrdersApi.md#public_cancel_order_public_v1_orders_order_id_delete) | **DELETE** /orders/{order_id}/ | Public:Cancel Order
*OrdersApi* | [**public_create_order_public_v1_orders_post**](docs/OrdersApi.md#public_create_order_public_v1_orders_post) | **POST** /orders/ | Public:Create Order
*OrdersApi* | [**public_dry_run_public_v1_orders_dry_run_post**](docs/OrdersApi.md#public_dry_run_public_v1_orders_dry_run_post) | **POST** /orders/dry_run/ | Public:Dry Run
*OrdersApi* | [**public_get_courier_position_public_v1_orders_order_id_tracking_get**](docs/OrdersApi.md#public_get_courier_position_public_v1_orders_order_id_tracking_get) | **GET** /orders/{order_id}/tracking/ | Public:Get Courier Position
*OrdersApi* | [**public_get_order_photos_public_v1_orders_order_id_photos_get**](docs/OrdersApi.md#public_get_order_photos_public_v1_orders_order_id_photos_get) | **GET** /orders/{order_id}/photos/ | Public:Get Order Photos
*OrdersApi* | [**public_get_order_public_v1_orders_order_id_get**](docs/OrdersApi.md#public_get_order_public_v1_orders_order_id_get) | **GET** /orders/{order_id}/ | Public:Get Order
*OrdersApi* | [**public_return_order_public_v1_orders_order_id_return_patch**](docs/OrdersApi.md#public_return_order_public_v1_orders_order_id_return_patch) | **PATCH** /orders/{order_id}/return/ | Public:Return Order
*OrdersApi* | [**public_return_order_public_v2_orders_order_id_return_patch**](docs/OrdersApi.md#public_return_order_public_v2_orders_order_id_return_patch) | **PATCH** /v2/orders/{order_id}/return/ | Public:Return Order
*OrdersApi* | [**public_update_order_public_v1_orders_order_id_patch**](docs/OrdersApi.md#public_update_order_public_v1_orders_order_id_patch) | **PATCH** /orders/{order_id}/ | Public:Update Order
*PlacesApi* | [**place_schedule_get_public_v1_merchant_places_place_id_schedule_get**](docs/PlacesApi.md#place_schedule_get_public_v1_merchant_places_place_id_schedule_get) | **GET** /merchant/places/{place_id}/schedule | Place Schedule:Get
*PlacesApi* | [**place_schedule_update_public_v1_merchant_places_place_id_schedule_put**](docs/PlacesApi.md#place_schedule_update_public_v1_merchant_places_place_id_schedule_put) | **PUT** /merchant/places/{place_id}/schedule | Place Schedule:Update
*PlacesApi* | [**places_block_public_v1_merchant_places_block_post**](docs/PlacesApi.md#places_block_public_v1_merchant_places_block_post) | **POST** /merchant/places/block/ | Places:Block
*PlacesApi* | [**places_blocks_public_v1_merchant_places_blocks_get**](docs/PlacesApi.md#places_blocks_public_v1_merchant_places_blocks_get) | **GET** /merchant/places/blocks/ | Places:Blocks
*PlacesApi* | [**places_create_public_v1_merchant_places_post**](docs/PlacesApi.md#places_create_public_v1_merchant_places_post) | **POST** /merchant/places | Places:Create
*PlacesApi* | [**places_list_public_v1_merchant_places_get**](docs/PlacesApi.md#places_list_public_v1_merchant_places_get) | **GET** /merchant/places | Places:List
*PlacesApi* | [**places_order_check_public_v1_merchant_places_order_check_post**](docs/PlacesApi.md#places_order_check_public_v1_merchant_places_order_check_post) | **POST** /merchant/places/order-check | Places:Order Check
*PlacesApi* | [**places_unblock_public_v1_merchant_places_unblock_post**](docs/PlacesApi.md#places_unblock_public_v1_merchant_places_unblock_post) | **POST** /merchant/places/unblock/ | Places:Unblock
*PlacesApi* | [**places_update_public_v1_merchant_places_place_id_put**](docs/PlacesApi.md#places_update_public_v1_merchant_places_place_id_put) | **PUT** /merchant/places/{place_id} | Places:Update

## Documentation For Models

 - [AdditionalServiceCodeNameOnly](docs/AdditionalServiceCodeNameOnly.md)
 - [AdditionalServiceInDB](docs/AdditionalServiceInDB.md)
 - [AllOfAreaCreateWithoutPlaceGeometry](docs/AllOfAreaCreateWithoutPlaceGeometry.md)
 - [AreaCreateWithoutPlace](docs/AreaCreateWithoutPlace.md)
 - [BaseSchemaResponse](docs/BaseSchemaResponse.md)
 - [CancelOrderInRequest](docs/CancelOrderInRequest.md)
 - [CreateDeliveryInRequest](docs/CreateDeliveryInRequest.md)
 - [CreateDeliveryInRequestV11](docs/CreateDeliveryInRequestV11.md)
 - [CreateIngredientInRequest](docs/CreateIngredientInRequest.md)
 - [CreateOrderInRequest](docs/CreateOrderInRequest.md)
 - [CreateOrderInRequestV11](docs/CreateOrderInRequestV11.md)
 - [CreateProductInRequest](docs/CreateProductInRequest.md)
 - [DbModelsBasePoint](docs/DbModelsBasePoint.md)
 - [DeliveryAttributes](docs/DeliveryAttributes.md)
 - [DeliveryDryRunInRequest](docs/DeliveryDryRunInRequest.md)
 - [DeliveryExpectedPeriod](docs/DeliveryExpectedPeriod.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [IngredientForResponse](docs/IngredientForResponse.md)
 - [JsonGeometry](docs/JsonGeometry.md)
 - [OrderCancelCodeEnum](docs/OrderCancelCodeEnum.md)
 - [OrderCheckInRequest](docs/OrderCheckInRequest.md)
 - [OrderCost](docs/OrderCost.md)
 - [OrderCourier](docs/OrderCourier.md)
 - [OrderCustomer](docs/OrderCustomer.md)
 - [OrderDryRun](docs/OrderDryRun.md)
 - [OrderForListResponse](docs/OrderForListResponse.md)
 - [OrderMerchant](docs/OrderMerchant.md)
 - [OrderPhotoForResponse](docs/OrderPhotoForResponse.md)
 - [OrderPhotoType](docs/OrderPhotoType.md)
 - [OrderPlace](docs/OrderPlace.md)
 - [OrderProblemCodeEnum](docs/OrderProblemCodeEnum.md)
 - [OrderStatusCallback](docs/OrderStatusCallback.md)
 - [OrderStatusCallbackPhotos](docs/OrderStatusCallbackPhotos.md)
 - [OrderStatusEnum](docs/OrderStatusEnum.md)
 - [Passport](docs/Passport.md)
 - [PaymentMethodEnum](docs/PaymentMethodEnum.md)
 - [PaymentStatusEnum](docs/PaymentStatusEnum.md)
 - [PlaceAccessForResponse](docs/PlaceAccessForResponse.md)
 - [PlaceAccessList](docs/PlaceAccessList.md)
 - [PlaceBlockInRequest](docs/PlaceBlockInRequest.md)
 - [PlaceBlockInResponse](docs/PlaceBlockInResponse.md)
 - [PlaceInDB](docs/PlaceInDB.md)
 - [PlaceUnBlockInRequest](docs/PlaceUnBlockInRequest.md)
 - [PlaceUpdate](docs/PlaceUpdate.md)
 - [PlaceWithArea](docs/PlaceWithArea.md)
 - [Point](docs/Point.md)
 - [ProductForResponse](docs/ProductForResponse.md)
 - [PublicCourierPositionForResponse](docs/PublicCourierPositionForResponse.md)
 - [PublicDeliveryForResponse](docs/PublicDeliveryForResponse.md)
 - [PublicDeliveryForResponseV11](docs/PublicDeliveryForResponseV11.md)
 - [PublicOrderDetailForResponse](docs/PublicOrderDetailForResponse.md)
 - [PublicOrderDetailForResponseV11](docs/PublicOrderDetailForResponseV11.md)
 - [RegularSchedule](docs/RegularSchedule.md)
 - [ReturnProductsInRequest](docs/ReturnProductsInRequest.md)
 - [ReturnProductsInRequestV2](docs/ReturnProductsInRequestV2.md)
 - [ReturnProductsInRequestV2Products](docs/ReturnProductsInRequestV2Products.md)
 - [SpecialSchedule](docs/SpecialSchedule.md)
 - [UpdateDeliveryInRequest](docs/UpdateDeliveryInRequest.md)
 - [UpdateOrderInRequest](docs/UpdateOrderInRequest.md)
 - [ValidationError](docs/ValidationError.md)
 - [Vehicle](docs/Vehicle.md)
 - [WorkTimes](docs/WorkTimes.md)
 - [WorkTimesUpdate](docs/WorkTimesUpdate.md)

## Documentation For Authorization


## APIKeyHeader

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author


