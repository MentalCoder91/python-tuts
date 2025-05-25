from tkinter import *

def button_clicked():
    print('Clicked')
    data_txt = input_data.get()
    my_label['text'] = data_txt


window = Tk()
window.title("GUI Anish")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#Labels
my_label = Label(text="I am Label", font= ('Arial', 25, 'bold'))
# my_label.pack()
my_label.grid(column=0, row=0)

# my_label['text'] = 'Anish new text'
# my_label.config(text= 'Anish updated text')

#Entry

input_data = Entry()
data = input_data.get()
input_data.grid(column=3, row=3)
# input_data.pack()

#Button
button = Button(text='Click', command=button_clicked)
button.grid(column=1, row=1)

button_new = Button(text='Click', command=button_clicked)
button_new.grid(column=3, row=0)
# button.pack()










window.mainloop()
