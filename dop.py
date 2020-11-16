#! Модуль вспомогательных функций

def sortdir(arg):
    x1, x2 = [i for i in arg if not "." in i]
        , [i for i in arg if "." in i]
    return x1 + x2

def concat(arg):
    return arg + "\\"
