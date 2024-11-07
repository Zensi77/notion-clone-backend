import uuid
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from app.db.db import get_db
from app.models.models import Tareas, Task

router = APIRouter(prefix="/tasks", tags=["Tasks"], responses={404: {"description": "Not found"}})

@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=list[Task])
async def getTasks(user_id: str, db=Depends(get_db))->list[Task]:
    print(user_id)
    resp = db.query(Tareas).filter(Tareas.user_id==user_id).all()
    if resp:
        return resp
        
    raise HTTPException(status_code=404, detail='Not fount task list for user' + user_id)
    

@router.get("get-task/{task_id}", status_code=status.HTTP_200_OK, response_model=Task)
async def getTaskById(task_id= str, db=Depends(get_db)) -> Task:
    resp = db.query(Tareas).filter(Tareas.id == task_id)
    if resp:
        return resp
        
    raise HTTPException(status_code=404, detail='Not fount task' )

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Task)
async def createTask(task: Task, db=Depends(get_db)) -> Task:
    task.id = str(uuid.uuid4())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.delete('/{task_id}', status_code=status.HTTP_200_OK, response_model=Task)
async def deleteTask(task_id: str, db=Depends(get_db)) -> Task:
    res = db.query(Task).filter(Task.id == task_id)
    if res:
        db.delete(res)
        db.commit()
        return res
    raise HTTPException(status_code=404, detail='Task not found')

@router.put('/{task_id}', status_code=status.HTTP_202_ACCEPTED, response_model=list[Task])
async def updateTask(task_id: str, task_edit: Task,  db=Depends(get_db)):
    res: Task = db.query(Task).filter(Task.id == task_id)
    if res:
        res.title = task_edit.title
        res.description = task_edit.description
        res.estado = task_edit.estado
        res.prioridad = task_edit.prioridad
        res.fecha_inicio = task_edit.fecha_inicio
        res.fecha_fin = task_edit.fecha_fin
        db.commit()
        id_user = res.user_id
        return db.query(Task).filter(Task.user_id == id_user)
    raise HTTPException(status_code=404, detail='Task not found')