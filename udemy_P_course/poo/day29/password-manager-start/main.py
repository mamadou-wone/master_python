#  ___       __   ________  ________   _______
# |\  \     |\  \|\   __  \|\   ___  \|\  ___ \
# \ \  \    \ \  \ \  \|\  \ \  \\ \  \ \   __/|
#  \ \  \  __\ \  \ \  \\\  \ \  \\ \  \ \  \_|/__
#   \ \  \|\__\_\  \ \  \\\  \ \  \\ \  \ \  \_|\ \
#    \ \____________\ \_______\ \__\\ \__\ \_______\
#     \|____________|\|_______|\|__| \|__|\|_______|
import pyperclip
from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # new_value for item in list
    letter_list = [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    symbol_list = [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    number_list = [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    # for char in password_list:
    #     password += char
    # print(password_list)
    input_password.insert(0, f"{password}")
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_info(site, get_email, password):
    with open("data.txt", "a") as data:
        data.write(f"{site} |   {get_email} | {password} \n")
        input_password.delete(0, "end")
        website_name.delete(0, "end")
        email_input.delete(0, "end")


def get_credential():
    website = website_name.get()
    if len(website) == 0:
        messagebox.showerror("Error", "Le champ Website ne peut être vide")
    else:
        try:
            with open("data.json") as file_data:
                data = json.load(file_data)
        except FileNotFoundError:
            messagebox.showerror("Error", "Le Fichier n'exite pas ou est vide")
        try:
            messagebox.showinfo(website, f"Email: {data[website]['email']} \n Password: {data[website]['password']}")
        except KeyError:
            messagebox.showerror("Error", f"La cle {website} ne correspond à aucun champ")

def save_password():
    website = website_name.get()
    email = email_input.get()
    passwd = input_password.get()
    new_data = {
        website:{
            "email": email,
            "password": passwd
        }
    }

    if len(website) == 0 or len(passwd) == 0 or len(email) == 0:
        messagebox.showerror("Error", "Verifiez les information avant de continuer")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the detatils entered: \nEmail:{email}\nPassword:{passwd}")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading File
                    data = json.load(data_file)
                    # Update
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    # Writte
                    json.dump(data, data_file, indent=4)
                    input_password.delete(0, "end")
            finally:
                input_password.delete(0, "end")
                website_name.delete(0, "end")
                email_input.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# website label
website = Label(text="Website:", font=("Roboto", 10, "bold"))
website.grid(column=0, row=1)

# website input
website_name = Entry(width=35)
website_name.grid(column=1, row=1, columnspan=2)
website_name.focus()
get_website = website_name.get()

# Email
email = Label(text="Email/Username:", font=("Roboto", 10, "bold"))
email.grid(column=0, row=2)

# email input
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "wone@email.com")
get_email = email_input.get()
# Password label
password = Label(text="Password:", font=("Roboto", 10, "bold"))
password.grid(column=1, row=3)

# password input
input_password = Entry(width=21)
input_password.grid(column=1, row=3)
get_password = input_password.get()

# Gen Button
gen_button = Button(text="Generate Password", command=gen_password)
gen_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=get_credential)
search_button.grid(column=3, row=1)


window.mainloop()
