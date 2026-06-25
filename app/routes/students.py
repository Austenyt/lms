from fastapi import APIRouter, Depends
from app.schemas.student import StudentFind, StudentCreate, StudentPatch
from app.services.student_service import student_service
from app.db.database import get_session

students_router = APIRouter(tags=['students'])


@students_router.get('/students')
def students(session=Depends(get_session)):
    return student_service.get_all(session)


@students_router.post('/students/{id}')
def find(payload: StudentFind, session=Depends(get_session)):
    try:
        return student_service.find(payload.id, session)
    except ValueError:
        return {'message': "Такого студента нет"}


@students_router.post('/students')
def create(payload: StudentCreate, session=Depends(get_session)):
    student = student_service.create(payload, session)
    return {'message': f"Студент {student.last_name} добавлен"}


@students_router.patch('/students/{id}')
def patch(payload: StudentPatch, session=Depends(get_session)):
    student_service.patch(payload, session)
    return {'message': 'ok'}


@students_router.delete('/students/{id}')
def delete(payload: StudentFind, session=Depends(get_session)):
    try:
        student_service.find(payload.id, session)
        return {'message': "Удаление успешно"}
    except ValueError:
        return {'message': 'Ошибка'}
