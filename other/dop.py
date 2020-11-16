#! Модуль вспомогательных функций

def main(arg):
    result = run(["exec.exe"],
                 capture_output=True,
                 creationflags = CREATE_NO_WINDOW,
                 text=True, input=arg)
    return (result.stdout, result.stderr)

'''def sortdir(arg):
    x1, x2 = [i for i in arg if not "." in i], [i for i in arg if "." in i]
    return x1 + x2

def concat(arg):
    return arg + "\\"'''


