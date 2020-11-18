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
btn_list = []

execute = "\n\
global {0}\n\
def left_click{1}(event):\n\
    global stdpath, stdlist\n\
    if '.' in stdlist[{1}]:\n\
        pass\n\
    else:\n\
        stdpath = dop.concat(path.abspath(stdpath + stdlist[{1}]))\n\
        print(stdpath)\n\
        stdlist = dop.sortdir(listdir(path=stdpath))\n\
        destr(btn_list, stdlist)\n\
        root.title(stdpath)\n\
{0} = Button(right, text=stdlist[i], bg='old lace')\n\
{0}.bind('<Button-1>', left_click{1})\n\
{0}.place(x=10, y=rast)\n\
"

def per(event):
    upd()

def upd():
    global left, right, line
    
    left.config(height=root.winfo_height()-80)
    right.config(height=root.winfo_height()-80)

    line.config(to=len(stdlist), length=root.winfo_height()-85)
    line.place(x=root.winfo_width()-380)

    rast = 30 - int(line.get()) * 30
    for i in range(len(stdlist)):
        name_btn = "btn" + str(i)
        exec(
"{0}.place(x=10, y=rast)\n\
".format(name_btn))
        rast += 30

def vn(event):
    upd()

def destr(x, y):
    global rast
    rast = 5
    for i in x:
        exec(
"{0}.destroy()\n\
".format(i))
    for i in range(len(y)):
        name_btn = "btn" + str(i)
        btn_list.append(name_btn)
        exec(execute.format(name_btn, i))
        rast += 30
        
root = Tk()
root.geometry("1000x600")
root.minsize(1000, 600)
root.title(stdpath)

left = Frame(root, width=333, height=560, bg="gray76")
left.place(x=0, y=80)

right = Frame(root, width=4000, height=560, bg="lemon chiffon")
right.place(x=333, y=80)

line = Scale(right, from_ = 1, to = len(stdlist), bg="lemon chiffon")
line.place(x=1, y=0)

rast = 5
for i in range(len(stdlist)):
    name_btn = "btn" + str(i)
    btn_list.append(name_btn)
    exec(execute.format(name_btn, i))
    rast += 30

line.bind("<B1-Motion>", vn)
line.bind("<Button-1>", vn)
line.bind('<ButtonRelease>', vn)
root.bind('<Configure>', per)

root.mainloop()
