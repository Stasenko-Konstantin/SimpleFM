#! Модуль вспомогательных функций

def sortdir(arg):
    x1, x2 = [i for i in arg if not "." in i], [i for i in arg if "." in i]
    return x1 + x2

def mycopy(arg):
    return [i for i in arg]

def concat(arg):
    return arg + "\\"

def got_back(arg, x="\\"):
    g = str_to_list(arg)[::-1]
    return "".join(take_while(x, g[1:])[::-1])

def str_to_list(arg):
    return [i for i in arg]

def take_while(f, arg):
    x = mycopy(arg)
    for i in range(len(arg)):
        if "".join(x[i:i+1]) == f:
            return x[i+1:]

def btn_lists(stdlist):
    widg_list = []
    for i in range(len(stdlist)):
        name = "btn" + str(i)
        widg_list.append(name)
    return widg_list

def exec():
    return "\n\
global {0}\n\
def copy{1}():\n\
    global copyname\n\
    copyname = path.abspath(stdpath + stdlist[{1}])\n\
    print(copyname)\n\
def rename{1}():\n\
    pass\n\
def delete{1}():\n\
    pass\n\
def popup{1}(event):\n\
    menu{1}.post(event.x_root, event.y_root)\n\
def left_click{1}(event):\n\
    global stdpath, stdlist\n\
    if '.' in stdlist[{1}]:\n\
        pass\n\
    else:\n\
        try:\n\
            stdpath = dop.concat(path.abspath(stdpath + stdlist[{1}]))\n\
            print(stdpath)\n\
            btn_list = dop.btn_lists(stdlist)\n\
            stdlist = dop.sortdir(listdir(path=stdpath))\n\
            destr(btn_list, stdlist)\n\
            root.title(stdpath)\n\
        except:\n\
            btn_list = dop.btn_lists(stdlist)\n\
            stdpath = dop.concat(dop.got_back(stdpath))\n\
            stdlist = dop.sortdir(listdir(path=stdpath))\n\
            print(stdpath)\n\
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
