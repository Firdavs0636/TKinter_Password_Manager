import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    # Takes random number of letters, characters and numbers from the lists above and assigns to a new list
    password_list += [choice(letters) for a in range(randint(8, 10))]
    password_list += [choice(symbols) for b in range(randint(2, 4))]
    password_list += [choice(numbers) for c in range(randint(2, 4))]
    # Shuffles the assigned string from a list
    shuffle(password_list)
    # Assigns shuffled string to a new variable without any space or braces
    password = "".join(password_list)
    # Clears everything inside password entry
    password_input.delete(0, END)
    re_entry_password_input.delete(0, END)
    # Inserts a password inside a password entry
    password_input.insert(0, password)
    re_entry_password_input.insert(0, password)
    # COPIES the password to a clipboard that is easy to PASTE
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Gets variables from Entries
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website:
            {
                'email': email,
                'password': password
            }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops!", message="You're missing some values!")
    elif check_password():
        messagebox.showwarning(title="WARNING!", message="Your password is not compatible!")
    else:
        try:
            with open("passwords.json", mode='r') as file:
                # Reads old data and saves as a dictionary
                updated = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", mode='w') as file:
                # Writes an updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updates an old data
            updated.update(new_data)

            with open("passwords.json", mode='w') as file:
                # Writes an updated data
                json.dump(updated, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            re_entry_password_input.delete(0, END)


# ---------------------------- CHECK PASSWORD COMPATIBILITY  ------------------------------- #
def check_password():
    if password_input.get() != re_entry_password_input.get():
        return True


# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas, Photo Setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
image1 = PhotoImage(file='./Pics/logo.png')
canvas.create_image(100, 100, image=image1)
canvas.grid(column=1, row=0)

# Label Setup
website_label = Label(text='Website:')
website_label.grid(column=0, row=1, sticky=W)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2, sticky=W)

first_password_label = Label(text='Password:')
first_password_label.grid(column=0, row=3, sticky=W)

second_password_label = Label(text='Re-enter the Password:')
second_password_label.grid(column=0, row=4, sticky=W)


# Input Entry
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_username_input = Entry(width=39)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(END, 'example@mail.com')

password_input = Entry(width=21, textvariable='Password', show='*')
password_input.grid(column=1, row=3)

re_entry_password_input = Entry(width=21, textvariable='Re-enter Password', show='*')
re_entry_password_input.grid(column=1, row=4)


# Buttons
search_bt = Button(text='Search', command=None)
search_bt.grid(column=2, row=1)

generate_bt = Button(text='Generate Password', command=generate_password)
generate_bt.grid(column=2, row=3)

add_bt = Button(text='Add', width=37, command=save)
add_bt.grid(column=1, row=5, columnspan=2)


window.mainloop()
