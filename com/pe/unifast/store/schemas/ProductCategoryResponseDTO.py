from pydantic import BaseModel

class ProductCategoryResponseDTO(BaseModel):
    productCategoryID: int
    productCategory : str
    class Config:
        #orm_mode = True
        from_attributes = True