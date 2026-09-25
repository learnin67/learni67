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

