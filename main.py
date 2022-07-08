from cProfile import label

from tkinter import *
import time
import pyautogui
from threading import *
from PIL import ImageTk 


from tkinter import Tk, Canvas, Frame, BOTH

bacr1 = "#1E1932"
text_color = "#4F38A6"
zadni = "#15111F"
b_color = "#48E66A"

def xy ():



    

    try:
      while True:

        # получение текущих координат
        x, y = pyautogui.position()
        # метод str(x) превращает число в строку а rjust(4) сдвигает его на четыре позиции вправо
         
        positionStr = 'X:' + str(x).rjust(4) + '  Y:' + str(y).rjust(4)
        # end предотвращает добавление символа новой строки,  без  этого старые координаты удалить не получится
        
        prinx=print(positionStr,end='')
        

        # escape-символ \ b стирает конец строки и чтобы удалить всю строку умножаем его на длину строки
        print('\b'*len(positionStr), end='', flush=True)

        # для предотвращения мигания при выполнении цикла используем засыпание
        time.sleep(0.01)



# Когда пользователь нажимает CTRL-C, выполнение программы переходит к разделу except и # Done будет напечатан с новой строки
    except KeyboardInterrupt:
        print('\nDone')


def root2():

    
    root2 = Tk()
    root2.geometry("350x460")
    root2.resizable(width=False, height=False)
    
    root2.title("Auto PC -W")
    root2.iconbitmap(r'img/logo.ico')
    root2['background'] = bacr1
    x = (root2.winfo_screenwidth() - root2.winfo_reqwidth()) / 1.5
    y = (root2.winfo_screenheight() - root2.winfo_reqheight()) / 2
    root2.wm_geometry("+%d+%d" % (x, y))


    posx=Label(root2,text="хуй", font=14,fg="#ff0000")

    posx.place(x=100,y=50)
    




    root2.mainloop()


