from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute

from app.routers.users import get_current_user

class VerifyTokenRoute(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()
        
        async def verify_token_middleware(request: Request):
            print(request)
            # Se verifica si el token está en los headers
            if not 'Authorization' in request.headers:
                return JSONResponse(status_code=401, content={"detail": "Invalid token"})
            
            token = request.headers.get('Authorization').split(' ')[1]
            
            validation_response = get_current_user(token)
            if not validation_response:
                return JSONResponse(status_code=401, content={"detail": "Invalid token"})
            return await original_route(request)
        
        return verify_token_middleware
            