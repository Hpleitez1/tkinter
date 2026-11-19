from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config( padx=20, pady=20)

#number that needs to go in there
entry = Entry(width = 10)
entry.grid(row=0, column=1)

#text box by the text box
miles_label = Label(text = "Miles")
miles_label.grid(row=0, column=2)

#equal
equal_label = Label(text = "is equal to")
equal_label.grid(row=1, column=0)

#button

def convert():
    miles = entry.get()
    miles = float(miles)

    miles = round(miles * 1.60934, 2)

    miles = str(miles)
    conver_label.config(text = miles)



button =Button(text = "calculate", command = convert)
button.grid(row=2, column=1)

#answer
conver_label = Label(text = "0")
conver_label.grid(row=1, column=1)

#km
km_label = Label(text = "km")
km_label.grid(row=1, column=2)



window.mainloop()

