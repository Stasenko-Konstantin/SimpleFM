# -*- coding: utf-8 -*-
#! Главный модуль

'''
Автор: Стасенко Константин
О программе: простой файловый менеджер который необходимо было сделать по учебному
заданию
'''

from tkinter import *
import os
from shutil import copytree, copyfile
import dop # Мой дополнительный модуль

def execute():
    return "\n\
global {0}\n\
def copy{1}():\n\
    global copyname\n\
    copyname = os.path.abspath(stdpath + stdlist[{1}])\n\
def renok{1}(event):\n\
    renamename = os.path.abspath(stdpath + stdlist[{1}])\n\
    try:\n\
        error.config(text=' ')\n\
        os.rename(renamename, stdpath+{0}ren.get())\n\
        upd2()\n\
    except:\n\
        error.config(text='Неверное имя')\n\
    {0}ren.destroy()\n\
def rename{1}():\n\
    global {0}ren\n\
    {0}ren = Entry(root)\n\
    {0}ren.place(y=20, x=400)\n\
    root.bind('<Return>', renok{1})\n\
def delete{1}():\n\
    if os.path.isfile(os.path.abspath(stdpath + stdlist[{1}])):\n\
        os.remove(os.path.abspath(stdpath + stdlist[{1}]))\n\
    else:\n\
        os.rmdir(os.path.abspath(stdpath + stdlist[{1}]))\n\
    upd2()\n\
def popup{1}(event):\n\
    menu{1}.post(event.x_root, event.y_root)\n\
def left_click{1}(event):\n\
    global stdpath, stdlist\n\
    if os.path.isfile(os.path.abspath(stdpath + stdlist[{1}])):\n\
        os.startfile(os.path.abspath(stdpath + stdlist[{1}]))\n\
    else:\n\
        try:\n\
            stdpath = dop.concat(os.path.abspath(stdpath + stdlist[{1}]))\n\
            btn_list = dop.btn_lists(stdlist)\n\
            stdlist = dop.sortdir(os.listdir(path=stdpath))\n\
            destr(btn_list, stdlist)\n\
            root.title(stdpath)\n\
        except:\n\
            btn_list = dop.btn_lists(stdlist)\n\
            stdpath = dop.concat(dop.got_back(stdpath))\n\
            stdlist = dop.sortdir(os.listdir(path=stdpath))\n\
            destr(btn_list, stdlist)\n\
{0} = Button(right, text=stdlist[i], bg='old lace')\n\
{0}.place(x=10, y=rast)\n\
menu{1} = Menu(tearoff=0)\n\
menu{1}.add_command(label='Копировать', command=copy{1})\n\
menu{1}.add_command(label='Переименовать', command=rename{1})\n\
menu{1}.add_command(label='Удалить', command=delete{1})\n\
{0}.bind('<Double-Button-1>', left_click{1})\n\
{0}.bind('<Button-3>', popup{1})\n\
"

stdpath = dop.concat(os.getenv("SystemDrive"))
stdlist = dop.sortdir(os.listdir(path=stdpath))
ch = 0

def popup(event):
    menu.post(event.x_root, event.y_root)

def paste():
    if os.path.isfile(copyname):
        copyfile(copyname, stdpath[:-1]+(dop.list_to_str(dop.take_while2("\\", copyname[::-1])[::-1])))
    else:
        copytree(copyname, stdpath[:-1]+(dop.list_to_str(dop.take_while2("\\", copyname[::-1])[::-1])))
    upd2()

def createfile():
    global cen
    cen = Entry(root)
    cen.place(y=20, x=400)
    root.bind('<Return>', createfile2)

def createfile2(event):
    try:
        error.config(text=" ")
        f = open(str(stdpath+cen.get()), "w")
        f.write(" ")
        f.close()
        upd2()
    except:
        error.config(text='Неверное имя')
    cen.destroy()

def createdir():
    global cen
    cen = Entry(root)
    cen.place(y=20, x=400)
    root.bind('<Return>', createdir2)

def createdir2(event):
    try:
        error.config(text=" ")
        os.makedirs(stdpath+cen.get())
        upd2()
    except:
        error.config(text='Неверное имя')
    cen.destroy()
        
def per(event):
    global ch
    if event.delta < 0:
        ch = 1
    elif event.delta > 0:
        ch = -1
    upd()

def get_back():
    global stdpath, stdlist
    btn_list = dop.btn_lists(stdlist)
    print("prev", stdpath)
    stdpath = dop.concat(dop.got_back(stdpath, "\\"))
    print("curr ", stdpath)
    stdlist = dop.sortdir(os.listdir(path=stdpath))
    destr(btn_list, stdlist)

def upd2():
    global stdpath, stdlist
    btn_list = dop.btn_lists(stdlist)
    stdpath = dop.concat(stdpath)
    stdlist = dop.sortdir(os.listdir(path=stdpath))
    destr(btn_list, stdlist)
    upd()

def upd():
    global left, right, line, rast, ch
    
    right.config(height=root.winfo_height()-80)

    line.config(to=len(stdlist), length=root.winfo_height()-85)
    line.place(x=root.winfo_width()-40)

    ref = line.get()
    line.set(ref + ch)
    ch = 0
    ref = line.get()
    rast = 30 - ref * 30
    for i in range(len(stdlist)):
        name_btn = "btn" + str(i)
        exec(
"{0}.place(x=10, y=rast)\n\
".format(name_btn))
        rast += 30

def destr(x, y):
    global rast
    rast = 5
    for i in x:
        exec(
"{0}.destroy()\n\
".format(i))
    for i in range(len(y)):
        name_btn = "btn" + str(i)
        exec(execute().format(name_btn, i))
        rast += 30

root = Tk()
root.geometry("1000x600")
root.minsize(1000, 600)
root.title(stdpath)

error = Label(root, text=" ")
error.place(y=20, x=450)

right = Frame(root, width=4000, height=560, bg="lemon chiffon")
right.place(x=0, y=80)

line = Scale(right, from_ = 1, to = len(stdlist), bg="lemon chiffon")
line.place(x=1, y=0)

back = Button(root, text="<-", font="Arial 30", fg="ivory4", command=get_back)
back.place(x=0, y=0)

menu = Menu(tearoff=0)
menu.add_command(label="Вставить", command=paste)
menu.add_command(label="Создать файл", command=createfile)
menu.add_command(label="Создать папку", command=createdir)

rast = 5
btn_list = dop.btn_lists(stdlist)
for i in range(len(stdlist)):
    name_btn = "btn" + str(i)
    exec(execute().format(name_btn, i))
    rast += 30

right.bind("<Button-3>", popup)
line.bind("<B1-Motion>", lambda event: upd())
line.bind("<Button-1>", lambda event: upd())
line.bind("<ButtonRelease>", lambda event: upd())
root.bind("<Configure>", lambda event: upd())
root.bind("<MouseWheel>", per)

root.mainloop()
