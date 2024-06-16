from pydantic import BaseModel

class ProductCategoriesResponseDTO(BaseModel):
    productID: int
    productCategoryID: int