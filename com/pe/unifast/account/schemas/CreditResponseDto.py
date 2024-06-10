from pydantic import BaseModel


class CreditResponseDto(BaseModel):
    creditID: int
    ownedCredit: float
    preApprovedRequest: bool
    prevInstallmentOverdue: bool
    creditEligibility: bool

    class Config:
        orm_mode = True
        from_attributes = True
