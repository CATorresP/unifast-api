from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

# Configurar el logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

user = 'sa'
password = 'myBANKadmin#y4p3'
host = 'localhost'
port = '1433'
database = 'Unifast'

is_dev  = False

SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://{user}:{password}@{host}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

if is_dev == False:
    host  = 'db01'
    SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc://{user}:{password}@{host}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"


try :
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
    connection = engine.connect()
    print('Connection is successful')
except Exception as e:
    print('Error:', e)

# Sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base declarativa de modelos
Base = declarative_base()

