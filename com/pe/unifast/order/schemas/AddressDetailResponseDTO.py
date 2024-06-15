from pydantic import BaseModel

class AddressDetailResponseDTO(BaseModel):
    addressID: int
    districtID: int
    address: str
    blockNumber: int
    reference: str
    class Config:
            from_attributes = True
            #orm_mode = True