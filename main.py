import random
from tkinter import *

import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("data/words_to_learn.csv")
    words = df.to_dict(orient="records")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
    words = df.to_dict(orient="records")
word = {}


def new_words():
    global word, flip_timer
    word = random.choice(words)
    window.after_cancel(flip_timer)
    canvas.itemconfig(card, image=card_front_image)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{word['French']}", fill="black")
    flip_timer = window.after(3000, flip_cards, word)


def flip_cards(wo):
    canvas.itemconfig(card, image=back_card_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{wo['English']}", fill="white")


def is_known():
    words.remove(word)
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_words()


window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(0, new_words)

card_front_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")

canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=new_words)
unknown_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

window.mainloop()
