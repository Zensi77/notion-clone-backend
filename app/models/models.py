from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from uuid import UUID

# Clases de los modelos de la base de datos    
class Estado(str, Enum):
    NO_COMENZADO = "No comenzado"
    EN_PROGRESO = "En Progreso"
    TERMINADA = "Completado"
        
class Prioridad(str, Enum):
    BAJA = "Baja"
    MEDIA = "Media"
    ALTA = "Alta"
    
class Usuario(BaseModel):
    id: UUID
    name: str
    email: str
    password: str
    
class Task(BaseModel):
    id: UUID
    title: str
    description: str
    state: Estado
    prioridad: Prioridad
    fecha_inicio: datetime
    fecha_fin: Optional[datetime]
    user_id: UUID
            
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, func, CHAR
from sqlalchemy.orm import relationship
from uuid import uuid4
from app.db.db import Base
class Usuarios(Base):
    __tablename__='Usuarios'
    
    id=Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    name= Column(String(150), nullable=False)
    email= Column(String(150), nullable=False)
    password= Column(String(150), nullable=False)
    
    tareas = relationship('Tareas', back_populates='user')
    
class Tareas(Base):
    __tablename__='Tareas'
    
    id=Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()), index=True)
    title = Column(String(150), nullable=False)
    description = Column(String(150))
    state = Column(Enum(Estado), default=Estado.NO_COMENZADO)
    prioridad = Column(Enum(Prioridad), default=Prioridad.BAJA)
    fecha_inicio = Column(DateTime, default=func.now())
    fecha_fin = Column(DateTime)
    user_id = Column(CHAR(36), ForeignKey('Usuarios.id'))
    
    user = relationship('Usuarios', back_populates='tareas')
    
