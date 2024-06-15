from pydantic import BaseModel


class CreditDto(BaseModel):
    creditID: int
    ownedCredit: float
    preApprovedRequest: bool
    prevInstallmentOverdue: bool
    creditEligibility: bool
