from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.services.auth import auth_service

bearer = HTTPBearer()

def get_current_student_id(credentials: HTTPAuthorizationCredentials=Depends(bearer)):
    try:
        a = auth_service.get_current_student(credentials.credentials)
        return a
    except ValueError:
        return {'message': 'Пользователь не авторизован'}
