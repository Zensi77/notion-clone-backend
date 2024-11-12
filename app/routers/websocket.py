from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from app.services.websocket_service import ConnectionManager

router = APIRouter(
    prefix="/ws", 
    tags=["Websocket"], 
)

manager = ConnectionManager()

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, tarea_id: str, usuario_id:str ):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{usuario_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{usuario_id} left the chat")