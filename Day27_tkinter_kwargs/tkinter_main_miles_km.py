from tkinter import *


def button_clicked():
    print('Clicked')
    data_txt = int(input_data.get())
    data_km = round(data_txt * 1.609, 2)
    result.config(text=data_km)


window = Tk()
window.title("GUI Anish")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

# Entry

input_data = Entry()
data = input_data.get()
input_data.grid(column=1, row=0)
# input_data.pack()

# Labels
miles = Label(text="Miles", font=('Arial', 9, 'bold'))
# my_label.pack()
miles.grid(column=2, row=0)

eq = Label(text="is equal to ", font=('Arial', 9, 'bold'))
# my_label.pack()
eq.grid(column=0, row=1)

result = Label(text="0", font=('Arial', 9, 'bold'))
# my_label.pack()
result.grid(column=1, row=1)

km = Label(text="Km", font=('Arial', 9, 'bold'))
# my_label.pack()
km.grid(column=2, row=1)

# Button
button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)

# button.pack()


window.mainloop()
