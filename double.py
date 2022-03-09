
from curses import wrapper


def doubler(func):
    def wrapper():
        if(func() == None):
            return
        elif():
            2 * func()
    return wrapper

def functionToWrap():
    return 1


functionToWrap = doubler(functionToWrap)

functionToWrap()