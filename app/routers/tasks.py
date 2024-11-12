import uuid
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from app.db.db import get_db
from app.models.models import Tareas, Task, TaskCreate
from app.routers.auth_basic import VerifyTokenRoute

router = APIRouter(
    prefix="/tasks", 
    tags=["Tasks"], 
    responses={404: {"description": "Not found"}},
    route_class=VerifyTokenRoute # Se agrega la clase VerifyTokenRoute para verificar el token
    )

@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=list[Task])
async def get_tasks(user_id: str, db=Depends(get_db))->list[Task]:
    resp = db.query(Tareas).filter(Tareas.user_id==user_id).all()
    if resp:
        return resp
    elif resp == [] :
        return []
    raise HTTPException(status_code=404, detail='Not fount task list for user' + user_id)

@router.get('/get-task/{task_id}', status_code=status.HTTP_200_OK, response_model=Task)
async def get_task(task_id: str, db=Depends(get_db)) -> Task:
    res = db.query(Tareas).filter(Tareas.id == task_id).first()
    if res:
        return Task.model_validate(res)
    raise HTTPException(status_code=404, detail='Task not found')
    
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=TaskCreate)
async def create_task(task: TaskCreate, db=Depends(get_db)) -> TaskCreate:
    task_data = Tareas(
        id=str(uuid.uuid4()),
        title=task.title,
        description=task.description,
        state=task.state,
        prioridad=task.prioridad,
        fecha_inicio=task.fecha_inicio,
        fecha_fin=task.fecha_fin,
        user_id=task.user_id
    )
    db.add(task_data)
    db.commit()
    db.refresh(task_data)
    return task_data # Se devuelve el modelo de datos de la tarea con el id generado

@router.delete('/{task_id}', status_code=status.HTTP_200_OK, response_model=Task)
async def delete_task(task_id: str, db=Depends(get_db)) -> Task:
    res: Task = db.query(Tareas).filter(Tareas.id == task_id).first()
    if res:
        db.delete(res)
        db.commit()
        return res
    raise HTTPException(status_code=404, detail='Task not found')

@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=list[Task])
async def update_task(task_edit: Task,  db=Depends(get_db)):
    res: Task = db.query(Tareas).filter(Tareas.id == task_edit.id).first()
    print(res)
    if res:
        res.title = task_edit.title
        res.description = task_edit.description
        res.state = task_edit.state
        res.prioridad = task_edit.prioridad
        res.fecha_inicio = task_edit.fecha_inicio
        res.fecha_fin = task_edit.fecha_fin
        id_user = res.user_id
        res.id = task_edit.id
        db.commit()
    response = db.query(Tareas).filter(Tareas.user_id == id_user)
    if response:
        return response
    raise HTTPException(status_code=404, detail='Task not found')