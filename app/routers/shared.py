import uuid
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from starlette import status
from app.db.db import get_db
from app.models.models import SharedTaskCreate, Tareas, Task, TaskSharedDB, Usuario, Usuarios
from app.routers.auth_basic import VerifyTokenRoute

router = APIRouter(
    prefix="/shared", 
    tags=["Shared"], 
    )

class TaskShare(BaseModel):
    task: Task
    creator: Usuario

@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=list[TaskShare])
def get_list_shared(user_id: str, db=Depends(get_db)) -> list[TaskShare]:
    res = db.query(TaskSharedDB).filter(TaskSharedDB.id_usuario == user_id).all()
    taskList: list[TaskShare] = []
    if not res:
        return taskList
    
    for item in res:
        task = db.query(Tareas).filter(Tareas.id == item.id_task).first()
        user = db.query(Usuarios).filter(Usuarios.id == task.user_id).first()
        item_data = Task(
            id = task.id,
            title = task.title,
            description = task.description,
            state = task.state,
            prioridad = task.prioridad,
            fecha_inicio = task.fecha_inicio,
            fecha_fin = task.fecha_fin,
            user_id = task.user_id
        )
        user_data = Usuario(
            id = user.id,
            name = user.name,
            email = user.email
        )
        taskList.append(TaskShare(task=item_data, creator=user_data))
    return taskList

@router.post('/{user_id}', status_code=status.HTTP_201_CREATED, response_model=SharedTaskCreate)
def create_shared_task(user_id:str, shared: SharedTaskCreate, db=Depends(get_db)):
    print(user_id)
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
    
    return shared

@router.delete('/{task_id}', status_code=status.HTTP_200_OK)
def delete_shared_task(task_id: str, db=Depends(get_db)):
    res = db.query(TaskSharedDB).filter(TaskSharedDB.id_task == task_id)
    if res:
        res.delete()
        db.commit()
        return {'message': 'Task deleted successfully'}
    raise HTTPException(status_code=404, detail='Task not found')