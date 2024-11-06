import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from app.db.db import engine
import app.models.models as modelos
from app.routers import users

app = FastAPI()

app.include_router(users.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static") # Incluye la carpeta static para mosrtarla en el navegador
modelos.Base.metadata.create_all(bind=engine) # Crea las tablas en la base de datos
    
if (__name__ == "__main__"):
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) # Corre el servidor en el puerto 8000