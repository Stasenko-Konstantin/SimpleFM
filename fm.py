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

class Exec:

    @staticmethod
    def copy(n):
        global copyname
        copyname = os.path.abspath(stdpath + stdlist[n])

    @staticmethod
    def renok(n):
        renamename = os.path.abspath(stdpath + stdlist[n])
        try:
            error.config(text=" ")
            os.rename(renamename, stdpath+ren.get())
            upd2()
        except:
            error.config(text="Неверное имя")
        ren.destroy()

    @staticmethod        
    def rename(n):
        global ren
        ren = Entry(root)
        ren.place(y=20, x=400)
        root.bind('<Return>', lambda event: Exec.renok(n))

    @staticmethod        
    def delete(n):
        if os.path.isfile(os.path.abspath(stdpath + stdlist[n])):
            os.remove(os.path.abspath(stdpath + stdlist[n]))
        else:
            os.rmdir(os.path.abspath(stdpath + stdlist[n]))
        upd2()

    @staticmethod
    def popup(event, menu):
        menu.post(event.x_root, event.y_root)

    @staticmethod
    def left_click(n):
        global stdpath, stdlist
        if os.path.isfile(os.path.abspath(stdpath + stdlist[n])):
            os.startfile(os.path.abspath(stdpath + stdlist[n]))
        else:
            try:
                stdpath = dop.concat(os.path.abspath(stdpath + stdlist[n]))
                btn_list = dop.btn_lists(stdlist)
                stdlist = dop.sortdir(os.listdir(path=stdpath))
                destr(btn_list, stdlist)
                root.title(stdpath)
            except:
                btn_list = dop.btn_lists(stdlist)
                stdpath = dop.concat(dop.got_back(stdpath, "\\"))
                stdlist = dop.sortdir(os.listdir(path=stdpath))
                destr(btn_list, stdlist)

    @staticmethod
    def exec(name_btn, i, rast):
        global btn
        btns[name_btn] = Button(right, text=stdlist[i], bg='old lace')
        btns[name_btn].place(x=10, y=rast)
        menu = Menu(tearoff=0)
        menu.add_command(label='Копировать', command= lambda: Exec.copy(i))
        menu.add_command(label='Переименовать', command= lambda: Exec.rename(i))
        menu.add_command(label='Удалить', command= lambda: Exec.delete(i))
        btns[name_btn].bind('<Double-Button-1>', lambda event: Exec.left_click(i))
        btns[name_btn].bind('<Button-3>', lambda event: Exec.popup(event, menu))

stdpath = dop.concat(os.getenv("SystemDrive"))
stdlist = dop.sortdir(os.listdir(path=stdpath))
btns = {}
ch = 0

def popup(event):
    menu.post(event.x_root, event.y_root)

def paste():
    if os.path.isfile(copyname):
        two = (dop.list_to_str(dop.take_while2("\\", copyname[::-1])[::-1]))
        print(stdpath[:-1])
        print(two)
        copyfile(copyname, stdpath[:-1]+two)
    else:
        two = (dop.list_to_str(dop.take_while2("\\", copyname[::-1])[::-1]))
        print(stdpath[:-1])
        print(two)
        copytree(copyname, stdpath[:-1]+two)
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
    stdpath = dop.concat(dop.got_back(stdpath, "\\"))
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
    global left, right, line, rast, ch, panel
    
    panel.config(width=root.winfo_width(), height=root.winfo_height()-80)
    right.config(width=root.winfo_width())

    line.config(to=len(stdlist), length=root.winfo_height()-85)
    line.place(x=root.winfo_width()-40)

    ref = line.get()
    line.set(ref + ch)
    ch = 0
    ref = line.get()
    rast = 30 - ref * 30
    
    right.place(x=10, y=rast)

def destr(x, y):
    global rast, btns
    rast = 5
    for i in x:
        btns[i].destroy()
    for i in range(len(y)):
        name_btn = "btn" + str(i)
        Exec.exec(name_btn, i, rast)
        rast += 30

root = Tk()
root.geometry("1000x600")
root.minsize(1000, 600)
root.title(stdpath)

error = Label(root, text=" ")
error.place(y=20, x=450)

panel = Frame(root, width=1000, height=600, bg="lemon chiffon")
panel.place(x=0, y=80)

right = Frame(panel, width=4000, height=9999999, bg="lemon chiffon")
right.place(x=0, y=80)

line = Scale(panel, from_ = 1, to = len(stdlist), bg="lemon chiffon")
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
    Exec.exec(name_btn, i, rast)
    rast += 30

right.bind("<Button-3>", popup)
line.bind("<B1-Motion>", lambda event: upd())
line.bind("<Button-1>", lambda event: upd())
line.bind("<ButtonRelease>", lambda event: upd())
root.bind("<Configure>", lambda event: upd())
root.bind("<MouseWheel>", per)

root.mainloop()
