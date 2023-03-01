from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops!", message="You're missing some values!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Information details: \nEmail: {email} \nPassword: {password} '
                                                              f'\nPress OK if you want to save!')

        if is_ok:
            with open("passwords.txt", mode='a') as file:
                file.write(f'{website} | {email} | {password}\n')
            website_input.delete(0, END)
            password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
# Window Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas, Photo Setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
image1 = PhotoImage(file='/Users/admin/PycharmProjects/TKinter_Password_Manager/Pics/logo.png')
canvas.create_image(100, 100, image=image1)
canvas.grid(column=1, row=0)

# Label Setup
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)


email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)


password_label = Label(text='Password:')
password_label.grid(column=0, row=3)


# Input Entry
website_input = Entry(width=39)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()


email_username_input = Entry(width=39)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(END, 'example@mail.com')


password_input = Entry(width=21, textvariable='Password', show='*')
password_input.grid(column=1, row=3)


# Buttons
generate_bt = Button(text='Generate Password')
generate_bt.grid(column=2, row=3)


add_bt = Button(text='Add', width=37, command=save)
add_bt.grid(column=1, row=4, columnspan=2)






window.mainloop()
