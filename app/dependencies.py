from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.services.auth import auth_service

bearer = HTTPBearer()

def get_current_student_id(credentials: HTTPAuthorizationCredentials=Depends(bearer)):
    try:
        auth_service.get_current_student(credentials.credentials)
    except ValueError:
        return {'message': 'Пользователь не авторизован'}
