import time


def calculate_time(func):
    def wrapper():
        time_start = time.time()
        print("This is the decorator!")
        func()
        time_end = time.time()
        print("It took " + str(time_end-time_start) + " seconds to run the function")
    return wrapper

@calculate_time
def howLongDoItakeToRun():
    n = 10000000
    while n > 0:
        n -= 1
    return 


howLongDoItakeToRun()


