from pydantic import BaseModel

class OrderItemDTO(BaseModel):
    orderId: int
    productId: int
    productUnits: int
    price: float
