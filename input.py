def input_number_of_students():
    global num_students
    new_screen(" INPUT STUDENTS ")
    num_students = int(ask("Enter number of students in the class: "))

def input_student_info():
    for i in range(num_students):
        show("Student " + str(i + 1) + ":")
        id = ask("  Enter student id: ")
        name = ask("  Enter student name: ")
        dob = ask("  Enter student DoB (DD/MM/YYYY): ")
        student = {"id": id, "name": name, "dob": dob}
        students.append(student)

def input_number_of_courses():
    global num_courses
    new_screen(" INPUT COURSES ")
    num_courses = int(ask("Enter number of courses: "))

def input_course_info():
    for i in range(num_courses):
        show("Course " + str(i + 1) + ":")
        id = ask("  Enter course id: ")
        name = ask("  Enter course name: ")
        credit = int(ask("  Enter course credit: "))    
        course = {"id": id, "name": name, "credit": credit}
        courses.append(course)

def input_marks():
    new_screen(" INPUT MARKS ")
    show("Select a course to input marks:")
    for i in range(len(courses)):
        show(str(i + 1) + ". " + courses[i]["name"])
    choice = int(ask("Enter your choice: ")) - 1
    course_id = courses[choice]["id"]
    course_name = courses[choice]["name"]

    if course_name not in marks:
        marks[course_name] = {}

    for student in students:
        raw = float(ask("Enter mark for " + student["name"] + " in " + course_name + ": "))
        mark = math.floor(raw * 10) / 10        
        marks[course_name][student["id"]] = mark
        show("  -> saved as " + str(mark))

