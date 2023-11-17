from tkinter import *
import math

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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    tittle.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_seconds = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break)
        tittle.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        tittle.config(text="Break", fg=PINK)

    else:
        count_down(work_seconds)
        tittle.config(text="Work", fg=GREEN)
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        check_mark.config(text=mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tittle = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
tittle.grid(column=1, row=0)

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", bg="white", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg="white", command=timer_reset)
reset.grid(column=2, row=2)

check_mark = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=4)

window.mainloop()
