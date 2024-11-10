from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel

# Clases de los modelos de la base de datos    
class Estado(str, Enum):
    NO_COMENZADO = "No comenzado"
    EN_PROGRESO = "En progreso"
    TERMINADA = "Completado"
        
class Prioridad(str, Enum):
    BAJA = "Baja"
    MEDIA = "Media"
    ALTA = "Alta"
    
class Usuario(BaseModel):
    name: str
    email: str
    
class Usuario_db(Usuario):
    hashed_password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    
class TaskCreate(BaseModel):
    title: str
    description: str
    state: Estado
    prioridad: Prioridad
    fecha_inicio: date
    fecha_fin: Optional[date] = None
    user_id: str
    
class Task(TaskCreate):
    id: str 

    class Config: # Esto hace que el modelo de datos se pueda convertir a un diccionario
        from_attributes = True
            
from sqlalchemy import Column, Date, String, Enum, ForeignKey, func, CHAR
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
    fecha_inicio = Column(Date, default=func.now())
    fecha_fin = Column(Date)
    user_id = Column(CHAR(36), ForeignKey('Usuarios.id'))
    
    user = relationship('Usuarios', back_populates='tareas')
    
