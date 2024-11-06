from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

class User(BaseModel):
    _id: str
    name: str
    email: str
    password: str
    disabled: bool
