def doubler(func):
    def wrapper():
        if(func() == None):
            return
        elif():
            func()
            func()
            return 
    return wrapper

def functionToWrap():
    return 1


functionToWrap = doubler(functionToWrap)

functionToWrap()