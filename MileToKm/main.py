from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(250, 100)
window.config(padx=25, pady=25)


def convert():
    in_km = round((float(entry.get()) * 1.609344), 2)
    answer["text"] = in_km


entry = Entry(width=10)
entry.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

answer = Label(text=0)
answer.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate = Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()
