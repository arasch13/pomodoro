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
CHECK_MARK = "🗸"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    topic.config(text="Timer", font=(FONT_NAME, 20, "bold"), fg = GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_nr = 0
    checkmarks.config(text=[CHECK_MARK for i in range(checkmark_nr)])

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    if reps != 0 and reps % 7 == 0:
        topic.config(text="Long Break", font=(FONT_NAME, 20, "bold"), fg = RED)
        count_minutes = LONG_BREAK_MIN
    elif reps % 2 == 0:
        topic.config(text="Work", font=(FONT_NAME, 20, "bold"), fg = GREEN)
        count_minutes = WORK_MIN
    else:
        topic.config(text="Short Break", font=(FONT_NAME, 20, "bold"), fg = PINK)
        count_minutes = SHORT_BREAK_MIN
    work_sec = count_minutes * 60
    count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps, timer

    remain_min = math.floor(count / 60)
    remain_sec = int(count % 60)
    if remain_min < 10:
        remain_min = f"0{remain_min}"
    if remain_sec < 10:
        remain_sec = f"0{remain_sec}"
    canvas.itemconfig(timer_text, text=f"{remain_min}:{remain_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        reps += 1
        checkmark_nr = math.ceil(reps / 2)
        checkmarks.config(text=[CHECK_MARK for i in range(checkmark_nr)])
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# show topic
topic = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
topic.grid(column=1, row=0)

# show tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# create buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# show check marks
checkmark_nr = math.ceil(reps/2)
checkmarks = Label(text=[CHECK_MARK for i in range(checkmark_nr)], fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmarks.grid(column=1, row=3)

window.mainloop()