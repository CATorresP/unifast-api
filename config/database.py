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
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://sa:myBANKadmin#y4p3@localhost:1433/Unifast?driver=ODBC+Driver+17+for+SQL+Server"

try:
    # Crear motor con logging
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
    # Probar conexión
    with engine.connect() as connection:
        result = connection.execute(select(1))
        assert result.scalar() == 1

    logger.info("Base de datos conectada exitosamente")
except Exception as e:
    logger.error(f"Error al conectar con la base de datos: {e}")
    raise

# Sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base declarativa de modelos
Base = declarative_base()

