import json
import math
import random
import tkinter
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    return password


def populate_password():
    password_data.delete(0, END)
    generated_password = generate_password()
    password_data.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    print("Data saved")
    website_name = input_data.get()
    email = email_user_input.get()
    pwd = password_data.get()

    if website_name != '' and pwd != '':

        is_ok = messagebox.askyesno("Saving into the file", f"Data saved {email} and {website_name}. Save okay?")

        if is_ok:
            with open("data.txt", "a+") as file:
                file.write(f"{website_name}  |  {email}  |  {pwd}\n")

            input_data.delete(0, tkinter.END)
            email_user_input.delete(0, tkinter.END)
            password_data.delete(0, tkinter.END)
    else:
        messagebox.showerror("Error", "Website name and Password should not be empty")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.config()

canvas = Canvas(width=200, height=200, highlightthickness=0)
filename = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=filename)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=('Arial', 9, 'bold'))
website_label.grid(row=1, column=0)

email_user_label = Label(text="Email/Username:", font=('Arial', 9, 'bold'))
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=('Arial', 9, 'bold'))
password_label.grid(row=3, column=0)

# Input Textbox
input_data = Entry(width=35)
input_data.grid(column=1, row=1, columnspan=2)
input_data.focus()

email_user_input = Entry(width=35)
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(1, "anish.alwekar@gmail.com")

password_data = Entry(width=21)
password_data.grid(column=1, row=3)
password_data.insert(1, generate_password())

# Buttons

gen_pass = Button(text="Generate", font=('Arial', 9, 'bold'), command=populate_password)
gen_pass.grid(column=2, row=3)

add = Button(text="Add", font=('Arial', 9, 'bold'), width=36, command=save_data)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
