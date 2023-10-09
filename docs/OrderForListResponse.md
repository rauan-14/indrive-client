# OrderForListResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**order_id** | **str** |  | 
**merchant** | [**OrderMerchant**](OrderMerchant.md) |  | [optional] 
**place** | [**OrderPlace**](OrderPlace.md) |  | [optional] 
**area_id** | **str** |  | 
**status** | [**OrderStatusEnum**](OrderStatusEnum.md) |  | 
**payment_status** | [**PaymentStatusEnum**](PaymentStatusEnum.md) |  | 
**suggested_time** | **datetime** |  | [optional] 
**city_id** | **int** |  | [optional] 
**courier** | [**OrderCourier**](OrderCourier.md) |  | [optional] 
**is_normative_exceeded** | **bool** |  | 
**group_id** | **str** |  | [optional] 
**group_orders** | [**list[OrderForListResponse]**](OrderForListResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

