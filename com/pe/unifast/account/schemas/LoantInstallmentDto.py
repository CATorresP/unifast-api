from pydantic import BaseModel
from datetime import datetime

class LoanInstallmentDto(BaseModel):
    installmentID: int
    creditLoanID: int
    interest: float
    amount: float
    limitDate: datetime
    installmentStatus: str
    
    class Config:
        from_attributes = True