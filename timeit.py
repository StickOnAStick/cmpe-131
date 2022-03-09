import time


def calculate_time(func):
    def wrapper():
        time_start = time.time()
        val = func()
        time_end = time.time()
        print("Total time " + str(time_end-time_start))
        return val
    return wrapper

@calculate_time
def howLongDoItakeToRun():
    n = 10000000
    while n > 0:
        n -= 1
    return 


howLongDoItakeToRun()


