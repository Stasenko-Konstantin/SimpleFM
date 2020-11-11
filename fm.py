#! Главный модуль

'''
Автор: Стасенко Константин

О программе: простой файловый менеджер который необходимо было сделать по учебному
заданию
'''

from tkinter import *
from os import *
import dop # Мой дополнительный модуль

stdpath = getenv("SystemDrive")+"\\"
stdlist = dop.sortdir(listdir(path=stdpath))

def upd(event):
    updd()

def updd():
    global left, right
    left.config(height=root.winfo_height()-40)
    right.config(height=root.winfo_height()-40)

root = Tk()
root.geometry("1000x600")
root.minsize(1000, 600)
root.title("stdpath")


left = Frame(root, width=333, height=560, bg="gray76")
right = Frame(root, width=4000, height=560, bg="lemon chiffon")


left.place(x=0, y=40)
right.place(x=333, y=40)

root.bind('<Configure>', upd)

root.mainloop()
