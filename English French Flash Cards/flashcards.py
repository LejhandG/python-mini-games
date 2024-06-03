import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
#RANDOM WORD
df = pandas.read_csv("data/french_words.csv")
words_dict = df.to_dict(orient="records")

random_word = {}


def random_word_generator():
    global random_word
    random_word = random.choice(words_dict)
    language_label.config(text="French")
    word_label.config(text=random_word["French"])
    window.after(3000, flip_card)


def flip_card():
    global random_word
    language_label.config(text="English")
    word_label.config(text=random_word["English"])


def is_known():
    words_dict.remove(random_word)
    random_word_generator()


not_known = {}


def is_not_known():
    global not_known
    not_known[random_word["French"]] = random_word["English"]
    words_dict.remove(random_word)
    print(not_known)
    random_word_generator()


#UI
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=flash_card_image)
canvas.grid(row=0, column=0, columnspan=2)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=is_not_known)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
language_label = Label(text="French", font=("Arial", 40, "italic"), bg="white")
language_label.place(x=400, y=150, anchor=CENTER)
word_label = Label(text="", font=("Arial", 60, "bold"), bg="white")
word_label.place(x=400, y=263, anchor=CENTER)

random_word_generator()


def save_not_known_to_csv():
    pandas.DataFrame(not_known.items(), columns=['French', 'English']).to_csv('data/not_known.csv', index=False)


window.bind('<Destroy>', lambda e: save_not_known_to_csv())

window.mainloop()
