from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..repositories.TransactionRepository import TransactionRepository
from ..repositories.AccountRepository import AccountRepository
from ..repositories.CreditRepository import CreditRepository
from ...schemas.TransactionDto import TransactionDto
from ...schemas.TransactionResponseDto import TransactionResponseDto



from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

from decimal import Decimal


#import depends

from typing import Annotated
from fastapi import  Depends
from sqlalchemy.orm import Session
from dependencies import get_db_session
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
import hashlib
import rsa


class XMLSign:

    def __init__(self):
            
            private_key_path = 'config/keys/private_key.pem'  
            public_key_path = 'config/keys/public_key.pem' 
            
            self.private_key = self.cargar_clave_privada(private_key_path)
            self.public_key = self.cargar_clave_publica(public_key_path)
    
        # Función para cargar la clave privada desde un archivo PEM
    def cargar_clave_privada(self,ruta_archivo, password=None):
        with open(ruta_archivo, 'rb') as archivo:
            clave_privada_pem = archivo.read()
            clave_privada = serialization.load_pem_private_key(
                clave_privada_pem,
                password=password,
                backend=default_backend()
            )
        return clave_privada

    # Función para cargar la clave pública desde un archivo PEM
    def cargar_clave_publica(self,ruta_archivo):
        with open(ruta_archivo, 'rb') as archivo:
            clave_publica_pem = archivo.read()
            clave_publica = serialization.load_pem_public_key(
                clave_publica_pem,
                backend=default_backend()
            )
        return clave_publica

    
    def generate_signature(self, xml_data: str) -> str:
        # Calcula el hash de los datos XML
        hash_value = hashlib.sha256(xml_data.encode()).digest()

        # Firma el hash usando la clave privada con PKCS#1 v1.5 padding
        signature = self.private_key.sign(
            hash_value,
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        # Codifica la firma en base64
        encoded_signature = base64.b64encode(signature).decode()

        return encoded_signature


    def verify_signature(self, xml_data: str, signature: str) -> bool:
        # Load public key
        public_key  = self.public_key

        # Calculate hash of the XML data
        hash_value = hashlib.sha256(xml_data.encode()).digest()

        # Decode the signature from base64
        decoded_signature = base64.b64decode(signature)

        # Verify the signature using the public key
        try:
            rsa.verify(hash_value, decoded_signature, public_key)
            return True
        except rsa.VerificationError:
            return False

    def generate_xml(self, transaction_dto: TransactionDto, account_id: int, subject_account_id: int) -> str:
        root = Element('transaction')
        amount = SubElement(root, 'amount')
        amount.text = str(transaction_dto.amount)
        message = SubElement(root, 'message')
        message.text = transaction_dto.message
        transaction_type = SubElement(root, 'transactionType')
        transaction_type.text = transaction_dto.transactionType
        account = SubElement(root, 'account')
        account.text = str(account_id)
        subject_account = SubElement(root, 'subjectAccount')
        subject_account.text = str(subject_account_id)

        xml_string = minidom.parseString(tostring(root)).toprettyxml(indent="  ")

        return xml_string


class TransactionService:
   
    def __init__(self, db: Annotated[Session, Depends(get_db_session)]):
        self.repository = TransactionRepository(db)
        self.accountRepository = AccountRepository(db)
        self.creditRepository = CreditRepository(db)

    def get_transaction_by_id(self, transaction_id: int):
        transaction = self.repository.get_transaction_by_id(transaction_id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return TransactionResponseDto(**transaction.__dict__)
    
    def get_all_transaction(self):
        transactions = self.repository.get_all_transaction()
        return [TransactionResponseDto(**transaction.__dict__) for transaction in transactions]
    
    def update_transaction_by_id(self, transaction_id:int, transaction_dto:TransactionDto):
        transaction = self.repository.get_transaction_by_id(transaction_id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")

        transaction = self.repository.update_transaction_by_id(transaction_id, transaction_dto)
        return  TransactionResponseDto(**transaction.__dict__)
    
    def delete_transaction_by_id(self, transaction_id:int):
        transaction = self.repository.get_transaction_by_id(transaction_id)
        if transaction is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        self.repository.delete_transaction_by_id(transaction_id)
        return

    def create_transaction(self, transaction_dto:TransactionDto,account_id:int):
        subjectAccount = self.accountRepository.find_by_phone_number(transaction_dto.subjectAccountPhoneNumber)
        account = self.accountRepository.find_by_id(account_id)

        if account is None and subjectAccount is None:
            raise HTTPException(status_code=404, detail="Account not found")
        
        subject_credit = self.creditRepository.find_by_id(subjectAccount.creditID)
        account_credit = self.creditRepository.find_by_id(account.creditID)

        if account_credit.ownedCredit < transaction_dto.amount:
            raise HTTPException(status_code=400, detail="Insufficient funds")
        
        amount_decimal = Decimal(str(transaction_dto.amount))
        new_owned_credit = account_credit.ownedCredit - amount_decimal

        subject_decimal = Decimal(str(subject_credit.ownedCredit))
        new_subject_credit = subject_decimal + amount_decimal


        
        self.creditRepository.update_credit_by_id(account.creditID, { "ownedCredit": new_owned_credit})
        self.creditRepository.update_credit_by_id(subjectAccount.creditID,{ "ownedCredit": new_subject_credit})
        
        xml_manager = XMLSign()

        eBill = xml_manager.generate_xml(transaction_dto,account_id,subjectAccount.accountID)
        eBillSign = xml_manager.generate_signature(eBill)

        transaction = self.repository.create_transaction( 
        transaction_dto.amount,
        transaction_dto.message,
        transaction_dto.transactionType,
        eBill,
        eBillSign,
        account_id,
        subjectAccount.accountID)


        return  TransactionResponseDto(**transaction.__dict__)



    
    