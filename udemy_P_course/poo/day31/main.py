from tkinter import *
import pandas
import random

time = None
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")

new_dict = data.to_dict(orient="records")
current_card = {}


def new_word():
    global current_card
    current_card = random.choice(new_dict)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=current_card["French"])
    canvas.itemconfig(card_bacground, image=card_front)
    canvas.itemconfig(title, fill="black")
    canvas.itemconfig(word, fill="black")
    # start_count(3)

def flip_card():
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=current_card["English"])
    canvas.itemconfig(card_bacground, image=card_back)
    canvas.itemconfig(title, fill="white")
    canvas.itemconfig(word, fill="white")

window = Tk()
window.after(3000, func=flip_card)

window.title("Boss")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
# card_bacground = canvas.create_image(400, 263, image=card_back)
card_bacground = canvas.create_image(400, 263, image=card_front)

# Text
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


cancel_image = PhotoImage(file="images/wrong.png")
yes_image = PhotoImage(file="images/right.png")

# Button
rigth_butoon = Button(image=yes_image, highlightthickness=0, command=new_word)
rigth_butoon.grid(column=1, row=1)
wrong_button = Button(image=cancel_image, highlightthickness=0, command=new_word)
wrong_button.grid(column=0, row=1)




canvas.grid(column=0, row=0, columnspan=2)



new_word()

# while True:
#     window.after(2000, test)
window.mainloop()
