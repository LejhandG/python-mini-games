import json
import random
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
CAPITAL_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
SMALL_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|',
                      ':', ';', '<', '>', '?']
OPTIONS = [CAPITAL_LETTERS, SMALL_LETTERS, NUMBERS, SPECIAL_CHARACTERS]


def password_generator():
    password_string = ""
    for _ in range(0, 15):
        password_string += random.choice(OPTIONS[random.randint(0, 3)])
    password_entry.delete(0, END)
    password_entry.insert(0, password_string)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if password_entry.get() == "" or email_entry.get() == "" or website_entry.get() == "":
        popup_window = Toplevel()
        popup_window.title("Empty Field")
        wrong_entry_label = Label(popup_window, text="Please fill all of the fields", font=("arial", 32, "bold"))
        wrong_entry_label.pack()
    else:
        popup_window = Toplevel()
        popup_window.title("Confirm Details")
        confirm_details_label = Label(popup_window, text="Confirm the details", font=("arial", 32, "bold"))
        details_label = Label(popup_window,
                              text=f"Website: {website_entry.get()}\nEmail/Username: {email_entry.get()}\nPassword: {password_entry.get()}")
        confirm_button = Button(popup_window, text="Confirm", command=lambda: file_write_password(popup_window))
        confirm_details_label.pack()
        details_label.pack()
        confirm_button.pack()


def file_write_password(popup_window):
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }

    filename = "saved_password.json"

    try:
        with open(filename, "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
    except json.JSONDecodeError:
        data = new_data

    with open(filename, "w") as data_file:
        json.dump(data, data_file, indent=4)

    popup_window.destroy()
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    with open("saved_password.json") as file:
        data = json.load(file)
        if website_entry.get() == "":
            prompt = Toplevel()
            prompt.title("Empty Field")
            display = Label(prompt, text="Don't leave field empty")
            display.pack()
        elif website in data:
            prompt = Toplevel()
            prompt.title("Display Password")
            display = Label(prompt,
                            text=f"Website: {website_entry.get()}\nUsername/Email: {data[website]["email"]}\nPassword: {data[website]["email"]}")
            display.pack()
        else:
            prompt = Toplevel()
            prompt.title("Error 404")
            display = Label(prompt, text="Didn't find any entry")
            display.pack()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
email_label = Label(text="Email/Username: ")
password_label = Label(text="Password: ")
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
password_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=14, command=find_password)
generate_pass_button = Button(text="Generate Password", width=14, command=password_generator)
add_button = Button(text="Add", width=36, command=save_password)
search_button.grid(row=1, column=2)
generate_pass_button.grid(row=3, column=2)
add_button.grid(row=4, column=1)

window.mainloop()
