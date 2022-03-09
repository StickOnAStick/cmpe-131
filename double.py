def doubler(func):
    def wrapper():
       
            val = 2*func()
            return val
    return wrapper

def functionToWrap():
    return 1


functionToWrap = doubler(functionToWrap)

functionToWrap()