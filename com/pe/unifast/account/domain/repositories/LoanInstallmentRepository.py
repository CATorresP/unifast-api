from typing import Optional

from sqlalchemy import select, update, delete, insert,join
from sqlalchemy.orm import Session
from com.pe.unifast.account.domain.entities.LoanInstallment import LoanInstallment


class LoanInstallmentRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_loan_installment_by_id(self, loan_installment_id: int):
        stmt = select(LoanInstallment).where(LoanInstallment.installmentID == loan_installment_id)
        return self.db.execute(stmt).scalar_one_or_none()
    
    def get_all_loan_installment(self):
        return self.db.execute(select(LoanInstallment)).scalars().all()
    
    def update_loan_installment_by_id(self, loan_installment_id:int, loan_installment:LoanInstallment):
        stmt = update(LoanInstallment).where(LoanInstallment.installmentID == loan_installment_id).values(loan_installment)
        self.db.execute(stmt)
        self.db.commit()
        return self.get_loan_installment_by_id(loan_installment_id)
    
    def delete_loan_installment_by_id(self, loan_installment_id:int):
        stmt = delete(LoanInstallment).where(LoanInstallment.installmentID == loan_installment_id)
        self.db.execute(stmt)
        self.db.commit()
        return
    
    def create_loan_installment(self, loan_installment:LoanInstallment):
        stmt = insert(LoanInstallment).values(loan_installment)
        self.db.execute(stmt)
        self.db.commit()
        return loan_installment
    