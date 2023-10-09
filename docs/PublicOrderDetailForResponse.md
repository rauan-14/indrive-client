# PublicOrderDetailForResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**order_id** | **str** |  | 
**route_id** | **str** |  | [optional] 
**merchant** | [**OrderMerchant**](OrderMerchant.md) |  | 
**place_id** | **str** |  | [optional] 
**status** | [**OrderStatusEnum**](OrderStatusEnum.md) |  | 
**payment_status** | [**PaymentStatusEnum**](PaymentStatusEnum.md) |  | 
**cost** | [**OrderCost**](OrderCost.md) |  | 
**customer** | [**OrderCustomer**](OrderCustomer.md) |  | 
**person_count** | **int** |  | 
**comment** | **str** |  | [optional] 
**cancel_code** | [**OrderCancelCodeEnum**](OrderCancelCodeEnum.md) |  | [optional] 
**cancel_reason** | **str** |  | [optional] 
**is_force_start** | **bool** |  | 
**delivery** | [**PublicDeliveryForResponse**](PublicDeliveryForResponse.md) |  | 
**products** | [**list[ProductForResponse]**](ProductForResponse.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**additional_services** | [**list[AdditionalServiceInDB]**](AdditionalServiceInDB.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

