import tkinter as Tk


from tkinter import *


class App(object):
    def new_row(self):
        # Create widgets
        new_entry = Label( root,text="рома",  width=7)

        # Put widgets in grid
        self.num_rows += 20
        new_entry.place(x=10,y=self.num_rows)

    def __init__(self):
        self.num_rows = 1
        iop="строка"
        createRow_button = Button(
            root, text=iop, command=self.new_row)
        createRow_button.grid()

root = Tk()
app = App()
root.mainloop()