import json
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from app.services.websocket_service import ConnectionManager

router = APIRouter(
    prefix="/ws", 
    tags=["Websocket"], 
)

manager = ConnectionManager()

import json
from fastapi import WebSocket, WebSocketDisconnect

@router.websocket("/{user}")
async def websocket_endpoint(websocket: WebSocket, user: str):
    await manager.connect(websocket, user)  # Registrar al usuario
    print(f"Usuario conectado: {user}")

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Mensaje recibido de {user}: {data}")
            # await manager.send_personal_message(data, user)
            #try:
            #    data_dict = json.loads(data)
            #    print(f"Datos procesados como JSON: {data_dict}")
#
            #    to_user = data_dict.get("to")
            #    task = data_dict.get("task")
            #    from_user = data_dict.get("from")
#
            #    if to_user:
            #        response = {
            #            "message": f"Tienes una invitación para la tarea '{task}' de {from_user}",
            #            "task": task,
            #            "from": from_user,
            #        }
            #        await manager.send_personal_message(json.dumps(response), to_user)
            #    else:
            #        print("No se encontró el destinatario ('to').")
            #except json.JSONDecodeError:
            #    print("Error al parsear el JSON recibido")
            #    continue
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print(f"Usuario desconectado: {user}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        manager.disconnect(websocket)
        print(f"Usuario desconectado: {user}")