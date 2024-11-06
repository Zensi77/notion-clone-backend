from fastapi import APIRouter, Depends, HTTPException
from app.db.db import get_db

router = APIRouter(prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}})

@router.get("/users")
async def users():
    return {"users": [{"name": "MoureDev"}, {"name": "Test"}]}