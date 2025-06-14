import json
import math
import random
import tkinter
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
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

    #print(f"Your password is: {password}")
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

    new_dict = {

        website_name: {

            "email": email,
            "password": pwd
        }}

    if website_name != '' and pwd != '':

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # If file doesn't exist, create a new one
            data = {}

        data.update(new_dict)

        with open("data.json", "w") as data_file:
            # Write or dump the updated data
            json.dump(data, data_file, indent= 4)


        input_data.delete(0, tkinter.END)
        password_data.delete(0, tkinter.END)
    else:
        messagebox.showerror("Error", "Website name and Password should not be empty")

#--------------------------------Search Data---------------------------------------#

def find_password():
    website_name = input_data.get()
    if len(website_name) == 0:
        messagebox.showerror("Error", "Website name should not be empty")
    else:

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

                if len(data) != 0:
                    flag = True
                    for item in data.keys():
                        if item == website_name:
                            flag = False
                            item_email = data[item]['email']
                            item_pwd = data[item]['password']
                            messagebox.showinfo(item, f"Email: {item_email}\n Password: {item_pwd}")
                    if flag:
                        messagebox.showinfo("Search", "No entry found for the given website")

                else:
                    messagebox.showerror("Error", "No entries in the file please create the file and add the entries")


        except FileNotFoundError:
            messagebox.showerror("Error", "No file Data found!!")






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


add = Button(text="Search", font=('Arial', 9, 'bold'), width=8, command=find_password)
add.grid(column=2, row=1)

window.mainloop()
