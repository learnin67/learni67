# =========================================================
# THE 3 SIMPLE CLASSES (OOP Core)
# =========================================================

#is this AI heavy ? yes
#do i understand ? yes
#do i want to oop coding ? no
# and i do update my code from original 1b for readability

class Entity:
    """Base class providing shared attributes & methods"""
    def __init__(self, entity_id, name):
        self._id = entity_id      # Encapsulation: '_' hides raw data
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def show(self):
        pass  # Placeholding method for Polymorphism


class Student(Entity):
    def __init__(self, name, student_id, dob):
        super().__init__(student_id, name)
        self._dob = dob

    # Polymorphism: Custom show() method for Student
    def show(self):
        print(f"  {self._name}  |  ID: {self._id}  |  DOB: {self._dob}")


class Course(Entity):
    # Polymorphism: Custom show() method for Course
    def show(self):
        print(f"{self._name}  |  ID: {self._id}")


# =========================================================
# YOUR ORIGINAL CODE (Only dicts changed to objects)
# =========================================================

students = []
courses = []
marks = {}

def number_of_students():
    nos_student = int(input("how many student are there in your class: "))
    for _ in range(nos_student):
        students_info()

def students_info():
    student_name = input("what's your name: ").strip()
    student_id = int(input("what is your student id: "))
    student_dob = input("what your date of birth: ").strip()
    # Changed from dict to Student object
    students.append(Student(student_name, student_id, student_dob))

def number_of_courses():
    nos_course = int(input("how many courses do you have: "))
    for _ in range(nos_course):
        courses_info()

def courses_info():
    course_name = input("what is the course name: ").strip()
    course_id = input("what is the course id: ").strip()
    # Changed from dict to Course object
    courses.append(Course(course_name, course_id))

def input_marks():
    for student in students:
        print(f"\nentering marks for {student.get_name()} (ID: {student.get_id()})")
        marks[student.get_id()] = {}
        for course in courses:
            mark = float(input(f"  mark for {course.get_name()} ({course.get_id()}): "))
            marks[student.get_id()][course.get_id()] = mark

def list_student():
    print("\n--- Students ---")
    for s in students:
        s.show()  # Calls Student's show()

def list_course():
    print("\n--- Courses ---")
    for c in courses:
        c.show()  # Calls Course's show()

def list_mark():
    print("\n--- Marks ---")
    for student in students:
        print(f"{student.get_name()} (ID: {student.get_id()})")
        for course in courses:
            print(f"{course.get_name()}: {marks[student.get_id()][course.get_id()]}")

def main():
    number_of_students()
    number_of_courses()
    input_marks()
    list_student()
    list_course()
    list_mark()

main()
