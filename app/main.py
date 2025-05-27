from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.db import engine
import app.models.models as modelos
from app.routers import shared, users, websocket
from app.routers import tasks

import os

app = FastAPI(title="API de tareas", description="API para la gestión de tareas", version="1.0.0")

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(shared.router)
app.include_router(websocket.router)
modelos.Base.metadata.create_all(bind=engine) # Crea las tablas en la base de datos

origins = [os.getenv("CORS_ORIGIN"), "http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
if (__name__ == "__main__"):
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) # Corre el servidor en el puerto 8000