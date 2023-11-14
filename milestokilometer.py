from tkinter import *

window = Tk()
window.title("my first gui")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

entry1 = Entry()
entry1.grid(row=1,column=2)

def calc():
    miles = entry1.get()
    km = int(miles) * 1.609344
    r_km = round(km)
    label3.config(text=r_km)
    print(miles)


label1 = Label(text='Miles')
label1.grid(row=1, column=3)

label2 = Label(text="is equal to")
label2.grid(row=2, column=1)

label3 = Label(text='0')
label3.grid(row=2,column=2)

label4 = Label(text="Km")
label4.grid(row=2, column=3)

button = Button(text="Calculate", command=calc)
button.grid(row=3, column=2)


window.mainloop()

