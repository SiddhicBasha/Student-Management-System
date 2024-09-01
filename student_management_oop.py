class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, student_id, name, age, grade):
        super().__init__(name, age)
        self._student_id = student_id
        self._grade = grade

    @property
    def student_id(self):
        return self._student_id

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, {super().__str__()}, Grade: {self.grade}"


class StudentManagementSystem:
    def __init__(self):
        self._students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self._students:
            print(f"Student with ID {student_id} already exists.")
        else:
            student = Student(student_id, name, age, grade)
            self._students[student_id] = student
            print(f"Student {name} added successfully.")

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id in self._students:
            student = self._students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            print(f"Student ID {student_id} updated successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_student(self, student_id):
        if student_id in self._students:
            del self._students[student_id]
            print(f"Student ID {student_id} deleted successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def view_student(self, student_id):
        if student_id in self._students:
            print(self._students[student_id])
        else:
            print(f"Student with ID {student_id} not found.")

    def view_all_students(self):
        if not self._students:
            print("No students found.")
        else:
            for student in self._students.values():
                print(student)


class StudentManagementInterface:
    def __init__(self):
        self.sms = StudentManagementSystem()

    def run(self):
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. Update Student")
            print("3. Delete Student")
            print("4. View Student")
            print("5. View All Students")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.update_student()

            elif choice == "3":
                self.delete_student()

            elif choice == "4":
                self.view_student()

            elif choice == "5":
                self.view_all_students()

            elif choice == "6":
                print("Exiting Student Management System.")
                break

            else:
                print("Invalid choice, please try again.")

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        grade = input("Enter Student Grade: ")
        self.sms.add_student(student_id, name, age, grade)

    def update_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter new name (leave blank to skip): ")
        age = input("Enter new age (leave blank to skip): ")
        grade = input("Enter new grade (leave blank to skip): ")
        self.sms.update_student(student_id, name if name else None, age if age else None, grade if grade else None)

    def delete_student(self):
        student_id = input("Enter Student ID: ")
        self.sms.delete_student(student_id)

    def view_student(self):
        student_id = input("Enter Student ID: ")
        self.sms.view_student(student_id)

    def view_all_students(self):
        self.sms.view_all_students()


if __name__ == "__main__":
    interface = StudentManagementInterface()
    interface.run()
