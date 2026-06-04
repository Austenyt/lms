from fastapi import APIRouter, Depends
from app.db.database import get_session
from app.schemas.lesson import LessonFind, LessonCreate, LessonPatch
from app.services.lesson_service import lesson_service

lessons_router = APIRouter(tags=['lessons'])

@lessons_router.get('/lessons')
def lessons(session=Depends(get_session)):
    return lesson_service.get_all(session)

@lessons_router.post('/lessons/{id}')
def find(payload: LessonFind, session=Depends(get_session)):
    try:
        return lesson_service.find(payload.id, session)
    except ValueError:
        return {'message': 'Урока с таким id не существует'}


@lessons_router.post('/lessons')
def create(payload: LessonCreate, session=Depends(get_session)):
    lesson = lesson_service.create(payload, session)
    return {'message': f'Урок {lesson.id} добавлен'}


@lessons_router.post('/lessons/{id}')
def patch(payload: LessonPatch, session=Depends(get_session)):
    lesson_service.patch(payload, session)
    return {'message': 'ok'}

