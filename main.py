from cProfile import label
from tkinter import *

from tkinter import Tk, Canvas, Frame, BOTH

bacr1="#1E1932"
text_color="#4F38A6"
zadni="#15111F"
b_color="#48E66A"

def root2():
    root2=Tk()
    root2.geometry("350x460")
    root2.resizable(width=False, height=False)
    root2.title("Auto PC -W")
    root2.iconbitmap(r'img/logo.ico')
    root2['background']=bacr1
    x = (root2.winfo_screenwidth() - root2.winfo_reqwidth()) / 1.5
    y = (root2.winfo_screenheight() - root2.winfo_reqheight()) / 2
    root2.wm_geometry("+%d+%d" % (x, y))
    


    root2.mainloop()



def start_menu():
    root=Tk()
    root.geometry("750x460")
    root.resizable(width=False, height=False)
    root.title("Auto PC -W")
    root.iconbitmap(r'img/logo.ico')
    root['background']=bacr1
    

    clik_lab=Button(text="number of clicks",fg=zadni,bg=text_color)
    clik_lab.place(x=10,y=20)
    clik_ent= Entry(root,  font=15, bg='#222431',borderwidth=0, foreground="white")
    clik_ent.place(x=109,y=20,width=55,height=25)

    clik_dli=Button(text="Mile/sec duration",fg=zadni,bg=text_color)
    clik_dli.place(x=205,y=20)
    clik_ent2= Entry(root,font=15,   bg='#222431',borderwidth=0, foreground="white")
    clik_ent2.place(x=309,y=20,width=55, height=26)


    but1= Button (root,background=b_color ,text= "Add")
    but1.place(x=395, y=20)

    iop1=Label(text="88888888",fg=zadni,bg=text_color)
    iop1.place(x=475, y=20)



    root2()
    root.mainloop()


start_menu()
