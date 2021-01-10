from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    entry_pw.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_site.get()
    email = entry_email.get()
    password = entry_pw.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Filed(s) Empty!", message="Bitte lass keines der Felder leer!")
    else:
        proceed = messagebox.askokcancel(title=website,
                                         message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n"
                                                 f"\n Wanna Save?")
        if proceed:
            with open("/Users/a/Documents/Data/data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                entry_site.delete(0, END)
                entry_email.delete(0, END)
                entry_pw.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=2, row=1)

# internal Widgets

label_site = Label(text='Website:')
label_site.grid(row=2, column=1)

label_email = Label(text="Email/Username:")
label_email.grid(row=3, column=1)

label_pw = Label(text="Password:")
label_pw.grid(row=4, column=1)

entry_site = Entry(width=35)
entry_site.grid(row=2, column=2, columnspan=2)
entry_site.focus()

entry_email = Entry(width=35)
entry_email.grid(row=3, column=2, columnspan=2)
entry_email.insert(0, "")

entry_pw = Entry(width=21)
entry_pw.grid(row=4, column=2)

gen_pw_btn = Button(text="Generate Password", command=generate_password)
gen_pw_btn.grid(row=4, column=3)

add_btn = Button(text="ADD", width=36, command=save)
add_btn.grid(row=5, column=2, columnspan=2)

window.mainloop()
