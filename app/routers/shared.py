import uuid
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from app.db.db import get_db
from app.models.models import SharedTaskCreate, Tareas, Task, TaskSharedDB, Usuario, Usuarios
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
def create_shared_task(user_id:str, shared: SharedTaskCreate, db=Depends(get_db)):
    user: Usuario = db.query(Usuarios).filter(Usuarios.email == shared.email).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    
    # Saco la tarea que se quiere compartir, para sacar el usuario que la creó
    task: Task = db.query(Tareas).filter(Tareas.id == shared.task_id).first()
    
    # Se verifica si el usuario que quiere compartir la tarea es el mismo que la creó
    saved_hoster = db.query(TaskSharedDB).filter(TaskSharedDB.id_task == task.id, TaskSharedDB.id_usuario == user.id).first()
    # Si no hay registros, se agrega el usuario que creó la tarea
    if not saved_hoster:
        db.add(TaskSharedDB(
            id_task = task.id,
            id_usuario = task.user_id
        ))
        db.commit()
        db.refresh(task)
    
    data = TaskSharedDB(
        id = str(uuid.uuid4()),
        id_task = shared.task_id,
        id_usuario = user.id
    )
    db.add(data)
    db.commit()
    db.refresh(data)
    
    return data