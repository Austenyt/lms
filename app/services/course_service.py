from sqlalchemy import select
from app.models.course import Course


class CourseService:

    def get_all(self, session):
        return session.scalars(select(Course)).all()

    def create(self, name, qty, session):
        course = Course(
            name=name,
            qty=qty
        )
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

    def find(self, id, session):
        course = session.get(Course, id)
        if course is None:
            raise ValueError("id не найден")
        return course

    def delete(self, id, session):
        course = self.find(id, session)
        session.delete(course)
        session.commit()

    def rename(self, id, name, session):
        course = self.find(id, session)
        course.name = name
        session.commit()

    def change_qty(self, id, qty, session):
        course = self.find(id, session)
        course.qty = qty
        session.commit()


course_service = CourseService()
"""
class CourseService:
    def __init__(self, courses):
        self.courses = courses

    def get_all(self):
        return self.courses

    def create(self, id, name, qty):
        course = {"id": id, "name": name, "qty": qty}
        self.courses.append(course)

    def find(self, id):
        for course in self.courses:
            if course["id"] == id:
                return course
        raise ValueError("id не найден")

    def delete(self, id):
        course = self.find(id)
        self.courses.remove(course)

    def rename(self, id, name):
        course = self.find(id)
        course["name"] = name

    def change_qty(self, id, qty):
        course = self.find(id)
        course["qty"] = qty


course_1 = [
    {"id": 1, "name": "Python", "qty": 10},
    {"id": 2, "name": "Java", "qty": 20},
    {"id": 3, "name": "C++", "qty": 30},
    {"id": 4, "name": "Ruby", "qty": 40},
    {"id": 5, "name": "php", "qty": 50}
]
course_service = CourseService(course_1)
"""
