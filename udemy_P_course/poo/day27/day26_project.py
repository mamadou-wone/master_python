from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=150, height=100)
window.config(padx=50, pady=50)

def convert():
    number = int(input.get())
    km = round(number * 1.609)
    km_num.config(text=str(km))

#is equal label
is_equal = Label(text="is equal to", font=("Arial", 15, "bold"))
is_equal.grid(column=0, row=1)


#num convert label
km_num = Label(text="0", font=("Arial", 15, "bold"))
km_num.grid(column=1, row=1)
km_num.config(padx=50)

#km
km = Label(text="Km", font=("Arial", 15, "bold"))
km.grid(column=2, row=1)

#input
input = Entry(text="0")
input.config(width=20)
input.grid(column=1, row=0)

#Miles
miles = Label(text="Miles", font=("Arial", 15, "bold"))
miles.grid(column=3, row=0)

#button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)







window.mainloop()