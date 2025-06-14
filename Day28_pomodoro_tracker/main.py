import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_session = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer_session)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer.config(text="Timer", font=(FONT_NAME, 50), fg='GREEN', bg=YELLOW)
    click.config(text = "")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        timer.config(text="Long Break", font=(FONT_NAME, 50), fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer.config(text="Break", font=(FONT_NAME, 50), fg=PINK)
    else:
        count_down(work_secs)
        timer.config(text="Work", font=(FONT_NAME, 50), fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer_session
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    if count_min < 10:
        count_min = f'0{count_min}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer_session = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        click.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Anish")
window.config(padx=100, pady=100, bg=YELLOW)
window.config()

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
filename = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=filename)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", font=(FONT_NAME, 50), fg='GREEN', bg=YELLOW)
timer.grid(column=1, row=0)

start = Button(text="start", font=('Arial', 9, 'bold'), command=start_timer)
start.grid(column=0, row=2)

end = Button(text="end", font=('Arial', 9, 'bold'), command=reset_timer)
end.grid(column=2, row=2)

click = Label(font=('Arial', 9, 'bold'), fg='GREEN', bg=YELLOW)
click.grid(column=1, row=4)

window.mainloop()
