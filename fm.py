#! Главный модуль

'''
Автор: Стасенко Константин

О программе: простой файловый менеджер который необходимо было сделать по учебному
заданию
'''

from tkinter import *
from os import *
import dop # Мой дополнительный модуль

stdpath = dop.concat(getenv("SystemDrive"))
stdlist = dop.sortdir(listdir(path=stdpath))

def per(event):
    upd()

def vn(event):
    upd()

def get_back():
    global stdpath, stdlist
    btn_list = dop.btn_lists(stdlist)
    radio_list = dop.radio_lists(stdlist)
    stdpath = dop.concat(dop.got_back(stdpath, "\\"))
    stdlist = dop.sortdir(listdir(path=stdpath))
    destr(btn_list, stdlist, radio_list)

def upd():
    global left, right, line
    
    right.config(height=root.winfo_height()-80)

    line.config(to=len(stdlist), length=root.winfo_height()-85)
    line.place(x=root.winfo_width()-40)

    rast = 30 - int(line.get()) * 30
    for i in range(len(stdlist)):
        name_btn = "btn" + str(i)
        name_radio = "radio" + str(i)
        exec(
"{0}.place(x=25, y=rast)\n\
{1}.place(x=1, y=rast)\n\
".format(name_btn, name_radio))
        rast += 30

def destr(x, y, z):
    global rast
    rast = 5
    for i in x:
        exec(
"{0}.destroy()\n\
".format(i))
    for i in z:
        exec(
"{0}.destroy()\n\
".format(i))
    for i in range(len(y)):
        name_btn = "btn" + str(i)
        name_radio = "radio" + str(i)
        exec(dop.exec().format(name_btn, i, name_radio))
        rast += 30
        
root = Tk()
root.geometry("1000x600")
root.minsize(1000, 600)
root.title(stdpath)

right = Frame(root, width=4000, height=560, bg="lemon chiffon")
right.place(x=0, y=80)

line = Scale(right, from_ = 1, to = len(stdlist), bg="lemon chiffon")
line.place(x=1, y=0)

back = Button(root, text="<-", font="Arial 30", fg="ivory4", command=get_back)
back.place(x=0, y=0)

rast = 5
btn_list = dop.btn_lists(stdlist)
radio_list = dop.radio_lists(stdlist)
for i in range(len(stdlist)):
    name_btn = "btn" + str(i)
    name_radio = "radio" + str(i)
    exec(dop.exec().format(name_btn, i, name_radio))
    rast += 30

line.bind("<B1-Motion>", vn)
line.bind("<Button-1>", vn)
line.bind('<ButtonRelease>', vn)
root.bind('<Configure>', per)

root.mainloop()
