import random
import re
import smtplib
from tkinter import *
import datetime
import time

window = Tk()
window.title("OTP Authentication")
window.minsize(width=675, height=350)
window.config(bg="white")

ff_logo = PhotoImage(file="assets/logo-no-background.gif", width=200, height=153)
canvas = Canvas(window, width=210, height=164, highlightthickness=0, background="white")
canvas.create_image(105, 83, image=ff_logo)
canvas.pack()
otp_auth_label = Label(text="OTP Authentication", font=("Arial", 32, "bold"), pady=20, highlightthickness=0, bg="white")
otp_auth_label.pack()
email_entry = Entry()
email_entry.insert(0, "Email")
email_entry.pack()
my_email = "youremail@gmail.com"
password = "email_app_password" #Google search how to get gmail app password and insert here
attempts = 3


def send_email():
    random_otp = random.randint(1000, 9999)
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    email = email_entry.get()
    if re.fullmatch(regex, email):
        subject = f"{random_otp} is OTP to access FifthFortune"
        body = f"Dear FifthFortune user,\nYour FifthFortune Account (Email ID {email}) One Time PIN is: {random_otp}, and is valid for 2 minutes.\n\n(Generated at {datetime.datetime.now()})\n\n********************************\nThis is an auto-generated email. Do not reply to this email."
        msg = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=msg.encode('utf-8')
            )
        popup = Toplevel()
        popup.title("OTP Auth")
        label = Label(popup, text="Enter OTP", font=("Arial", 24, "bold"), pady=30)
        label.pack()
        entry = Entry(popup)
        entry.pack()

        def validate_otp():
            if int(entry.get()) == random_otp:
                popup.destroy()
                validated = Toplevel()
                validated_text = Label(validated, text="OTP Validated. You can now close the window",
                                       font=("Arial", 24, "bold"))
                validated_text.pack()
            else:
                not_validated = Toplevel()
                global attempts
                if attempts != 1:
                    attempts -= 1
                    not_validated_text = Label(not_validated, text=f"Wrong OTP. {attempts} attempts left!",
                                               font=("Arial", 24, "bold"))
                    not_validated_text.pack()
                else:
                    popup.destroy()

        button = Button(popup, text="Validate", command=validate_otp)
        button.pack(pady=20)

        timer_label = Label(popup, text="Time remaining: 2:00", font=("Arial", 18, "bold"))
        timer_label.pack()
        def countdown(count):
            minutes, seconds = divmod(count, 60)
            timer_label.config(text=f"Time remaining: {minutes:02d}:{seconds:02d}")
            if count > 0:
                popup.after(1000, countdown, count-1)
            else:
                popup.destroy()
        countdown(120)

    else:
        popup = Toplevel()
        popup.title("Re-enter Email")
        label = Label(popup, text="Enter a valid email address", font=("Arial", 24, "bold"))
        label.pack()


otp_button = Button(text="Receive OTP", command=send_email)
otp_button.pack(pady=20)
window.mainloop()