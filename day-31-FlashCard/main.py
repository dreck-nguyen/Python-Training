import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    flash_card.itemconfig(card_title, text="French", fill="black")
    flash_card.itemconfig(card_word, text=current_card["French"], fill="black")
    flash_card.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    flash_card.itemconfig(card_title, text="English", fill="white")
    flash_card.itemconfig(card_word, text=current_card["English"], fill="white")
    flash_card.itemconfig(card_background, image=card_back_img)

def is_know():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


flash_card = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

card_background = flash_card.create_image(400, 263, image=card_front_img)

card_title = flash_card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = flash_card.create_text(400, 263, text="Word", font=("Ariel", 40, "bold  "))
flash_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card.grid(row=0, column=0, columnspan=2)




tick_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=tick_img, highlightthickness=0, command=is_know)
correct_button.grid(row=1,column=1)

cross_img = PhotoImage(file="./images/wrong.png")
incorrect_button = Button(image=cross_img, highlightthickness=0, command=next_card)
incorrect_button.grid(row=1, column=0)

next_card()



window.mainloop()