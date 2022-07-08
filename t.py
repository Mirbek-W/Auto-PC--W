from tkinter import *

window = Tk()
window.resizable(0, 0)
window.title('WORM')  
window.geometry('800x600')
window['bg'] = 'white'

def click():
   c = Canvas(width='100', height='100', bg='blue', bd='0')
   c.pack()

   btn1 = Button(text='В Меню', command=c.destroy)            # <---- command=c.destroy
   btn1 = c.create_window(400, 280, window=btn1)

btn = Button(text='Новая игра', font='Arial 15', command=click)
btn.place(relx=0.439, rely=0.3, relwidth=0.13, relheight=0.05)

window.mainloop()