import datetime
from enum import Enum
from pydantic import BaseModel

# Clases de los modelos de la base de datos    
class Estado(Enum):
    NO_COMENZADO = "No comenzado"
    EN_PROGRESO = "En Progreso"
    TERMINADA = "Completado"
        
class Prioridad(Enum):
    BAJA = "Baja"
    MEDIA = "Media"
    ALTA = "Alta"
        
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.db import Base
class User(Base):
    __tablename__='Usuarios'
    
    id=Column(Integer, primary_key=True, index=True)
    name= Column(String(150), nullable=False)
    email= Column(String(150), nullable=False)
    password= Column(String(150), nullable=False)
    
class Task(Base):
    __tablename__='Tareas'
    
    id=Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(String(150))
    state = Column(Enum(Estado), default=Estado.NO_COMENZADO)
    prioridad = Column(Enum(Prioridad), default=Prioridad.BAJA)
    fecha_inicio = Column(DateTime, default=func.now())
    fecha_fin = Column(DateTime)
    user_id = Column(Integer, ForeignKey('Usuarios.id'))
    user = relationship('User', back_populates='tareas')
    
