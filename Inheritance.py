from traceback import print_tb


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_student_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        self.show_info()

s = Student("Alice", 20, "S1234")
s.show_student_info()
