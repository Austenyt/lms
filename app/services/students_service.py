class StudentsService:
    def __init__(self, students):
        self.students = students

    def get_all(self):
        return self.students

    def create(self, id, name, age):
        student = {"id": id, "name": name, "age": age}
        self.students.append(student)

    def find(self, id):
        for student in self.students:
            if student["id"] == id:
                return student
        return

    def delete(self, id):
        student = self.find(id)
        if student is None:
            print("Такого элемента нет")
            return
        self.students.remove(student)

    def rename(self, id, name):
        student = self.find(id)
        if student is None:
            print("Такого элемента нет")
            return
        student["name"] = name

    def change_age(self, id, age):
        student = self.find(id)
        if student is None:
            print("Такого элемента нет")
            return
        student["age"] = age


students_1 = [
    {"id": 1, "name": "Body_1", "age": 10},
    {"id": 2, "name": "Body_2", "age": 20},
    {"id": 3, "name": "Body_3", "age": 30},
    {"id": 4, "name": "Body_4", "age": 40},
    {"id": 5, "name": "Body_5", "age": 50}
]
students_service = StudentsService(students_1)
print(students_service.get_all())
