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
        return

    def delete(self, id):
        course = self.find(id)
        if course is None:
            print("Такого элемента нет")
            return
        self.courses.remove(course)


    def rename(self, id):
        pass

    def change_qty(self, id, qty):
        pass


course_1 = [
    {"id": 1, "name": "Python", "qty": 10},
    {"id": 2, "name": "Java", "qty": 20},
    {"id": 3, "name": "C++", "qty": 30},
    {"id": 4, "name": "Ruby", "qty": 40},
    {"id": 5, "name": "php", "qty": 50}
]
course_service = CourseService(course_1)
# print(course_service.find(6))
course_service.delete(4)
print(course_service.get_all())
