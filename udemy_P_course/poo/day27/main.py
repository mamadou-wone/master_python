from tkinter import *

from setuptools._distutils.dist import command_re

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_click():
    print("Clik")
    text = input.get()
    my_label.config(text=text)

# label
my_label = Label(text="Boss", font=("Arial", 24, "bold"))
# pack pour ajouter
# my_label.pack(side="left")
# my_label.pack()
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

#new Button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)


#Input
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)







window.mainloop()
