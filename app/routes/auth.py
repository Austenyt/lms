from fastapi import APIRouter, Depends, HTTPException
from app.schemas.auth import UserRegister, UserLogin
from app.services.auth import auth_service
from app.db.database import get_session

auth_router = APIRouter(tags=['auth'])


@auth_router.post('/registration')
def registration(payload: UserRegister, session=Depends(get_session)):
    user = auth_service.register(payload.first_name, payload.last_name, payload.username, payload.password, session)
    return {'message': 'Регистрация успешна'}

@auth_router.post('/login')
def login(payload: StudentLogin, session=Depends(get_session)):
    try:
        return auth_service.login(payload.username, payload.password, session)
    except ValueError:
        raise HTTPException(status_code=401, detail="Пользователь не авторизован")
