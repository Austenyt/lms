from fastapi import APIRouter, Depends
from app.schemas.user import UserFind, UserCreate, UserPatch
from app.services.user_service import user_service
from app.db.database import get_session

users_router = APIRouter(tags=['users'])


@users_router.get('/users')
def users(session=Depends(get_session)):
    return user_service.get_all(session)


@users_router.post('/users/{id}')
def find(payload: UserFind, session=Depends(get_session)):
    try:
        return user_service.find(payload.id, session)
    except ValueError:
        return {'message': "Такого студента нет"}

@users_router.delete('/users/{id}')
def delete(payload: UserFind, session=Depends(get_session)):
    try:
        user_service.find(payload.id, session)
        return {'message': "Удаление успешно"}
    except ValueError:
        return {'message': 'Ошибка'}


@users_router.post('/users/{user_id}/{course_id}')
def enroll(course_id, user_id, session=Depends(get_session)):
    try:
        user_service.enroll(course_id, user_id, session)
        return {'message': 'Пользователь добавлен'}
    except ValueError:
        return {'message': 'Ошибка добавления'}


@users_router.delete('/users/{user_id}/{course_id}')
def dismiss(course_id, user_id, session=Depends(get_session)):
    try:
        user_service.dismiss(course_id, user_id, session)
        return {'message': 'Пользователь удален'}
    except ValueError:
        return {'message': 'Ошибка удаления'}
