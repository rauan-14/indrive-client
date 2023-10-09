# UpdateOrderInRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OrderStatusEnum**](OrderStatusEnum.md) |  | [optional] 
**payment_status** | [**PaymentStatusEnum**](PaymentStatusEnum.md) |  | [optional] 
**cost** | **float** |  | [optional] 
**additional_cost** | **float** |  | [optional] 
**change_cost** | **float** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**customer_phone** | **str** |  | [optional] 
**customer_email** | **str** |  | [optional] 
**person_count** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**cancel_code** | [**OrderCancelCodeEnum**](OrderCancelCodeEnum.md) |  | [optional] 
**cancel_reason** | **str** |  | [optional] 
**delivery** | [**UpdateDeliveryInRequest**](UpdateDeliveryInRequest.md) |  | [optional] 
**products** | [**list[CreateProductInRequest]**](CreateProductInRequest.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

