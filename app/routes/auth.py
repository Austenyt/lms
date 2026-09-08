from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.auth import UserRegister, UserLogin
from app.services.auth import auth_service
from app.db.database import get_session

auth_router = APIRouter(tags=['auth'])


@auth_router.post('/registration')
def registration(payload: UserRegister, session=Depends(get_session)) -> dict:
    user = auth_service.register(payload.first_name, payload.last_name, payload.username, payload.password, session)
    return {'message': 'Регистрация успешна'}


@auth_router.post('/login')
def login(payload: UserLogin, session=Depends(get_session)) -> UserLogin | HTTPException:
    try:
        return auth_service.login(payload.username, payload.password, session)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Пользователь не авторизован")
