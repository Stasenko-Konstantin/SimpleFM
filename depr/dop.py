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
