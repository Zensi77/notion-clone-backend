import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configuracion de la bd MySQL
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear la conexion a la bd
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()

def get_db():
    db = SessionLocal()
    try:
        # yield es como un return pero no termina la funcion, si no que la pausa y la reanuda cuando se necesite
        yield db
    finally:
        db.close()