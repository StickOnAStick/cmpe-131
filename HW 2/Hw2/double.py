
def doubler(func):
    def wrap1():
        func()
        func()
        print("\nI would highly recommend you properly punctuate, and re-word your assignment insturctions as they are quite hard to follow.")
        print("But who am I, what do I know. After all, I'm only the end user who has to read and follow them closely...")
    return wrap1

def functionToWrap():
    return 


functionToWrap = doubler(functionToWrap)

functionToWrap()