from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    website = website_entry.get()
    email = email_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump("", data_file, indent=4)
    else:
        if website in data.keys():
            try:
                email_info = data[website]["email"]
                password_info = data[website]["password"]
            except KeyError:
                messagebox.showinfo(title="Oops", message="Error Occur")
            else:
                if email.lower() == str(email_info).lower():
                    messagebox.showinfo(title="Information",
                                        message=f"Your Email : {email_info}\nPassword : {password_info}")
                else:
                    messagebox.showinfo(title="Oops", message="Email/Username is not correct")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists .")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', ]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '&', '(', ')', '+']


def gen_password():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += str(char)
    password = "".join(str(letter) for letter in password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) > 0 and len(email) > 0 and len(password) > 0:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        # with open("data.json", mode="r") as data_file:
        #
        #     data = json.load(data_file)
        #
        #     data.update(new_data)

        # with open("data.json", mode="w") as data_file:
        #
        #     json.dump(new_data, data_file, indent=4)


    else:
        messagebox.showinfo(title="Oops", message="Invalid information. Empty field(s)")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")

window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dev.mail.testforsend@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", command=search_website)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=gen_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
