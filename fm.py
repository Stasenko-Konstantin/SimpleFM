from tkinter import *
from os import *
from dop import *

stdpath = getenv("SystemDrive")+"\\"
d = sortdir(listdir(path=stdpath))
print(d)

def upd(event):
    updd()

def updd():
    global left, right
    left.config(width=root.winfo_width()/3, height=root.winfo_height()-40)
    right.config(width=root.winfo_width(), height=root.winfo_height()-40)
    left.place(x=0, y=40)
    right.place(x=root.winfo_width()/3, y=40)

root = Tk()
root.geometry("1000x600")
root.minsize(1000, 600)
root.title("stdpath")

left = Frame(root, width=root.winfo_width()/3, height=root.winfo_height()-40, bg="gray76")
right = Frame(root, width=root.winfo_width(), height=root.winfo_height()-40, bg="lemon chiffon")


left.place(x=0, y=40)
right.place(x=root.winfo_width()/3, y=40)

root.bind('<Configure>', upd)

root.mainloop()
