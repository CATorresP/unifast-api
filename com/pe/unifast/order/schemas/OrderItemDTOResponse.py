from pydantic import BaseModel

class OrderItemResponseDTO(BaseModel):
    orderId: int
    productId: int
    productUnits: int
    price: float
    class Config:
        from_attributes = True
        #orm_mode = True