#! Модуль вспомогательных функций

def sortdir(arg):
    x1, x2 = [i for i in arg if not "." in i], [i for i in arg if "." in i]
    return x1 + x2

def mycopy(arg):
    return [i for i in arg]

def concat(arg):
    return arg + "\\"

def concat2(arg):
    return "\\" + arg

def got_back(arg, x="\\"):
    g = str_to_list(arg)[::-1]
    return "".join(take_while(x, g[1:])[::-1])

def str_to_list(arg):
    return [i for i in arg]

def list_to_str(arg):
    string = ""
    for i in arg:
        string += str(i)
    return string

def take_while(f, arg):
    print(f)
    x = mycopy(arg)
    for i in range(len(arg)):
        if "".join(x[i:i+1]) == f:
            return x[i+1:]

def take_while2(f, arg):
    x = mycopy(arg)
    for i in range(len(arg)):
        if "".join(x[i:i+1]) == f:
            return x[:i+1]

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
