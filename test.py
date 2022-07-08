import tkinter as Tk


from tkinter import *


class App(object):
    def new_row(self):
        # Create widgets

        message = StringVar()
        message_entry = Entry(textvariable=message)
        message_entry.pack(side=TOP)
        new_entry = Label( root,text=" h",  width=7)
        new_entry.config(text=message.get())


        # Put widgets in grid
        self.num_rows += 20
        new_entry.place(x=10,y=self.num_rows)

    def __init__(self):
        self.num_rows = 1
        
        iop3="строка"
        createRow_button = Button(
            root, text="jljlj", command=self.new_row(iop3))
        createRow_button.place(x=20,y=100)
    def __init__(self):
        self.num_rows = 1


        
        iop="oop"

        createRow_button = Button(
            root, text="lfsdjkl", command=self.new_row)
        createRow_button.pack()

root = Tk()
app = App()
root.mainloop()