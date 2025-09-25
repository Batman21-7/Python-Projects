# ----------------------------------------Importing Modules-------------------------------------------------- #
from tkinter import *
import random
import pandas as pd

# ------------------------------Import Data and Convert to Dictionary---------------------------------------- #
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
data = df.to_dict(orient="records")
current_card = {}

# --------------------------------------------Constants------------------------------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"


# --------------------------------------------Functions------------------------------------------------------ #
def next_card():
    global flip_timer, current_card
    current_card = random.choice(data)
    window.after_cancel(flip_timer)

    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, flip)


def flip():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def right():
    data.remove(current_card)
    next_card()


# -------------------------------------------------UI-------------------------------------------------------- #

# Window
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Images
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
tick = PhotoImage(file="./images/right.png")
cross = PhotoImage(file="./images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="French", font=("Times New Roman", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", font=("Times New Roman", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button = Button(image=cross, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
correct_button = Button(image=tick, highlightthickness=0, command=right)
correct_button.grid(row=1, column=1)

# ------------------------------------------End Calls---------------------------------------------- #
flip_timer = window.after(3000, flip, 0)
next_card()
window.mainloop()

# ------------------------------------------Store data--------------------------------------------- #
df = pd.DataFrame(data)
df.to_csv("data/words_to_learn.csv", index=False)
