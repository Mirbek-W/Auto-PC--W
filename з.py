


from tkinter import *

# commands

def add_one():
    label1.config(text=message.get())

# head
root = Tk()
root.title("MMR")
root.geometry("250x400")
# nameLabel
name_label = Label(text="MMR:")
name_label.pack(side=TOP)
# txt
message = StringVar()
message_entry = Entry(textvariable=message)
message_entry.pack(side=TOP)

# btn
btn = Button(text="Update", command=add_one)
btn.pack(side=TOP)

# LABEL
label1 = Label(text="TEST", fg="#eee", bg="#333", width=250, height=400)
label1.pack(side=LEFT)


root.mainloop()