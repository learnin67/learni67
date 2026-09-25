import curses
import math
import numpy as np

students = []
courses = []
marks = {}

num_students = 0
num_courses = 0

screen = None     
y = 0            

#CURSES

def new_screen(title):
    global y
    screen.clear()
    screen.border(0)
    screen.addstr(0, 2, title)        
    y = 2

def show(text):
    global y
    try:
        screen.addstr(y, 2, text)
    except curses.error:             
        pass
    y = y + 1
    screen.refresh()

def ask(prompt):
    global y
    screen.addstr(y, 2, prompt)
    screen.refresh()
    answer = screen.getstr(y, 2 + len(prompt)).decode()
    y = y + 1
    return answer

def pause():
    show("")
    show("Press any key to continue...")
    screen.getch()


#INPUT 

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


#LISTING
def list_courses():
    new_screen(" LIST COURSES ")
    show("List of courses:")
    for course in courses:
        show("  ID: " + course["id"] + ", Name: " + course["name"] +
             ", Credit: " + str(course["credit"]))
    pause()

def list_students():
    new_screen(" LIST STUDENTS ")
    show("List of students:")
    for student in students:
        show("  ID: " + student["id"] + ", Name: " + student["name"] +
             ", DoB: " + student["dob"])
    pause()

def show_marks():
    new_screen(" SHOW MARKS ")
    show("Select a course to show marks:")
    for i in range(len(courses)):
        show(str(i + 1) + ". " + courses[i]["name"])
    choice = int(ask("Enter your choice: ")) - 1
    course_name = courses[choice]["name"]

    if course_name in marks:
        show("Marks for course: " + course_name)
        for student in students:
            sid = student["id"]
            if sid in marks[course_name]:
                show("  " + student["name"] + ": " + str(marks[course_name][sid]))
            else:
                show("  " + student["name"] + ": No mark")
    else:
        show("No marks available for this course yet.")
    pause()


#NUMPY 

def calc_gpa(student_id):
    credits = []
    scores = []
    for course in courses:
        cname = course["name"]
        if cname in marks and student_id in marks[cname]:
            credits.append(course["credit"])
            scores.append(marks[cname][student_id])
    if len(credits) == 0:
        return 0.0
    credits = np.array(credits)
    scores = np.array(scores)
    return np.sum(credits * scores) / np.sum(credits)

def show_gpa():
    new_screen(" SHOW GPA ")
    show("Select a student to show GPA:")
    for i in range(len(students)):
        show(str(i + 1) + ". " + students[i]["name"])
    choice = int(ask("Enter your choice: ")) - 1
    student = students[choice]
    show("Average GPA of " + student["name"] + ": " + str(round(calc_gpa(student["id"]), 2)))
    pause()

def sort_students_by_gpa():
    global students
    gpas = np.array([calc_gpa(s["id"]) for s in students])
    order = np.argsort(gpas)[::-1]             
    students = [students[i] for i in order]
    new_screen(" SORT BY GPA ")
    show("Students sorted by GPA descending:")
    for i in range(len(students)):
        show("  #" + str(i + 1) + " " + students[i]["name"] +
             " - GPA: " + str(round(calc_gpa(students[i]["id"]), 2)))
    pause()


#MAIN 

def main(stdscr):
    global screen
    screen = stdscr
    curses.curs_set(1)

    new_screen(" STUDENT MARK MANAGEMENT ")
    show("Hello! Press any key to start...")
    screen.getch()

    input_number_of_students()
    input_student_info()

    input_number_of_courses()
    input_course_info()

    input_marks()

    list_courses()
    list_students()
    show_marks()

    show_gpa()               
    sort_students_by_gpa()   

    new_screen(" BYE ")
    show("Done! Bye bye :)")
    screen.getch()


curses.wrapper(main)
