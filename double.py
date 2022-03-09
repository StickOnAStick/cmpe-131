def doubler(func):
    def wrapper():
        if(type(func()) == None):
           return
        else:
            val = 2*func()
            return val
    return wrapper

def functionToWrap():
    return 1


functionToWrap = doubler(functionToWrap)

functionToWrap()