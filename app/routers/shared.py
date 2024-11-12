import uuid
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from app.db.db import get_db
from app.models.models import SharedTaskCreate, Tareas, Task, TaskSharedDB
from app.routers.auth_basic import VerifyTokenRoute

router = APIRouter(
    prefix="/shared", 
    tags=["Shared"], 
    responses={404: {"description": "Not found"}},
    )

@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=list[Task])
def get_list_shared(user_id: str, db=Depends(get_db)) -> list[Task]:
    res = db.query(TaskSharedDB).filter(TaskSharedDB.id_usuario == user_id)
    
    if not res:
        return []
    return res

@router.post('/{user_id}', status_code=status.HTTP_201_CREATED, response_model=SharedTaskCreate)
def create_shared_task(shared: SharedTaskCreate, db=Depends(get_db)):
    data = TaskSharedDB(
        id = str(uuid.uuid4()),
        id_task = shared.task_id,
        id_usuario = shared.user_id
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    
    return data