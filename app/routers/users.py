from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import jwt
from starlette import status
import uuid
import bcrypt

from app.db.db import get_db
from app.models.models import Token, TokenData, Usuarios, UsuarioRegister, Usuario

router = APIRouter(prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}})

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Usuario)
async def new_user(user: UsuarioRegister, db: Session=Depends(get_db)) -> Usuario:
    bytes = user.password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes, salt)
    # Se crea el modelo de datos del usuario para la base de datos
    user_data = Usuarios(
        id = str(uuid.uuid4()),
        password = hashed_password,
        name = user.name,
        email = user.email
    )
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data

@router.post('/check-email', status_code=status.HTTP_200_OK)
async def check_email(email: str, db: Session=Depends(get_db))->bool:
    res = db.query(Usuarios).filter(Usuarios.email == email).first()
    if res:
        return False # El email ya existe
    return True # El email no existe
        

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    
async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

# Se valida el usuario por el email
async def get_user(username: str, db: Session=Depends(get_db)):
    res = db.query(Usuarios).filter(Usuarios.email == username).first()
    if res:
        # El doble asterisco el desempaquetado de diccionarios
        return res
    raise HTTPException(status_code=404, detail="User not found")
   
async def authenticate_user(username: str, password: str, db=Depends(get_db)):
    user = await get_user(username, db)
    if not user:
        return False
    if not await verify_password(password, user.password):
        return False
    return user

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy() # Esto es para que no se modifique el diccionario original
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependencia para validar el token de acceso
@router.post('/check-token' , status_code=status.HTTP_200_OK, response_model=Usuario)
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # El payload es el contenido del token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email") 
        print(email)
        if email is None:
            raise credentials_exception
        token_data = TokenData(username=email) # Se crea el modelo de datos del token
    except jwt.InvalidTokenError:
        raise credentials_exception
    user = await get_user(username=token_data.username, db=db)
    if user is None:
        raise credentials_exception
    return user

# Ruta para obtener el token de acceso a partir del usuario y contraseña
@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db = Depends(get_db)
) -> Token:
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(
        data={"sub": user.name, "email": user.email, "id": user.id}, 
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")