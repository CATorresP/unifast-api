from config.database import Base,engine

#Domain Account
from com.pe.unifast.account.domain.entities.Account import Account
from com.pe.unifast.account.domain.entities.Credit import Credit
from com.pe.unifast.account.domain.entities.CreditRequest import CreditRequest
from com.pe.unifast.account.domain.entities.LoanInstallment import LoanInstallment
from com.pe.unifast.account.domain.entities.Transaction import Transaction
#Domain Order

from com.pe.unifast.order.domain.entities.AddressDetail import AddressDetail
from com.pe.unifast.order.domain.entities.Delivery import Delivery
from com.pe.unifast.order.domain.entities.Order import Order
from com.pe.unifast.order.domain.entities.OrderItem import OrderItem
from com.pe.unifast.order.domain.entities.Province import Province
from com.pe.unifast.order.domain.entities.District import District
from com.pe.unifast.order.domain.entities.Department import Department

#Domain Store
from com.pe.unifast.store.domain.entities.ProductCategories import ProductCategories
from com.pe.unifast.store.domain.entities.Product import Product
from com.pe.unifast.store.domain.entities.ProductCategory import ProductCategory
from com.pe.unifast.store.domain.entities.Brand import Brand
from com.pe.unifast.store.domain.entities.Supplier import Supplier
from com.pe.unifast.store.domain.entities.Sale import Sale




Base.metadata.create_all(bind=engine)
print("Tables created")
