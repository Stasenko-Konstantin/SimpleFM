#! Модуль вспомогательных функций

def exec():
    return "\n\
global {0}, {2}\n\
def left_click{1}(event):\n\
    global stdpath, stdlist\n\
    if '.' in stdlist[{1}]:\n\
        pass\n\
    else:\n\
        try:\n\
            stdpath = dop.concat(path.abspath(stdpath + stdlist[{1}]))\n\
            print(stdpath)\n\
            btn_list = dop.btn_lists(stdlist)\n\
            radio_list = dop.radio_lists(stdlist)\n\
            stdlist = dop.sortdir(listdir(path=stdpath))\n\
            destr(btn_list, stdlist, radio_list)\n\
            root.title(stdpath)\n\
        except:\n\
            btn_list = dop.btn_lists(stdlist)\n\
            radio_list = dop.radio_lists(stdlist)\n\
            stdpath = dop.concat(dop.got_back(stdpath))\n\
            stdlist = dop.sortdir(listdir(path=stdpath))\n\
            print(stdpath)\n\
            destr(btn_list, stdlist, radio_list)\n\
def radio_click{1}(event):\n\
    print({1})\n\
{0} = Button(right, text=stdlist[i], bg='old lace')\n\
{0}.bind('<Button-1>', left_click{1})\n\
{0}.place(x=10, y=rast)\n\
var{1} = BooleanVar()\n\
var{1}.set(0)\n\
{2} = Checkbutton(right, variable=var{1}, onvalue=1, offvalue=0,bg='lemon chiffon', command=radio_click{1})\n\
{2}.bind('<Button-1>', radio_click{1})\n\
{2}.place(x=10, y=rast)\n\
"

def sortdir(arg):
    x1, x2 = [i for i in arg if not "." in i], [i for i in arg if "." in i]
    return x1 + x2

def mycopy(arg):
    return [i for i in arg]

def concat(arg):
    return arg + "\\"

def got_back(arg, x="\\"):
    g = str_to_list(arg)[::-1]
    c = "".join(take_while(x, g[1:])[::-1])
    return c

def str_to_list(arg):
    c = [i for i in arg]
    return c

def take_while(f, arg):
    x = mycopy(arg)
    for i in range(len(arg)):
        if "".join(x[i:i+1]) == f:
            return x[i+1:]

def btn_lists(stdlist):
    btn_list = []
    for i in range(len(stdlist)):
        name_btn = "btn" + str(i)
        btn_list.append(name_btn)
    return btn_list

def radio_lists(stdlist):
    btn_list = []
    for i in range(len(stdlist)):
        name_btn = "radio" + str(i)
        btn_list.append(name_btn)
    return btn_list
