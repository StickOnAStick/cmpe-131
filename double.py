
from curses import wrapper


def doubler(func):
    def wrapper():
       2 * func()
    return wrapper

def functionToWrap():
    return 1


functionToWrap = doubler(functionToWrap)

functionToWrap()