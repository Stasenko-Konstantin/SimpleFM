from tkinter import *
from tkinter.filedialog import *
import os

sc = 0
data = []
labels = {}
ch = 0

class Customer:
    def __init__(self, name):
        self.name = name
        self.products = {}
    
    def addProduct(self, product, price):
        self.products[product] = price
    
    def getProducts(self):
        return self.products
    
    def getProduct(self, product):
        return self.products[product]

#Всплывающие окна при нажатии кнопки "Помощь"
def Help():
    root1 = Tk()
    root1.title('Помощь')
    root1.geometry('420x100')
    lbl = Label(root1, text="Для работы с программой\n\
вам просто нужно ввести отпускную цену\n\
для каждого вида обуви. Программа, на основе\n\
введеных данных, сама посчитает доход и выведет диаграмму.", font="Arial 10")
    lbl.place(x=10, y=10)
    root1.mainloop()


#Всплывающие окна при нажатии кнопки "О Программе"
def About():
    root2 = Tk()
    root2.title('О Программе')
    root2.geometry('270x100')
    lbl = Label(root2, text="Программа: Project v1.0\n\
Разработана ТАТК ГА филиал МГТУ ГА\n\
курсантом 331 группы Мешалкиным В.О", font="Arial 10")
    lbl.place(x=10, y=10)
    root2.mainloop()

def create(i, rast):
    pass

def click(event, i, rast):
    pass

#Таблица
def fill_table():
    pass

def oppen():
    global data
    '''path = askopenfilename()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            f = f.read()
    except:
        oppen()
        return'''
    #Покупатель Товар    Кол-ва
    #ФИО        Название Тут ясно
    f = '{"Чувак1": [{"панталоны": 500}, {"картина": 12}]}\n\
{"Чувак2": [{"панталоны": 500}, {"картина": 12}]}\n\
{"Чувак3": [{"панталоны": 500}, {"картина": 12}]}\n\
{"Чувак4": [{"панталоны": 500}, {"картина": 12}]}\n\
{"Чувак5": [{"панталоны": 500}, {"картина": 12}]}\n\
{"Чувак6": [{"панталоны": 500}, {"картина": 12}]}\n\
{"Чувак7": [{"панталоны": 500}, {"картина": 12}]}\n\
{"Чувак8": [{"панталоны": 500}, {"картина": 12}]}\n\
{"Чувак9": [{"панталоны": 500}, {"картина": 12}]}\n\
{"Чувак10": [{"панталоны": 500}, {"картина": 12}]}'
    temp = f.split('\n')
    for i in range(len(temp)):
        name_border = temp[i][1:].index(':')
        products = temp[i][temp[i].index('[')+1:temp[i].index(']')].split(', ')
        customer = Customer(temp[i][2:name_border])
        data.append(customer)
        for j in range(len(products)):
            prod_border = products[j][2:].index('"')+2
            prod = products[j][2:prod_border]
            price_border = products[j].index('}')
            price = products[j][prod_border+2:price_border]
            data[i].addProduct(prod, int(price))
    fill_table()
    
    

def save():
    pass

def upd():
    global right, line, prast, ch, panel
    
    panel.config(width=root.winfo_width(), height=root.winfo_height())
    right.config(width=root.winfo_width()-80)

    line.config(to=len(data), length=root.winfo_height())
    line.place(x=root.winfo_width()-40)

    ref = line.get()
    line.set(ref + ch)
    ch = 0
    ref = line.get()
    prast = 30 - ref * 30
    
    right.place(x=10, y=prast)

root = Tk()
root.minsize(450, 450)
root.resizable(False, False)
root.config(bg="lemon chiffon")
root.title("Program")
mainmenu = Menu(root)
root.config(menu=mainmenu)

panel = Frame(root, width=400, height=600, bg="green")
panel.place(x=0, y=0)

right = Frame(panel, width=400, height=9999999, bg="lemon chiffon")
right.place(x=25, y=0)

oppen()
line = Scale(panel, from_ = 1, to = len(data), bg="lemon chiffon")
line.place(x=1, y=0)
upd()

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть", command=oppen)
filemenu.add_command(label="Сохранить", command=save)
filemenu.add_command(label="Выход", command=lambda: exit(1))

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="Помощь", command=Help)
helpmenu.add_command(label="О Программе", command=About)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Помощь", menu=helpmenu)

line.bind("<B1-Motion>", lambda event: upd())
line.bind("<Button-1>", lambda event: upd())
line.bind("<ButtonRelease>", lambda event: upd())

root.mainloop()
