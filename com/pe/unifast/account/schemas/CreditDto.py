from pydantic import BaseModel


class CreditDto(BaseModel):
    ownedCredit: float
    preApprovedRequest: bool
    prevInstallmentOverdue: bool
    creditEligibility: bool
