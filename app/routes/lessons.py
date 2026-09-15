from fastapi import APIRouter, Depends, HTTPException, status
from app.db.database import get_session
from app.dependencies import get_current_user_id
from app.schemas.lesson import LessonFind, LessonResponse, LessonCreate, LessonCreateResponse, LessonPatch, \
    LessonPatchResponse
from app.services.lesson_service import lesson_service

lessons_router = APIRouter(tags=['lessons'])


@lessons_router.get('/lessons')
def lessons(session=Depends(get_session)) -> list[LessonResponse]:
    return lesson_service.get_all(session)


@lessons_router.post('/lessons/{id}')
def find(payload: LessonFind, session=Depends(get_session)) -> LessonResponse:
    try:
        return lesson_service.find(payload.id, session)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Урока с таким id не существует")


@lessons_router.post('/lessons')
def create(payload: LessonCreate, session=Depends(get_session), user_id=Depends(get_current_user_id)) -> (
        LessonCreateResponse):
    return lesson_service.create(payload, session, user_id)


@lessons_router.patch('/lessons/{id}')
def patch(payload: LessonPatch, session=Depends(get_session)) -> LessonPatchResponse:
    return lesson_service.patch(payload, session)


@lessons_router.delete('/lessons/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(payload: LessonFind, session=Depends(get_session)):
    try:
        lesson_service.delete(payload.id, session)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Урока с таким id не существует")
