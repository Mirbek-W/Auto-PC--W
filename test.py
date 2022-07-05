from tkinter import*
from tkinter import ttk
 
 
def xFunc1(event):
 print (f"Координаты щелчка левой кнопкой мыши: x = {event.x} y = {event.y}")
 
 
 win=Tk()
 win.title ("Kahn Software v1") # # Название окна
 win.geometry ("600x500 + 200 + 20") # # За окном 500 следует буква x

 button1 =Button(win, text="leftmouse button")
 # button1 = tkinter.Label (win, text = "leftmouse button") # # Любое небольшое пространство может быть связано с событиями мыши
 button1.bind ("<Button-1>", xFunc1) # # Привязка событий левого щелчка к элементам управления кнопки
 button1.pack()
 
 win.mainloop () # # Сохранение окон


xFunc1()