from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

#cors midleware
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

#domain security
from com.pe.unifast.security.routers.auth_router import auth_router
app.include_router(auth_router, prefix="/api/v1/auth", tags=["auth"])

#domain account
from com.pe.unifast.account.routers.AccountRouter import account_router
from com.pe.unifast.account.routers.LoanInstallmentRouter import loanInstallmentRouter
from com.pe.unifast.account.routers.TransactionRouter import transactionRouter
from com.pe.unifast.account.routers.CreditRouter import creditRouter
from com.pe.unifast.account.routers.CreditRequestRouter import creditRequestRouter

app.include_router(account_router, prefix="/api/v1/account", tags=["account"])
app.include_router(loanInstallmentRouter, prefix="/api/v1/account", tags=["account"])
app.include_router(transactionRouter, prefix="/api/v1/account", tags=["account"])
app.include_router(creditRouter, prefix="/api/v1/account", tags=["account"])
app.include_router(creditRequestRouter, prefix="/api/v1/account", tags=["account"])

#domain order

from com.pe.unifast.order.routers.OrderRouter import orderRouter
from com.pe.unifast.order.routers.AddressDetailRouter import addressDetailRouter
from com.pe.unifast.order.routers.DeliveryRouter import deliveryRouter
from com.pe.unifast.order.routers.DepartmentRouter import departmentRouter
from com.pe.unifast.order.routers.DistrictRouter import districtRouter
from com.pe.unifast.order.routers.OrderItemRouter import orderItemRouter
from com.pe.unifast.order.routers.ProvinceRouter import provinceRouter

app.include_router(orderRouter, prefix="/api/v1/order", tags=["order"])
app.include_router(addressDetailRouter, prefix="/api/v1/order", tags=["order"])
app.include_router(deliveryRouter, prefix="/api/v1/order", tags=["order"])
app.include_router(departmentRouter, prefix="/api/v1/order", tags=["order"])
app.include_router(districtRouter, prefix="/api/v1/order", tags=["order"])
app.include_router(orderItemRouter, prefix="/api/v1/order", tags=["order"])
app.include_router(provinceRouter, prefix="/api/v1/order", tags=["order"])

#domain store

from com.pe.unifast.store.routers.BrandRouter import brandRouter
from com.pe.unifast.store.routers.ProductCategoryRouter import productCategoryRouter
from com.pe.unifast.store.routers.ProductRouter import productRouter
from com.pe.unifast.store.routers.SaleRouter import saleRouter
from com.pe.unifast.store.routers.SupplierRouter import supplierRouter

app.include_router(brandRouter, prefix="/api/v1/store", tags=["store"])
app.include_router(productCategoryRouter, prefix="/api/v1/store", tags=["store"])
app.include_router(productRouter, prefix="/api/v1/store", tags=["store"])
app.include_router(saleRouter, prefix="/api/v1/store", tags=["store"])
app.include_router(supplierRouter, prefix="/api/v1/store", tags=["store"])



import create_tables

