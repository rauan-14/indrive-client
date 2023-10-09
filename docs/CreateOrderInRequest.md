# CreateOrderInRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**place_id** | **str** |  | 
**cost** | [**OrderCost**](OrderCost.md) |  | 
**person_count** | **int** |  | 
**comment** | **str** |  | [optional] 
**products** | [**list[CreateProductInRequest]**](CreateProductInRequest.md) |  | 
**additional_services** | [**list[AdditionalServiceCodeNameOnly]**](AdditionalServiceCodeNameOnly.md) |  | [optional] 
**is_force_start** | **bool** |  | [optional] [default to False]
**order_id** | **str** |  | 
**customer** | [**OrderCustomer**](OrderCustomer.md) |  | 
**delivery** | [**CreateDeliveryInRequest**](CreateDeliveryInRequest.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

