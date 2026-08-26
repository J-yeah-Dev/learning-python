import json
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get().lower()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror("Error", "Dont leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError,json.decoder.JSONDecodeError):
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website.title(), message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showerror(title="data not found")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

#labels

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
website_label = Label(text="Email/Username: ")
website_label.grid(row=2, column=0)
website_label = Label(text="Password: ")
website_label.grid(row=3, column=0)

#entries

website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"my_most_common_email@email.com")
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

#buttons
search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", width=16, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Save", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
