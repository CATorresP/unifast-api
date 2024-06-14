from pydantic import BaseModel

class ProductCategoryDTO(BaseModel):
    productCategoryID: int
    productCategory : str