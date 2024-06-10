import random

import requests
import html
from tkinter import *

response = ""
data = ""
question = ""
answers_array = []
score = 0

def new_question():
    global response, data, question, answers_array
    response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
    data = response.json()
    question = html.unescape(data["results"][0]["question"])
    answers_array = [data["results"][0]["correct_answer"]] + data["results"][0]["incorrect_answers"]
    random.shuffle(answers_array)
    question_label.config(text=question)
    answer_1.config(text=answers_array[0])
    answer_2.config(text=answers_array[1])
    answer_3.config(text=answers_array[2])
    answer_4.config(text=answers_array[3])

def check_answer(answer):
    global score
    if answer == data["results"][0]["correct_answer"]:
        print("True")
        score += 1
        question_label.config(bg="green")
        question_label.after(1000, lambda: question_label.config(bg="white"))
        score_label.config(text=f"Score: {score}")
        new_question()
    else:
        print("False")
        question_label.config(bg="red")
        question_label.after(1000, lambda: question_label.config(bg="white"))
        new_question()

window = Tk()
window.title("Trivia Quiz")
window.minsize(width=400, height=600)
window.config(bg="#304855")

score_label = Label(window, text=f"Score: {score}", justify=CENTER, bg="#304855", fg="white",
                    font=("Arial", 20, "bold"))
score_label.place(relx=0.8, rely=0.05, anchor=CENTER)

question_label = Label(window, text="", bg="white", font=("Arial", 22, "italic"), wraplength=350, justify=CENTER)
question_label.place(relx=0.5, rely=0.35, anchor=CENTER)

answer_1 = Button(text="", justify=CENTER, wraplength=80, command=lambda: check_answer(answers_array[0]))
answer_1.place(relx=0.2, rely=0.7, anchor=CENTER)

answer_2 = Button(text="", justify=CENTER, wraplength=80, command=lambda: check_answer(answers_array[1]))
answer_2.place(relx=0.8, rely=0.7, anchor=CENTER)

answer_3 = Button(text="", justify=CENTER, wraplength=80, command=lambda: check_answer(answers_array[2]))
answer_3.place(relx=0.2, rely=0.8, anchor=CENTER)

answer_4 = Button(text="", justify=CENTER, wraplength=80, command=lambda: check_answer(answers_array[3]))
answer_4.place(relx=0.8, rely=0.8, anchor=CENTER)

new_question()

window.mainloop()