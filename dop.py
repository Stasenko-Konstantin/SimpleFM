#! Модуль вспомогательных функций

def sortdir(arg):
    x1, x2 = [i for i in arg if not "." in i], [i for i in arg if "." in i]
    return x1 + x2

def mycopy(arg):
    return [i for i in arg]

def concat(arg):
    return arg + "\\"

def got_back(arg, x):
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
