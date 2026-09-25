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
