from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.TransactionRepository import TransactionRepository
from ...schemas.TransactionDto import TransactionDto
from ...schemas.TransactionResponseDto import TransactionResponseDto
from ..entities.Transaction import Transaction
from ....shared.mapper.Mapper import Mapper

from signxml import XMLVerifier, XMLSigner
from lxml import etree
from OpenSSL import crypto

#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session





class TransactionService:
    class xmlManager:
        def __init__(self):
            self.KEY_PRIVATE = crypto.PKey("RSA")
            self.KEY_PRIVATE.generate_key(crypto.TYPE_RSA, 2048)
            self.KEY_PUBLIC = crypto.PKey("RSA")
            self.KEY_PUBLIC.generate_key(crypto.TYPE_RSA, 2048)
            self.CERT = crypto.X509()
            self.CERT.set_pubkey(self.KEY_PUBLIC)
            self.CERT.sign(self.KEY_PRIVATE, "sha256")
        
        def signXML(self, xml:str):
            signedXML = XMLSigner().sign(etree.fromstring(xml), key=self.KEY_PRIVATE, cert=self.CERT)
            return etree.tostring(signedXML)
        
        def verifyXML(self, xml:str):
            verifiedXML = XMLVerifier().verify(etree.fromstring(xml), x509_cert=self.CERT)
            if not verifiedXML:
                raise HTTPException(status_code=400, detail="Invalid XML")
            return verifiedXML
        
        def generateXML(self,transaction:Transaction):
            xml = f"<transaction><id>{transaction.accountID}</id><amount>{transaction.amount}</amount><description>{transaction.message}</description><subjectAccountId>{transaction.subjectAccountID}</subjectAccountId></transaction>"
            return self.signXML(xml)
        
        def parseXML(self, xml:str):
            return self.verifyXML(xml)
        

    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = TransactionRepository(db)
        self.mapper = Mapper()

    def get_transaction_by_id(self, transaction_id: int):
        transaction = self.repository.get_transaction_by_id(transaction_id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return self.mapper.entity_to_response_dto(transaction)
    
    def get_all_transaction(self):
        transactions = self.repository.get_all_transaction()
        return self.mapper.list_entity_to_list_dto(transactions)
    
    def update_transaction_by_id(self, transaction_id:int, transaction_dto:TransactionDto):
        transaction = self.repository.get_transaction_by_id(transaction_id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        transaction = self.mapper.dto_to_entity(transaction_dto)
        transaction = self.repository.update_transaction_by_id(transaction_id, transaction)
        return self.mapper.entity_to_response_dto(transaction)
    
    def delete_transaction_by_id(self, transaction_id:int):
        transaction = self.repository.get_transaction_by_id(transaction_id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        self.repository.delete_transaction_by_id(transaction_id)
        return

    def create_transaction(self, transaction_dto:TransactionDto):
        transaction :Transaction= self.mapper.dto_to_entity(transaction_dto)
        transaction.eBill = self.xmlManager.generateXML(transaction)
        transaction = self.repository.create_transaction(transaction)
        return self.mapper.entity_to_response_dto(transaction)
    
    
    