from datetime import datetime, timedelta, timezone
import os
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
import jwt
from starlette import status
import uuid
import bcrypt

from app.db.db import get_db
from app.models.models import Token, TokenData, Usuario, Usuario_db

router = APIRouter(prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}})

@router.post("/", status_code=status.HTTP_201_CREATED)
async def newUser(user: Usuario, db=Depends(get_db)):
    user.id = str(uuid.uuid4())
    bytes = user.password.encode('utf-8')
    salt = bcrypt.gensalt()
    user.password = bcrypt.hashpw(bytes, salt)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    login_for_access_token(user, db) # Esto es para que el usuario se loguee automaticamente al registrarse y se le devuelva el token de acceso
    

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str, db=Depends(get_db)):
    res = db.query(Usuario_db).filter(Usuario_db.name == username).first()
    if res:
        # El doble asterisco el desempaquetado de diccionarios
        return Usuario_db(**res) # Esto es para que el modelo de datos sea compatible con el modelo de datos de la base de datos
    
def authenticate_user(username: str, password: str, db=Depends(get_db)):
    user = get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy() # Esto es para que no se modifique el diccionario original
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependencia para validar el token de acceso
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # el payload es el contenido del token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub") 
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.InvalidTokenError:
        raise credentials_exception
    user = get_user(username=token_data.username, db=Depends(get_db))
    if user is None:
        raise credentials_exception
    return user

# Ruta para obtener el token de acceso a partir del usuario y contraseña
@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")   
