from pydantic import BaseModel

class AddressDetailDTO(BaseModel):
    addressID: int
    districtID: int
    address: str
    blockNumber: int
    reference: str

