from pydantic import BaseModel

class ProductCategoriesDTO(BaseModel):
    productID: int
    productCategoryID: int