def start_menu():
    root = Tk()
    root.geometry("750x460")
    root.resizable(width=False, height=False)
    root.title("Auto PC -W")
    root.iconbitmap(r'img/logo.ico')
    root['background'] = bacr1

    #кнопка настройки 
    image = ImageTk.PhotoImage(file="img/set.png")
    set=Button(root, image=image, bg=bacr1 ,border=0)
    set.place(x=670,y=20)


    # нажатие фронт
    clik_lab = Button(text="number of clicks", fg=zadni, bg=text_color)
    clik_lab.place(x=10, y=20)
    clik_ent = Entry(root,  font=15, bg='#222431',
                     borderwidth=0, foreground="white")
    clik_ent.place(x=109, y=20, width=55, height=25)

    clik_dli = Button(text="Mile/sec duration", fg=zadni, bg=text_color)
    clik_dli.place(x=205, y=20)
    clik_ent2 = Entry(root, font=15,   bg='#222431',
                      borderwidth=0, foreground="white")
    clik_ent2.place(x=309, y=20, width=55, height=26)

    but1 = Button(root, background=b_color, text="Add")
    but1.place(x=395, y=20)

    # нажатие Rigint фронт
    clikr_lab = Button(text="right  clicks", fg=zadni, bg=text_color)
    clikr_lab.place(x=10, y=50)
    clikr_ent = Entry(root,  font=15, bg='#222431',
                      borderwidth=0, foreground="white")
    clikr_ent.place(x=82, y=50, width=55, height=25)

    clikr_dli = Button(text="Mile/sec duration", fg=zadni, bg=text_color)
    clikr_dli.place(x=205, y=50)
    clikr_ent2 = Entry(root, font=15,   bg='#222431',
                       borderwidth=0, foreground="white")
    clikr_ent2.place(x=309, y=50, width=55, height=26)

    but1r = Button(root, background=b_color, text="Add")
    but1r.place(x=395, y=50)

   # навидение на фронт

    navi = Button(text="hover", fg=zadni, bg=text_color)
    navi.place(x=10, y=80)
    navi_e1 = Entry(root,  font=15, bg='#222431',
                    borderwidth=0, foreground="white")
    navi_e1.place(x=109, y=80, width=55, height=25)
    navi_e2 = Entry(root,  font=15, bg='#222431',
                    borderwidth=0, foreground="white")
    navi_e2.place(x=52, y=80, width=55, height=25)

    navi_dli = Button(text="Mile/sec duration", fg=zadni, bg=text_color)
    navi_dli.place(x=205, y=80)
    navi_ent2 = Entry(root, font=15,   bg='#222431',
                      borderwidth=0, foreground="white")
    navi_ent2.place(x=309, y=80, width=55, height=26)

    navi_add = Button(root, background=b_color, text="Add")
    navi_add.place(x=395, y=80)

    # drag to брать  фронт

    dra = Button(text="drag to A", fg=zadni, bg=text_color)
    dra.place(x=10, y=110)
    dra_e1 = Entry(root,  font=15, bg='#222431',
                   borderwidth=0, foreground="white")
    dra_e1.place(x=127, y=110, width=55, height=25)
    dra_e2 = Entry(root,  font=15, bg='#222431',
                   borderwidth=0, foreground="white")
    dra_e2.place(x=70, y=110, width=55, height=25)

    dra2 = Button(text="drag to B", fg=zadni, bg=text_color)
    dra2.place(x=205, y=110)

    dra2_e1 = Entry(root,  font=15, bg='#222431',
                    borderwidth=0, foreground="white")
    dra2_e1.place(x=322, y=110, width=55, height=25)
    dra2_e2 = Entry(root,  font=15, bg='#222431',
                    borderwidth=0, foreground="white")
    dra2_e2.place(x=265, y=110, width=55, height=25)

    dra_dli = Button(text="Mile/sec duration", fg=zadni, bg=text_color)
    dra_dli.place(x=400, y=110)
    dra_ent2 = Entry(root, font=15,   bg='#222431',
                     borderwidth=0, foreground="white")
    dra_ent2.place(x=504, y=110, width=55, height=26)

    dra_add = Button(root, background=b_color, text="Add")
    dra_add.place(x=590, y=110)

    # писать Print press

    prin_lab = Button(text="print, press", fg=zadni, bg=text_color)
    prin_lab.place(x=10, y=140)
    prin_ent = Entry(root,  font=15, bg='#222431',
                     borderwidth=0, foreground="white")
    prin_ent.place(x=80, y=140, width=105, height=25)

    prin_dli = Button(text="Mile/sec duration", fg=zadni, bg=text_color)
    prin_dli.place(x=205, y=140)
    prin_ent2 = Entry(root, font=15,   bg='#222431',
                      borderwidth=0, foreground="white")
    prin_ent2.place(x=309, y=140, width=55, height=26)

    prinb = Button(root, background=b_color, text="Add")
    prinb.place(x=395, y=140)

    #scroll
    scroll_lab = Button(text="scroll", fg=zadni, bg=text_color)
    scroll_lab.place(x=10, y=170)
    scroll_ent = Entry(root,  font=15, bg='#222431',
                     borderwidth=0, foreground="white")
    scroll_ent.place(x=50, y=170, width=55, height=25)

    scrollb = Button(root, background=b_color, text="Add")
    scrollb.place(x=136, y=170)

    #scroll click
    scrollk_lab = Button(text="scroll", fg=zadni, bg=text_color)
    scrollk_lab.place(x=205, y=170)
    scrollk_ent = Entry(root,  font=15, bg='#222431',
                     borderwidth=0, foreground="white")
    scrollk_ent.place(x=245, y=170, width=55, height=25)

    scrollbk = Button(root, background=b_color, text="Add")
    scrollbk.place(x=336, y=170)














    xy1=Thread(target=xy)
    xy1.start()
    xy3=Thread(target=root2)
    xy3.start()
    

    
    root.mainloop()


xy2=Thread(target=start_menu)



xy2.start()



