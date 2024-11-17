# https://fastapi.tiangolo.com/advanced/websockets/#handling-disconnections-and-multiple-clients

from fastapi import WebSocket, WebSocketDisconnect

from app.routers.users import get_user

class ConnectionManager:
    def __init__(self):
        # Guardo los websockets activos en un diccionario con el usuario como clave y el websocket como valor
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, user: str):
        await websocket.accept()
        self.active_connections[user] = websocket
        
    def disconnect(self, websocket: WebSocket):
        user_to_remove = None
        # Buscar el usuario por el WebSocket
        for email, conn in self.active_connections.items():
            if conn == websocket:
                user_to_remove = email
                break
        if user_to_remove:
            del self.active_connections[user_to_remove]
            print(f"Usuario desconectado: {user_to_remove}")
            
    async def send_personal_message(self, message: str, email: str):
        user = await get_user(email)
        ws = self.active_connections.get(user.name) # Obtener el websocket del usuario
        if ws is not None:
            await ws.send_text(message)
            # TODO si no está conectado, guardar una notificación para cuando se conecte

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
