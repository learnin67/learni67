students = []
courses = []
marks = {}

def input_number_of_students():
    global num_students
    num_students = int(input("Enter number of students in the class: "))

def input_student_info():
    for i in range(num_students):
        print("Student " + str(i + 1) + ":")
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student DoB (DD/MM/YYYY): ")
        student = {"id": id, "name": name, "dob": dob}
        students.append(student)

def input_number_of_courses():
    global num_courses
    num_courses = int(input("Enter number of courses: "))

def input_course_info():
    for i in range(num_courses):
        print("Course " + str(i + 1) + ":")
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        course = {"id": id, "name": name}
        courses.append(course)

def input_marks():
    print("Select a course to input marks:")
    for i in range(len(courses)):
        print(str(i + 1) + ". " + courses[i]["name"])
    choice = int(input("Enter your choice: ")) - 1
    course_id = courses[choice]["id"]
    course_name = courses[choice]["name"]

    if course_name not in marks:
        marks[course_name] = {}

    for student in students:
        mark = input("Enter mark for " + student["name"] + " in " + course_name + ": ")
        marks[course_name][student["id"]] = mark

#LISTING FUNCTIONS

def list_courses():
    print("List of courses:")
    for course in courses:
        print("ID: " + course["id"] + ", Name: " + course["name"])

def list_students():
    print("List of students:")
    for student in students:
        print("ID: " + student["id"] + ", Name: " + student["name"] + ", DoB: " + student["dob"])

def show_marks():
    print("Select a course to show marks:")
    for i in range(len(courses)):
        print(str(i + 1) + ". " + courses[i]["name"])
    choice = int(input("Enter your choice: ")) - 1
    course_name = courses[choice]["name"]

    if course_name in marks:
        print("Marks for course: " + course_name)
        for student in students:
            sid = student["id"]
            if sid in marks[course_name]:
                print(student["name"] + ": " + marks[course_name][sid])
            else:
                print(student["name"] + ": No mark")
    else:
        print("No marks available for this course yet.")

# ============ MAIN ============

print("=== Student Mark Management ===")

input_number_of_students()
input_student_info()

input_number_of_courses()
input_course_info()

input_marks()

print("")
list_courses()
print("")
list_students()
print("")
show_marks()