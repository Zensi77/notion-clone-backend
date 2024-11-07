from fastapi import APIRouter, Depends, HTTPException
from starlette import status
import uuid
import bcrypt

from app.db.db import get_db
from app.models.models import Usuario

router = APIRouter(prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}})

@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=Usuario)
async def getUser(user_id: str, db=Depends(get_db)) -> Usuario:
    resp = db.query(Usuario).filter(Usuario.id == user_id)
    if resp:
        return resp
    raise HTTPException(status_code=404, detail='User not found')

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Usuario)
async def newUser(user: Usuario, db=Depends(get_db)) -> Usuario:
    user.id = str(uuid.uuid4())
    bytes = user.password.encode('utf-8')
    salt = bcrypt.gensalt()
    user.password = bcrypt.hashpw(bytes, salt)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
    