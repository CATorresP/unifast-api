from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

# Configurar el logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Database URL
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://sa:myBANKadmin#y4p3@localhost:1434/Unifast?driver=ODBC+Driver+17+for+SQL+Server"

try:
    # Crear motor con logging
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
    logger.info("Base de datos conectada exitosamente")
except Exception as e:
    logger.error(f"Error al conectar con la base de datos: {e}")
    raise

# Sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base declarativa de modelos
Base = declarative_base()

class ReprMixin:
    def __repr__(self):
        columns = self.__table__.columns.keys()
        values = {column: getattr(self, column) for column in columns}
        values_str = ', '.join(f"{column}={value!r}" for column, value in values.items())
        return f"<{self.__class__.__name__}({values_str})>"