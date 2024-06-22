from pydantic import BaseModel


class CreditResponseDto(BaseModel):
    creditID: int
    ownedCredit: float
    preApprovedRequest: bool
    prevInstallmentOverdue: bool
    creditEligibility: bool

    class Config:
        from_attributes = True
