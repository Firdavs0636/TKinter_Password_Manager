from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("passwords.txt", mode='a') as file:
        file.write(website_input.get())



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


password_input = Entry(width=21)
password_input.grid(column=1, row=3)


# Buttons
generate_bt = Button(text='Generate Password')
generate_bt.grid(column=2, row=3)


add_bt = Button(text='Add', width=37)
add_bt.grid(column=1, row=4, columnspan=2)






window.mainloop()
