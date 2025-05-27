# Notion Clone API

API de backend para un clon de Notion desarrollado con FastAPI y SQLAlchemy.

## Descripción

Este proyecto implementa una API RESTful para una aplicación tipo Notion, permitiendo la gestión de tareas, usuarios, y funcionalidades de colaboración en tiempo real. La aplicación está construida con FastAPI, un moderno framework web de Python, y utiliza SQLAlchemy como ORM para interactuar con la base de datos.

## Tecnologías utilizadas

- **FastAPI**: Framework web de alto rendimiento para construir APIs con Python
- **SQLAlchemy**: ORM (Object Relational Mapper) para Python
- **MySQL**: Base de datos relacional (con posibilidad de migración a PostgreSQL)
- **Docker**: Contenedorización de la aplicación y servicios
- **WebSockets**: Comunicación en tiempo real
- **JWT**: Autenticación basada en tokens
- **Bcrypt**: Encriptación segura de contraseñas
- **Pydantic**: Validación de datos y serialización
- **Uvicorn**: Servidor ASGI para Python

## Estructura del proyecto

```
notion-clone-backend/
├── app/
│   ├── db/
│   │   ├── data.sql        # Datos de ejemplo para la base de datos
│   │   └── db.py           # Configuración de la conexión a la base de datos
│   ├── models/
│   │   └── models.py       # Definición de modelos de datos y esquemas
│   ├── routers/
│   │   ├── auth_basic.py   # Middleware de autenticación
│   │   ├── shared.py       # Rutas para compartir tareas
│   │   ├── tasks.py        # Rutas para gestión de tareas
│   │   ├── users.py        # Rutas para gestión de usuarios
│   │   └── websocket.py    # Rutas para WebSockets
│   ├── services/
│   │   └── websocket_service.py  # Servicio para gestionar conexiones WebSocket
│   └── main.py             # Punto de entrada de la aplicación
├── docker-compose.yml      # Configuración de Docker Compose
├── Dockerfile              # Configuración para construir la imagen Docker
├── render.yml              # Configuración para despliegue en Render
├── requirements.txt        # Dependencias del proyecto
└── .env                    # Variables de entorno
```

## Características principales

- **Autenticación y autorización**: Sistema completo con JWT para proteger las rutas
- **Gestión de tareas**: CRUD completo para tareas con estados y prioridades
- **Compartir tareas**: Funcionalidad para colaborar en tareas con otros usuarios
- **WebSockets**: Comunicación en tiempo real para actualizaciones colaborativas
- **Dockerización**: Configuración completa para desarrollo y producción en contenedores
- **Documentación automática**: API documentada automáticamente con Swagger UI

## Modelos de datos

### Usuarios

- `id`: UUID único
- `name`: Nombre del usuario
- `email`: Correo electrónico (único)
- `password`: Contraseña encriptada

### Tareas

- `id`: UUID único
- `title`: Título de la tarea
- `description`: Descripción detallada
- `state`: Estado (No comenzado, En progreso, Completado)
- `prioridad`: Prioridad (Baja, Media, Alta)
- `fecha_inicio`: Fecha de inicio
- `fecha_fin`: Fecha de finalización (opcional)
- `user_id`: ID del usuario propietario

### Tareas Compartidas

- `id`: UUID único
- `id_task`: ID de la tarea compartida
- `id_usuario`: ID del usuario con quien se comparte

## Endpoints principales

### Autenticación

- `POST /users/token`: Obtener token JWT
- `POST /users/check-token`: Verificar validez del token

### Usuarios

- `POST /users/`: Crear nuevo usuario
- `GET /users/check-email`: Verificar disponibilidad de email

### Tareas

- `GET /tasks/{user_id}`: Obtener todas las tareas de un usuario
- `GET /tasks/get-task/{task_id}`: Obtener una tarea específica
- `POST /tasks/`: Crear una nueva tarea
- `PUT /tasks/`: Actualizar una tarea existente
- `DELETE /tasks/{task_id}`: Eliminar una tarea

### Tareas compartidas

- `GET /shared/{user_id}`: Obtener tareas compartidas con un usuario
- `POST /shared/{user_id}`: Compartir una tarea con un usuario
- `DELETE /shared/{task_id}`: Eliminar tareas compartidas

### WebSockets

- `WebSocket /ws/{user}`: Conexión WebSocket para comunicación en tiempo real

## Configuración y despliegue

### Variables de entorno

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```
MYSQL_DATABASE=Notion_Clone
MYSQL_ROOT_PASSWORD=notion_clone_seccure
MYSQL_USER=tu_usuario
MYSQL_PASSWORD=tu_password
CORS_ORIGIN=http://localhost:4200
```

### Desarrollo local

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/notion-clone-backend.git
   cd notion-clone-backend
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Despliegue con Docker Compose

1. Asegúrate de tener Docker y Docker Compose instalados

2. Ejecuta:

   ```bash
   docker-compose up -d
   ```

3. Accede a:
   - API: http://localhost:8000
   - Documentación de la API: http://localhost:8000/docs
   - phpMyAdmin: http://localhost:8080

### Migración a PostgreSQL (opcional)

Para utilizar PostgreSQL en lugar de MySQL:

1. Modifica el archivo `docker-compose.yml` para usar PostgreSQL
2. Actualiza la variable `DATABASE_URL` en el servicio api-todo
3. Instala el driver de PostgreSQL: `pip install psycopg2-binary`
4. Reconstruye los contenedores: `docker-compose up -d --build`

## Documentación de la API

Una vez iniciada la aplicación, puedes acceder a la documentación interactiva:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Desarrollo

### Ejecutar pruebas

```bash
# TODO: Implementar pruebas
```

### Generar datos de prueba

El archivo `app/db/data.sql` contiene datos de ejemplo que puedes usar para poblar la base de datos durante el desarrollo.

## Licencia

[MIT](LICENSE)
