def doubler(func):
    def wrapper():
            func()
            func()
            return 
    return wrapper

def functionToWrap():
    return 1


functionToWrap = doubler(functionToWrap)

functionToWrap()