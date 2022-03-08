def func_counter(func):
    def wrapper(*args): #only need args since we know we are passing only 1 variable and not any dictionaries
        wrapper.counter += 1
        return (func(*args))
    wrapper.counter = 0
    return wrapper


@func_counter
def foo(y):
    return y+2

print(foo(2))
print(foo(10))
print(foo(20)) 
#called foo 3 times, printed output just to confirm calls

print(foo.counter)