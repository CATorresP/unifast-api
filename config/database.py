from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

# Configurar el logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Database URL
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://sa:@localhost:3034/unifast?driver=ODBC+Driver+17+for+SQL+Server"


try:
    # Crear motor con logging
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        echo=True
    )
    logger.info("Base de datos conectada exitosamente")
except Exception as e:
    logger.error(f"Error al conectar con la base de datos: {e}")
    raise

# Sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base declarativa de modelos
Base = declarative_base()